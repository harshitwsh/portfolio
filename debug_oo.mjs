
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
  // Monkey-patch oo in window context to log when e is not a string
  await send('Runtime.evaluate', {
    expression: `
      const origOo = window.oo;
      window.addEventListener('error', (e) => {
        console.error('Window Error:', e.error?.stack || e.message);
      });
    `
  });
  
  await new Promise(r => setTimeout(r, 4000));
  await fetch('http://localhost:9222/json/close/' + page.id, { method: 'PUT' });
  process.exit(0);
};

ws.onmessage = (msg) => {
  const data = JSON.parse(msg.data);
  if (data.method === 'Runtime.consoleAPICalled') {
    console.log('[CONSOLE ' + data.params.type.toUpperCase() + ']', ...data.params.args.map(a => a.value || a.description || JSON.stringify(a)));
  }
};
