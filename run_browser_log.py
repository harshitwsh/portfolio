import subprocess

# Launch puppeteer or chrome with a node script to get console errors
script = """
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
  const page = await browser.newPage();
  page.on('console', msg => console.log('LOG:', msg.type(), msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message, err.stack));
  try {
    await page.goto('http://localhost:5173/', { waitUntil: 'domcontentloaded', timeout: 10000 });
    await new Promise(r => setTimeout(r, 4000));
  } catch (e) {
    console.log('GOTO ERROR:', e.message);
  }
  await browser.close();
})();
"""
with open("test_browser_log.mjs", "w", encoding="utf-8") as f:
    f.write(script)

res = subprocess.run(["node", "test_browser_log.mjs"], capture_output=True, text=True)
print(res.stdout)
print(res.stderr)
