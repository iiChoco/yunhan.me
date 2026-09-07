import { $, on, status, download, loadScript, busy } from './common.js';
const ready = Promise.all([loadScript('/vendor/pdf-lib.min.js'), loadScript('/vendor/fflate.js')]); ready.catch(err => status(err.message, true));
let pages = [], totalBytes = 0;
const controls = ['pdf-files', 'pdf-all', 'pdf-none', 'pdf-clear', 'pdf-merge', 'pdf-split'].map($);
function render(focusIndex = null, action = null) {
  const list = $('pdf-pages'); list.replaceChildren();
  pages.forEach((page, i) => {
    const row = document.createElement('div'); row.className = 'pdf-page'; const label = document.createElement('label'); label.className = 'check';
    const check = document.createElement('input'); check.type = 'checkbox'; check.checked = page.selected;
    check.addEventListener('change', () => { page.selected = check.checked; counts(); }); label.append(check, document.createTextNode(`${page.name} · page ${page.index + 1}`)); row.append(label);
    for (const [delta, text] of [[-1, '↑'], [1, '↓']]) {
      const button = document.createElement('button'); button.type = 'button'; button.className = 'chip'; button.textContent = text; button.disabled = i + delta < 0 || i + delta >= pages.length;
      button.setAttribute('aria-label', `Move ${page.name} page ${page.index + 1} ${delta < 0 ? 'up' : 'down'}`);
      button.addEventListener('click', () => { [pages[i], pages[i + delta]] = [pages[i + delta], pages[i]]; render(i + delta, delta); }); row.append(button);
    }
    list.append(row);
  }); counts();
  if (focusIndex !== null) list.children[focusIndex]?.querySelectorAll('button')[action === -1 ? 0 : 1]?.focus();
}
function counts() { const selected = pages.filter(p => p.selected).length; $('pdf-count').textContent = `${selected} of ${pages.length} pages selected`; for (const id of ['pdf-all', 'pdf-none', 'pdf-clear']) $(id).disabled = !pages.length; $('pdf-merge').disabled = $('pdf-split').disabled = !selected; }
on('pdf-files', 'change', async () => {
  const files = [...$('pdf-files').files]; if (!files.length) return;
  await busy(controls, async () => {
    await ready; if (totalBytes + files.reduce((n, f) => n + f.size, 0) > 50 * 1024 * 1024) throw Error('Keep the combined input below 50 MB.');
    const additions = []; let bytes = 0;
    for (const file of files) {
      let doc; try { doc = await PDFLib.PDFDocument.load(await file.arrayBuffer()); } catch { throw Error(`Could not open ${file.name}. Use an unencrypted, valid PDF.`); }
      if (pages.length + additions.length + doc.getPageCount() > 300) throw Error('Use up to 300 pages at a time.');
      for (let index = 0; index < doc.getPageCount(); index++) additions.push({ doc, index, name: file.name, selected: true }); bytes += file.size;
    }
    pages.push(...additions); totalBytes += bytes; status('Pages loaded. Choose what to keep and arrange their order.');
  }); $('pdf-files').value = ''; render();
});
on('pdf-all', 'click', () => { pages.forEach(p => { p.selected = true; }); render(); });
on('pdf-none', 'click', () => { pages.forEach(p => { p.selected = false; }); render(); });
on('pdf-clear', 'click', () => { pages = []; totalBytes = 0; render(); });
async function build(selected) { const output = await PDFLib.PDFDocument.create(); for (const page of selected) { const [copy] = await output.copyPages(page.doc, [page.index]); output.addPage(copy); } return output.save(); }
for (const mode of ['merge', 'split']) on(`pdf-${mode}`, 'click', () => busy([...controls, ...$('pdf-pages').querySelectorAll('button,input')], async () => {
  const selected = pages.filter(p => p.selected); if (!selected.length) throw Error('Select at least one page.'); status('Preparing your download…'); await ready;
  if (mode === 'merge') download(new Blob([await build(selected)], { type: 'application/pdf' }), 'selected-pages.pdf');
  else { const files = {}; for (let i = 0; i < selected.length; i++) { files[`page-${String(i + 1).padStart(3, '0')}.pdf`] = await build([selected[i]]); if (i % 10 === 0) await new Promise(resolve => setTimeout(resolve, 0)); } download(new Blob([fflate.zipSync(files, { level: 0 })], { type: 'application/zip' }), 'split-pages.zip'); }
  status(`Downloaded ${selected.length} selected page${selected.length === 1 ? '' : 's'}.`);
}));
