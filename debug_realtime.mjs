
import fs from 'node:fs';

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
  await send('Runtime.enable');
  await send('Input.enable');
  
  while (true) {
    const st = await send('Runtime.evaluate', {
      expression: 'document.querySelector(".hud-status-label")?.textContent',
      returnByValue: true
    });
    if (st.result?.value === 'DRAW A H') {
      break;
    }
    await new Promise(r => setTimeout(r, 200));
  }

  // Draw H
  await send('Input.dispatchMouseEvent', { type: 'mousePressed', x: 450, y: 250, button: 'left', clickCount: 1 });
  for (let y = 250; y <= 550; y += 20) {
    await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: 450, y, button: 'left' });
    await new Promise(r => setTimeout(r, 15));
  }
  await send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: 450, y: 550, button: 'left' });
  await new Promise(r => setTimeout(r, 80));

  await send('Input.dispatchMouseEvent', { type: 'mousePressed', x: 650, y: 250, button: 'left', clickCount: 1 });
  for (let y = 250; y <= 550; y += 20) {
    await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: 650, y, button: 'left' });
    await new Promise(r => setTimeout(r, 15));
  }
  await send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: 650, y: 550, button: 'left' });
  await new Promise(r => setTimeout(r, 80));

  await send('Input.dispatchMouseEvent', { type: 'mousePressed', x: 450, y: 400, button: 'left', clickCount: 1 });
  for (let x = 450; x <= 650; x += 20) {
    await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x, y: 400, button: 'left' });
    await new Promise(r => setTimeout(r, 15));
  }
  await send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: 650, y: 400, button: 'left' });

  await new Promise(r => setTimeout(r, 4500));

  let info = await send('Runtime.evaluate', {
    expression: `
      (() => {
        const app = window.__ZERO_APP__;
        const oA = window.__ZERO_OA__;
        const comps = app?.components;
        const hm = comps?.handsModel;
        const tl = comps?.textLayout;
        return {
          segmentId: oA?._activeSegment?.id,
          scrollProgress: oA?._scrollProgress,
          hasHm: !!hm,
          hmGroupVisible: hm?.group?.visible,
          hmChildrenCount: hm?.group?.children?.length,
          hmGroupPos: hm?.group?.position?.toArray(),
          hasTl: !!tl,
          tlSpritesCount: tl?.sprites?.length,
          tlSprites: tl?.sprites?.map(sp => ({
            visible: sp.visible,
            opacity: sp.userData?.material?.opacity,
            pos: sp.position.toArray(),
            scale: sp.scale.toArray()
          })),
          cameraPos: app?.camera?.position?.toArray()
        };
      })()
    `,
    returnByValue: true
  });
  console.log('REALTIME STAGE 1 INFO:', JSON.stringify(info.result?.value, null, 2));

  await fetch('http://localhost:9222/json/close/' + page.id, { method: 'PUT' });
  process.exit(0);
};
