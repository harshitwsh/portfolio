
import fs from "node:fs";

const viewports = [
  { name: "desktop_1920x1080", width: 1920, height: 1080 },
  { name: "laptop_1440x900", width: 1440, height: 900 },
  { name: "laptop_1366x768", width: 1366, height: 768 },
  { name: "tablet_1024x768", width: 1024, height: 768 },
  { name: "tablet_portrait_834x1194", width: 834, height: 1194 },
  { name: "tablet_portrait_768x1024", width: 768, height: 1024 },
  { name: "mobile_430x932", width: 430, height: 932 },
  { name: "mobile_390x844", width: 390, height: 844 },
  { name: "mobile_375x812", width: 375, height: 812 },
];

for (let vp of viewports) {
  const res = await fetch("http://localhost:9222/json/new?http://localhost:5173/?v=" + Date.now(), { method: "PUT" });
  const page = await res.json();
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  let reqId = 1;

  function send(method, params = {}) {
    return new Promise((resolve) => {
      const id = reqId++;
      const handler = (msg) => {
        const data = JSON.parse(msg.data);
        if (data.id === id) {
          ws.removeEventListener("message", handler);
          resolve(data.result);
        }
      };
      ws.addEventListener("message", handler);
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  await new Promise(resolve => {
    ws.onopen = async () => {
      await send("Page.enable");
      await send("Runtime.enable");
      await send("Emulation.setDeviceMetricsOverride", {
        width: vp.width,
        height: vp.height,
        deviceScaleFactor: 2,
        mobile: vp.width < 768
      });

      await new Promise(r => setTimeout(r, 2000));

      const shot = await send("Page.captureScreenshot", { format: "png" });
      fs.writeFileSync(`audit_intro_${vp.name}.png`, Buffer.from(shot.data, "base64"));
      console.log(`Saved audit_intro_${vp.name}.png`);

      await fetch("http://localhost:9222/json/close/" + page.id, { method: "PUT" });
      resolve();
    };
  });
}
console.log("Intro audit complete!");
