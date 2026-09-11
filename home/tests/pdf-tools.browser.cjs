/** Local browser checks for PDF selection, ordering, output bytes, previews, recovery,
 * keyboard controls, and narrow layouts. Uses temporary PDFs and a loopback-only
 * fixture server; no Door accounts or production data are read. Requires Playwright
 * and a local Chrome installation, with optional CHROME_PATH and PDF_CHECK_OUTPUT.
 */
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const os = require('node:os');
const http = require('node:http');
const { chromium } = require('playwright');
const PDFLib = require('../public/vendor/pdf-lib.min.js');
const { unzipSync } = require('../public/vendor/fflate.js');
const home = path.resolve(__dirname, '..');
let checks = 0;
function check(name, ok) { assert.ok(ok, name); console.log(`  ok  ${name}`); checks++; }
async function fixture(widths) {
  const doc = await PDFLib.PDFDocument.create();
  for (const width of widths) {
    const page = doc.addPage([width, 600]);
    page.drawRectangle({ x: 0, y: 0, width, height: 600, color: PDFLib.rgb(.08, .18, .23) });
    page.drawText(`Test page ${width}`, { x: 30, y: 500, size: 28, color: PDFLib.rgb(.91, .79, .54) });
  }
  return Buffer.from(await doc.save());
}
const payload = (name, buffer) => ({ name, mimeType: 'application/pdf', buffer });
async function widths(buffer) { return (await PDFLib.PDFDocument.load(buffer)).getPages().map(page => page.getWidth()); }
(async () => {
  const output = process.env.PDF_CHECK_OUTPUT || await fs.mkdtemp(path.join(os.tmpdir(), 'pdf-tool-checks-'));
  await fs.mkdir(output, { recursive: true });
  const server = http.createServer(async (req, res) => {
    try {
      const url = new URL(req.url, 'http://localhost');
      const filename = url.pathname === '/pdf' ? path.join(home, 'private/utilities/pdf-tools.html') : path.resolve(home, 'public', `.${url.pathname}`);
      if (!filename.startsWith(home + path.sep)) { res.writeHead(403).end(); return; }
      let content = await fs.readFile(filename);
      if (url.pathname === '/pdf') content = Buffer.from(content.toString().replaceAll('{{HOME_ORIGIN}}', ''));
      res.setHeader('Content-Type', ({ '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' })[path.extname(filename)] || 'application/octet-stream');
      res.end(content);
    } catch { res.writeHead(404).end(); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const origin = `http://127.0.0.1:${server.address().port}`;
  let browser;
  try {
    browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
    const context = await browser.newContext({ acceptDownloads: true });
    const page = await context.newPage();
    const errors = [], requests = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('request', request => requests.push({ url: request.url(), method: request.method() }));
    await page.setViewportSize({ width: 1280, height: 1000 });
    await page.goto(`${origin}/pdf`);
    const a = payload('Meeting notes.pdf', await fixture([401, 402, 403]));
    const b = payload('Appendix.pdf', await fixture([501, 502]));
    const add = async files => { await page.locator('#pdf-files').setInputFiles(files); await page.waitForFunction(() => !document.querySelector('#main').hasAttribute('aria-busy')); };
    const count = () => page.locator('.pdf-card').count();
    let lastDownload = 0;
    const download = async () => {
      // Chrome limits bursts of automatic downloads, including rapid user-click simulations.
      await page.waitForTimeout(Math.max(0, 1100 - (Date.now() - lastDownload)));
      lastDownload = Date.now();
      const pending = page.waitForEvent('download'); await page.locator('#pdf-download').click();
      const result = await pending.catch(async error => { console.error('Download state:', await page.locator('#status').textContent(), await page.locator('#main').getAttribute('aria-busy'), errors); throw error; }); const buffer = await fs.readFile(await result.path());
      return { name: result.suggestedFilename(), buffer };
    };
    const order = async () => widths((await download()).buffer);
    check('the empty view asks for files before showing page and export controls', await page.locator('#pdf-drop').isVisible() && !await page.locator('#pdf-workspace').isVisible() && !await page.locator('#pdf-export').isVisible());
    await page.screenshot({ path: path.join(output, 'empty-desktop.png'), fullPage: true });
    await add([a, b]);
    check('adding multiple files selects all five pages and states the combined result', await count() === 5 && await page.locator('#pdf-result').textContent() === '1 PDF · 5 pages · in the order above');
    check('the combined PDF contains actual pages in input order', JSON.stringify(await order()) === '[401,402,403,501,502]');
    await page.getByRole('textbox', { name: 'Page range for Meeting notes.pdf', exact: true }).fill('1–2, 2');
    await page.getByRole('button', { name: 'Apply page range for Meeting notes.pdf', exact: true }).click();
    check('ranges accept en dashes and deduplicate pages while preserving other files', JSON.stringify(await order()) === '[401,402,501,502]');
    await page.getByRole('textbox', { name: 'Page range for Meeting notes.pdf', exact: true }).fill('0, 99');
    await page.getByRole('button', { name: 'Apply page range for Meeting notes.pdf', exact: true }).click();
    check('invalid ranges report an error without changing selection', await page.locator('#status').evaluate(node => node.classList.contains('error')) && JSON.stringify(await order()) === '[401,402,501,502]');
    await page.getByRole('textbox', { name: 'Page range for Meeting notes.pdf', exact: true }).fill('all');
    await page.getByRole('textbox', { name: 'Page range for Meeting notes.pdf', exact: true }).press('Enter');
    check('a range can be applied using the keyboard', JSON.stringify(await order()) === '[401,402,403,501,502]');
    await page.getByRole('spinbutton', { name: 'Position of Appendix.pdf page 2', exact: true }).fill('1');
    await page.getByRole('spinbutton', { name: 'Position of Appendix.pdf page 2', exact: true }).press('Enter');
    await page.getByRole('spinbutton', { name: 'Position of Appendix.pdf page 2', exact: true }).blur();
    check('a page jumps directly to the requested position', JSON.stringify(await order()) === '[502,401,402,403,501]');
    await page.getByRole('button', { name: 'Move Appendix.pdf page 2; use up and down arrow keys', exact: true }).focus();
    await page.keyboard.press('End');
    check('keyboard reordering moves the page and keeps focus on its handle', await page.evaluate(() => document.activeElement.getAttribute('aria-label').includes('Appendix.pdf page 2')) && JSON.stringify(await order()) === '[401,402,403,501,502]');
    await page.locator('#pdf-pages').scrollIntoViewIfNeeded();
    const dragFrom = await page.getByRole('button', { name: 'Move Appendix.pdf page 2; use up and down arrow keys', exact: true }).boundingBox();
    const dragTo = await page.locator('.pdf-card').first().boundingBox();
    await page.mouse.move(dragFrom.x + dragFrom.width / 2, dragFrom.y + dragFrom.height / 2);
    await page.mouse.down();
    await page.mouse.move(dragFrom.x + dragFrom.width / 2 + 12, dragFrom.y + dragFrom.height / 2, { steps: 5 });
    await page.mouse.move(dragTo.x + 10, dragTo.y + 10, { steps: 12 });
    await page.mouse.up();
    check('dragging a page handle changes exported order', JSON.stringify(await order()) === '[502,401,402,403,501]');
    await page.getByRole('button', { name: 'Move all pages of Meeting notes.pdf to the start', exact: true }).click();
    check('a whole file moves together and keeps its page order', JSON.stringify(await order()) === '[401,402,403,502,501]');
    await page.locator('#pdf-none').click();
    check('zero selected pages disables download and explains how to continue', await page.locator('#pdf-download').isDisabled() && await page.locator('#pdf-no-selection').isVisible());
    await page.locator('.pdf-card').nth(1).getByRole('checkbox').check();
    await page.locator('.pdf-card').nth(3).getByRole('checkbox').check();
    await page.locator('#pdf-first').click();
    check('selected pages move as a group while preserving relative order', JSON.stringify(await order()) === '[402,502]' && (await page.locator('.pdf-card .check').allTextContents()).slice(0, 2).join('|').includes('Page 2Meeting notes.pdf|Page 2Appendix.pdf'));
    await page.locator('#pdf-last').click();
    check('moving selected pages to the end keeps unchecked pages outside the export', JSON.stringify(await order()) === '[402,502]');
    await page.locator('#pdf-name').fill('My pages.pdf');
    check('download names do not duplicate the PDF extension', (await download()).name === 'My pages.pdf');
    await page.locator('input[name="pdf-format"][value="combined"]').focus(); await page.keyboard.press('ArrowRight');
    check('keyboard output selection describes the ZIP explicitly', await page.locator('#pdf-result').textContent() === '2 separate PDFs in one ZIP' && await page.locator('#pdf-download').textContent() === 'Download ZIP');
    const zip = await download(), contents = unzipSync(zip.buffer);
    check('the ZIP contains one real PDF per selected page in shown order', zip.name === 'My pages.zip' && Object.keys(contents).join(',') === 'page-001.pdf,page-002.pdf' && JSON.stringify(await widths(contents['page-001.pdf'])) === '[402]' && JSON.stringify(await widths(contents['page-002.pdf'])) === '[502]');
    await page.locator('input[name="pdf-format"][value="combined"]').check();
    check('changing output format preserves page selection and order', JSON.stringify(await order()) === '[402,502]');
    const before = await count();
    await add([payload('Good addition.pdf', await fixture([601])), payload('Broken.pdf', Buffer.from('not a PDF'))]);
    check('a partially valid upload batch leaves existing work intact', await count() === before && (await page.locator('#status').textContent()).includes('Could not open Broken.pdf'));
    check('upload failures preserve the existing download contents', JSON.stringify(await order()) === '[402,502]');
    await page.getByRole('button', { name: 'Preview Meeting notes.pdf page 2', exact: true }).click();
    await page.locator('#pdf-preview').waitFor({ state: 'visible' });
    const previewBytes = await page.locator('#pdf-preview-open').evaluate(async link => Array.from(new Uint8Array(await (await fetch(link.href)).arrayBuffer())));
    check('the preview contains exactly the requested source page', JSON.stringify(await widths(Uint8Array.from(previewBytes))) === '[402]');
    await page.waitForTimeout(1200);
    await page.screenshot({ path: path.join(output, 'preview-desktop.png'), fullPage: false });
    await page.keyboard.press('Escape');
    check('Escape closes the preview and returns focus to its opener', !await page.locator('#pdf-preview').isVisible() && await page.evaluate(() => document.activeElement.getAttribute('aria-label') === 'Preview Meeting notes.pdf page 2'));
    await page.waitForFunction(() => !document.querySelector('#pdf-preview-frame').hasAttribute('src'));
    check('closing the preview releases the frame URL', !await page.locator('#pdf-preview-frame').getAttribute('src') && !await page.locator('#pdf-preview-open').getAttribute('href'));
    await page.locator('#pdf-all').click();
    await add([payload('A very long filename <img src=x onerror=alert(1)> & meeting notes with many words and symbols.pdf', await fixture([701]))]);
    check('filenames are displayed as text', await page.locator('#pdf-sources img').count() === 0 && await page.locator('#pdf-sources').textContent().then(text => text.includes('<img src=x')));
    for (const width of [320, 390, 1280]) {
      await page.setViewportSize({ width, height: 900 });
      check(`the populated layout fits at ${width} pixels`, await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
      await page.screenshot({ path: path.join(output, `populated-${width}.png`), fullPage: true });
      await page.locator('#pdf-workspace').screenshot({ path: path.join(output, `pages-${width}.png`) });
      await page.locator('#pdf-export').screenshot({ path: path.join(output, `export-${width}.png`) });
    }
    await page.setViewportSize({ width: 390, height: 900 });
    await page.getByRole('button', { name: 'Preview Meeting notes.pdf page 1', exact: true }).click();
    await page.locator('#pdf-preview').waitFor({ state: 'visible' });
    check('the preview fits a narrow viewport', await page.locator('#pdf-preview').evaluate(node => node.getBoundingClientRect().right <= innerWidth && node.getBoundingClientRect().left >= 0));
    await page.waitForTimeout(1200);
    await page.screenshot({ path: path.join(output, 'preview-mobile.png'), fullPage: false });
    await page.locator('#pdf-preview-close').click();
    await page.getByRole('button', { name: 'Remove Appendix.pdf', exact: true }).click();
    check('removing a source removes only its pages', await count() === 4 && JSON.stringify(await order()) === '[401,403,402,701]');
    await page.locator('#pdf-clear').click();
    check('clearing files returns to the empty state and focuses the picker', !await page.locator('#pdf-workspace').isVisible() && await page.evaluate(() => document.activeElement.id === 'pdf-files'));
    await page.evaluate(() => {
      const transfer = new DataTransfer(); transfer.items.add(new File([new Uint8Array(51 * 1024 * 1024)], 'Too large.pdf', { type: 'application/pdf' }));
      document.querySelector('#pdf-drop').dispatchEvent(new DragEvent('drop', { bubbles: true, dataTransfer: transfer }));
    });
    await page.waitForFunction(() => !document.querySelector('#main').hasAttribute('aria-busy'));
    check('oversized file drops report the limit and add no pages', (await page.locator('#status').textContent()).includes('50 MB') && await count() === 0);
    await add([payload('Too many.pdf', await fixture(Array(301).fill(420)))]);
    check('PDFs over the page limit are rejected without partial additions', (await page.locator('#status').textContent()).includes('300 pages') && await count() === 0);
    await page.evaluate(async bytes => {
      const transfer = new DataTransfer(); transfer.items.add(new File([new Uint8Array(bytes)], 'Dropped.pdf', { type: 'application/pdf' }));
      document.querySelector('#pdf-drop').dispatchEvent(new DragEvent('drop', { bubbles: true, dataTransfer: transfer }));
    }, Array.from(a.buffer));
    await page.waitForFunction(() => document.querySelectorAll('.pdf-card').length === 3);
    check('a valid drop works after limit failures', JSON.stringify(await order()) === '[401,402,403]');
    await page.evaluate(() => {
      window.restoreCreate = PDFLib.PDFDocument.create;
      PDFLib.PDFDocument.create = async () => { throw Error('Simulated export failure'); };
    });
    await page.locator('#pdf-download').click();
    await page.waitForFunction(() => !document.querySelector('#main').hasAttribute('aria-busy'));
    check('an export failure restores the controls and reports the error', await page.locator('#pdf-download').isEnabled() && (await page.locator('#status').textContent()).includes('Simulated export failure'));
    await page.evaluate(() => { PDFLib.PDFDocument.create = window.restoreCreate; });
    check('export can be retried after a failure', JSON.stringify(await order()) === '[401,402,403]');
    await page.locator('.pdf-handle').first().focus();
    await page.keyboard.press('Home');
    check('keyboard controls have a visible focus outline', await page.locator('.pdf-handle').first().evaluate(node => getComputedStyle(node).outlineStyle !== 'none' && getComputedStyle(node).outlineWidth === '2px'));
    await page.evaluate(() => {
      const load = PDFLib.PDFDocument.load;
      PDFLib.PDFDocument.load = async (...args) => { await new Promise(resolve => { window.finishLoading = resolve; }); return load(...args); };
      window.restoreLoad = () => { PDFLib.PDFDocument.load = load; };
    });
    await page.locator('#pdf-files').setInputFiles(b);
    await page.waitForFunction(() => typeof window.finishLoading === 'function');
    check('adding a file locks existing page and output controls', await page.locator('.pdf-handle').first().isDisabled() && await page.locator('input[name="pdf-format"]').first().isDisabled() && await page.locator('#pdf-download').isDisabled());
    await page.evaluate(bytes => {
      const transfer = new DataTransfer(); transfer.items.add(new File([new Uint8Array(bytes)], 'Ignored during load.pdf', { type: 'application/pdf' }));
      document.querySelector('#pdf-drop').dispatchEvent(new DragEvent('drop', { bubbles: true, dataTransfer: transfer }));
      window.restoreLoad(); window.finishLoading();
    }, Array.from(a.buffer));
    await page.waitForFunction(() => !document.querySelector('#main').hasAttribute('aria-busy'));
    check('a concurrent drop cannot interleave with an in-progress addition', await count() === 5 && !(await page.locator('#pdf-sources').textContent()).includes('Ignored during load'));
    await page.locator('#pdf-clear').click();
    await add([payload('Long document.pdf', await fixture(Array.from({ length: 300 }, (_, i) => 400 + i)))]);
    check('a document at the page limit fits the bounded grid', await count() === 300 && await page.locator('#pdf-pages').evaluate(node => node.clientHeight <= 620 && node.scrollHeight > node.clientHeight));
    const longOrder = await order();
    check('all 300 pages export without truncation', longOrder.length === 300 && longOrder[0] === 400 && longOrder[299] === 699);
    // Chrome's built-in viewer loads browser resources locally, without a network origin.
    check('processing sends no input uploads or external requests', requests.every(request => request.method === 'GET' && (request.url.startsWith(origin + '/') || request.url.startsWith('blob:') || request.url.startsWith('chrome://resources/') || request.url.startsWith('chrome-extension://mhjfbmdgcfjbbpaeojofohoefgiehjai/'))));
    check('the page has no uncaught JavaScript errors', errors.length === 0);
    const failed = await context.newPage();
    await failed.route('**/vendor/pdf-lib.min.js', route => route.abort());
    await failed.goto(`${origin}/pdf`);
    await failed.waitForFunction(() => document.querySelector('#status').classList.contains('error'));
    check('missing libraries explain how to recover', (await failed.locator('#status').textContent()).includes('Refresh and try again'));
    console.log(`\nAll ${checks} checks passed. Screenshots: ${output}`);
  } finally { if (browser) await browser.close(); await new Promise(resolve => server.close(resolve)); }
})().catch(error => { console.error(error); process.exitCode = 1; });
