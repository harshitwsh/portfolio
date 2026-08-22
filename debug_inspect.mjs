
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

ws.onmessage = (msg) => {
  const data = JSON.parse(msg.data);
  if (data.method === 'Runtime.consoleAPICalled') {
    console.log('[LOG ' + data.params.type + ']', ...data.params.args.map(a => a.value || a.description || JSON.stringify(a)));
  } else if (data.method === 'Runtime.exceptionThrown') {
    console.log('[EXCEPTION]', data.params.exceptionDetails.text, data.params.exceptionDetails.exception?.description || data.params.exceptionDetails.exception?.value);
  }
};

ws.onopen = async () => {
  await send('Page.enable');
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

  console.log('H drawn. Waiting 5s...');
  await new Promise(r => setTimeout(r, 5000));

  let res = await send('Runtime.evaluate', {
    expression: `
      (() => {
        const app = window.$;
        return {
          segment: window.oA?._activeSegment?.id,
          components: Object.keys(app?.components || {}),
          hasHandsModel: !!app?.components?.handsModel,
          handsChildrenCount: app?.components?.handsModel?.group?.children?.length,
          handsPosition: app?.components?.handsModel?.group?.position?.toArray(),
          handsVisible: app?.components?.handsModel?.group?.visible,
          cameraPos: app?.camera?.position?.toArray(),
          cameraQuaternion: app?.camera?.quaternion?.toArray(),
          scrollProgress: window.oA?._scrollProgress
        };
      })()
    `,
    returnByValue: true
  });
  console.log('App components result:', JSON.stringify(res.result?.value, null, 2));

  await fetch('http://localhost:9222/json/close/' + page.id, { method: 'PUT' });
  process.exit(0);
};
