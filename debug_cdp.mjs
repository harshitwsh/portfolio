
const res = await fetch('http://localhost:9222/json/new?http://localhost:5173/', { method: 'PUT' });
const page = await res.json();
console.log('Opened page:', page.id);

const ws = new WebSocket(page.webSocketDebuggerUrl);
let reqId = 1;

function send(method, params = {}) {
  ws.send(JSON.stringify({ id: reqId++, method, params }));
}

ws.onopen = () => {
  console.log('WS connected');
  send('Page.enable');
  send('Runtime.enable');
  send('Log.enable');
  send('Network.enable');
};

ws.onmessage = (msg) => {
  const data = JSON.parse(msg.data);
  if (data.method === 'Runtime.consoleAPICalled') {
    console.log('[CONSOLE ' + data.params.type.toUpperCase() + ']', ...data.params.args.map(a => a.value || a.description || JSON.stringify(a)));
  } else if (data.method === 'Runtime.exceptionThrown') {
    console.log('[EXCEPTION]', data.params.exceptionDetails.text, data.params.exceptionDetails.exception?.description || data.params.exceptionDetails.exception?.value);
  } else if (data.method === 'Log.entryAdded') {
    console.log('[LOG ' + data.params.entry.level + ']', data.params.entry.text);
  } else if (data.method === 'Network.loadingFailed') {
    console.log('[NETWORK FAILED]', data.params.errorText, data.params.type);
  } else if (data.result && data.result.result) {
    console.log('[EVAL RESULT]', JSON.stringify(data.result.result));
  }
};

setTimeout(async () => {
  console.log('--- 8 seconds elapsed ---');
  send('Runtime.evaluate', {
    expression: 'document.body.innerHTML',
    returnByValue: true
  });
}, 8000);

setTimeout(async () => {
  await fetch('http://localhost:9222/json/close/' + page.id, { method: 'PUT' });
  process.exit(0);
}, 11000);
