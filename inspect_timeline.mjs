
const res = await fetch('http://localhost:9222/json/new?http://localhost:5173/', { method: 'PUT' });
const page = await res.json();

const ws = new WebSocket(page.webSocketDebuggerUrl);
let reqId = 1;

function send(method, params = {}) {
  return new Promise((resolve) => {
    const id = reqId++;
    const handler = (msg) => {
      const data = JSON.parse(msg.data);
      if (data.id === id) {
        ws.removeEventListener('message', handler);
        resolve(data.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

ws.onopen = async () => {
  await send('Page.enable');
  await send('Runtime.enable');
  
  for (let s = 1; s <= 12; s++) {
    await new Promise(r => setTimeout(r, 1000));
    const info = await send('Runtime.evaluate', {
      expression: '({ time: ' + s + ', status: document.querySelector(".hud-status-label")?.textContent, ariaVal: document.querySelector(".loader-container")?.getAttribute("aria-valuenow"), pre99: document.getElementById("pre-canvas-99")?.style.display })',
      returnByValue: true
    });
    console.log(JSON.stringify(info.result.value));
  }

  await fetch('http://localhost:9222/json/close/' + page.id, { method: 'PUT' });
  process.exit(0);
};
