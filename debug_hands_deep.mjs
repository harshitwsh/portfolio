
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

  let check = await send('Runtime.evaluate', {
    expression: `
      (() => {
        const app = window.$ || window.app;
        const s = window.oA?._activeSegment?.id;
        const comps = window.0.components;
        let handDetails = null;
        if (comps?.handsModel) {
          const hm = comps.handsModel;
          const meshes = [];
          hm.group.traverse(obj => {
            if (obj.isMesh || obj.isSkinnedMesh) {
              meshes.push({
                name: obj.name,
                visible: obj.visible,
                matName: obj.material?.constructor?.name,
                matVisible: obj.material?.visible,
                opacity: obj.material?.opacity,
                transparent: obj.material?.transparent,
                pos: obj.position.toArray(),
                scale: obj.scale.toArray()
              });
            }
          });
          handDetails = {
            groupVisible: hm.group.visible,
            groupParent: hm.group.parent ? hm.group.parent.constructor.name : null,
            groupPos: hm.group.position.toArray(),
            meshes: meshes,
            cameraPos: window.$.camera.position.toArray()
          };
        }
        return {
          segment: s,
          scrollProgress: window.oA?._scrollProgress,
          hasHandsModel: !!comps?.handsModel,
          handDetails: handDetails
        };
      })()
    `,
    returnByValue: true
  });
  console.log('HANDS DIAGNOSTICS:', JSON.stringify(check.result?.value, null, 2));

  await fetch('http://localhost:9222/json/close/' + page.id, { method: 'PUT' });
  process.exit(0);
};
