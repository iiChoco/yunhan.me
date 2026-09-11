import { $, on, status, download, loadScript, busy } from './common.js';
const ready = Promise.all([loadScript('/vendor/pdf-lib.min.js'), loadScript('/vendor/fflate.js')]);
ready.catch(err => status(err.message, true));
let sources = [], pages = [], nextId = 0, working = false, dragged = null, previewUrl = null;
const plural = n => n === 1 ? 'page' : 'pages';
const selectedPages = () => pages.filter(page => page.selected);
const separate = () => document.querySelector('input[name="pdf-format"]:checked').value === 'separate';
function statusAt(id) { $(id).append($('status')); }
function button(text, action, label = text) {
  const node = document.createElement('button'); node.type = 'button'; node.className = 'chip'; node.textContent = text; node.setAttribute('aria-label', label);
  node.addEventListener('click', action); return node;
}
function counts() {
  const count = selectedPages().length;
  $('pdf-workspace').hidden = $('pdf-export').hidden = !pages.length;
  $('pdf-count').textContent = `${count} of ${pages.length} ${plural(pages.length)} selected`;
  $('pdf-no-selection').hidden = !!count;
  $('pdf-download').disabled = working || !count;
  for (const id of ['pdf-first', 'pdf-last']) $(id).disabled = working || !count || count === pages.length;
  $('pdf-all').disabled = working || count === pages.length; $('pdf-none').disabled = working || !count;
  $('pdf-result').textContent = count ? separate() ? `${count} separate PDF${count === 1 ? '' : 's'} in one ZIP` : `1 PDF · ${count} ${plural(count)} · in the order above` : 'Select pages to prepare a download.';
  $('pdf-download').textContent = separate() ? 'Download ZIP' : 'Download PDF';
  $('pdf-name-help').textContent = `The .${separate() ? 'zip' : 'pdf'} extension is added automatically.`;
  for (const card of $('pdf-pages').children) card.classList.toggle('selected', pages.find(page => String(page.id) === card.dataset.page)?.selected);
}
async function run(action) {
  if (working) return;
  const opener = document.activeElement;
  working = true; $('main').setAttribute('aria-busy', 'true');
  try { await busy([...$('main').querySelectorAll('button,input')], action); }
  catch (err) { status(err.message || String(err), true); }
  finally { working = false; $('main').removeAttribute('aria-busy'); counts(); if (opener?.isConnected && !opener.disabled) opener.focus({ preventScroll: true }); }
}
function focusPage(id, control = 'handle') { $('pdf-pages').querySelector(`[data-page="${id}"] [data-control="${control}"]`)?.focus(); }
function movePage(id, position, control = 'handle') {
  if (working) return;
  statusAt('pdf-workspace');
  const index = pages.findIndex(page => page.id === id);
  const [page] = pages.splice(index, 1); pages.splice(position, 0, page); renderPages(); focusPage(id, control);
  status(`${page.source.name}, page ${page.index + 1}, moved to position ${position + 1}.`);
}
function renderPages() {
  const list = $('pdf-pages'); list.replaceChildren();
  pages.forEach((page, index) => {
    const card = document.createElement('div'); card.className = 'pdf-card'; card.dataset.page = page.id; card.setAttribute('role', 'listitem');
    const head = document.createElement('div'); head.className = 'pdf-card-head';
    const position = document.createElement('span'); position.textContent = `Position ${index + 1}`;
    const handle = button('↕ Move', () => { handle.focus(); status('Drag this handle, press its up or down arrow key, or enter a position below.'); }, `Move ${page.source.name} page ${page.index + 1}; use up and down arrow keys`);
    handle.classList.add('pdf-handle'); handle.dataset.control = 'handle'; handle.draggable = true;
    handle.addEventListener('keydown', event => {
      if (!['ArrowUp', 'ArrowDown', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const target = event.key === 'Home' ? 0 : event.key === 'End' ? pages.length - 1 : index + (event.key === 'ArrowUp' ? -1 : 1);
      if (target >= 0 && target < pages.length) movePage(page.id, target);
    });
    handle.addEventListener('dragstart', event => { if (working) { event.preventDefault(); return; } dragged = page.id; event.dataTransfer.effectAllowed = 'move'; event.dataTransfer.setData('text/plain', String(page.id)); });
    handle.addEventListener('dragend', () => { dragged = null; list.querySelectorAll('.drag-target').forEach(node => node.classList.remove('drag-target')); });
    card.addEventListener('dragover', event => { if (dragged === null || working) return; event.preventDefault(); event.dataTransfer.dropEffect = 'move'; card.classList.add('drag-target'); });
    card.addEventListener('dragleave', event => { if (!card.contains(event.relatedTarget)) card.classList.remove('drag-target'); });
    card.addEventListener('drop', event => { if (dragged === null || working) return; event.preventDefault(); const id = dragged; dragged = null; movePage(id, index); });
    head.append(position, handle);
    const label = document.createElement('label'); label.className = 'check';
    const check = document.createElement('input'); check.type = 'checkbox'; check.checked = page.selected; check.dataset.control = 'check';
    check.addEventListener('change', () => { page.selected = check.checked; counts(); });
    const caption = document.createElement('span'); caption.textContent = `Page ${page.index + 1}`;
    const name = document.createElement('span'); name.className = 'pdf-source-name'; name.textContent = page.source.name; caption.append(name); label.append(check, caption);
    const preview = button('Preview page', () => previewPage(page), `Preview ${page.source.name} page ${page.index + 1}`);
    const moveLabel = document.createElement('label'); moveLabel.className = 'pdf-position'; moveLabel.textContent = 'Move to position';
    const move = document.createElement('input'); move.type = 'number'; move.min = 1; move.max = pages.length; move.value = index + 1; move.dataset.control = 'position';
    move.setAttribute('aria-label', `Position of ${page.source.name} page ${page.index + 1}`);
    move.addEventListener('change', () => {
      const value = Number(move.value);
      if (!Number.isInteger(value) || value < 1 || value > pages.length) { move.value = index + 1; status(`Enter a position from 1 to ${pages.length}.`, true); return; }
      movePage(page.id, value - 1, 'position');
    });
    moveLabel.append(move); card.append(head, label, preview, moveLabel); list.append(card);
  }); counts();
}
function parseRange(value, total) {
  if (value.trim().toLowerCase() === 'all') return new Set(Array.from({ length: total }, (_, i) => i));
  if (!value.trim()) throw Error('Enter pages such as 1–3, 5, or type all.');
  const chosen = new Set();
  for (const part of value.split(',')) {
    const match = part.trim().match(/^(\d+)(?:\s*[-–]\s*(\d+))?$/);
    if (!match) throw Error('Use page numbers and ranges, such as 1-3, 5.');
    const first = Number(match[1]), last = Number(match[2] || match[1]);
    if (first < 1 || last > total || first > last) throw Error(`Use page numbers from 1 to ${total}, with ranges in ascending order.`);
    for (let index = first - 1; index < last; index++) chosen.add(index);
  }
  return chosen;
}
function renderSources() {
  const list = $('pdf-sources'); list.replaceChildren();
  for (const source of sources) {
    const row = document.createElement('div'); row.className = 'pdf-source';
    const heading = document.createElement('div'); heading.className = 'pdf-source-title';
    const title = document.createElement('strong'); title.textContent = source.name;
    const detail = document.createElement('span'); detail.className = 'hint'; detail.textContent = `${source.count} ${plural(source.count)}`; heading.append(title, detail);
    const fields = document.createElement('div'); fields.className = 'pdf-source-controls';
    const label = document.createElement('label'); label.textContent = 'Select pages from this file';
    const input = document.createElement('input'); input.type = 'text'; input.placeholder = 'All, or 1-3, 5'; input.setAttribute('aria-label', `Page range for ${source.name}`); label.append(input);
    const apply = () => {
      statusAt('pdf-add');
      try {
        const chosen = parseRange(input.value, source.count);
        pages.filter(page => page.source === source).forEach(page => { page.selected = chosen.has(page.index); });
        renderPages(); status(`${chosen.size} ${plural(chosen.size)} selected from ${source.name}. Other files are unchanged.`);
      } catch (err) { status(err.message, true); input.focus(); }
    };
    input.addEventListener('keydown', event => { if (event.key === 'Enter') { event.preventDefault(); apply(); } });
    fields.append(label, button('Apply', apply, `Apply page range for ${source.name}`));
    fields.append(button('Move file to start', () => {
      statusAt('pdf-add');
      pages = [...pages.filter(page => page.source === source), ...pages.filter(page => page.source !== source)]; renderPages(); status(`${source.name} moved to the start.`);
    }, `Move all pages of ${source.name} to the start`));
    fields.append(button('Remove file', () => {
      statusAt('pdf-add');
      sources = sources.filter(item => item !== source); pages = pages.filter(page => page.source !== source); renderSources(); renderPages(); $('pdf-files').focus(); status(`${source.name} removed.`);
    }, `Remove ${source.name}`));
    row.append(heading, fields); list.append(row);
  }
  $('pdf-drop').querySelector('p').textContent = sources.length ? 'Drop more PDFs here' : 'Drop PDFs here to get started';
}
async function addFiles(files) {
  if (!files.length || working) return;
  statusAt('pdf-add');
  await run(async () => {
    status('Opening PDFs…'); await ready;
    if (sources.reduce((n, source) => n + source.bytes, 0) + files.reduce((n, file) => n + file.size, 0) > 50 * 1024 * 1024) throw Error('Keep the combined input below 50 MB. Remove a file or choose smaller PDFs.');
    const additions = [], newPages = [];
    // Commit the batch only after every file passes, so a failed addition keeps the current work intact.
    for (const file of files) {
      let doc; try { doc = await PDFLib.PDFDocument.load(await file.arrayBuffer()); } catch { throw Error(`Could not open ${file.name}. Choose a valid PDF without a password.`); }
      const count = doc.getPageCount();
      if (!count) throw Error(`${file.name} has no pages. Choose a PDF with at least one page.`);
      if (pages.length + newPages.length + count > 300) throw Error('Use up to 300 pages at a time. Remove a file or choose a smaller PDF.');
      const source = { name: file.name, doc, count, bytes: file.size }; additions.push(source);
      for (let index = 0; index < count; index++) newPages.push({ id: nextId++, source, index, selected: true });
    }
    sources.push(...additions); pages.push(...newPages);
    status(`Added ${newPages.length} ${plural(newPages.length)}. All new pages are selected; arrange them below or go straight to Download.`);
  });
  $('pdf-files').value = ''; renderSources(); renderPages();
}
on('pdf-files', 'change', () => addFiles([...$('pdf-files').files]));
const drop = $('pdf-drop');
drop.addEventListener('dragover', event => { if (!event.dataTransfer.types.includes('Files')) return; event.preventDefault(); event.dataTransfer.dropEffect = working ? 'none' : 'copy'; if (!working) drop.classList.add('dragging'); });
drop.addEventListener('dragleave', event => { if (!drop.contains(event.relatedTarget)) drop.classList.remove('dragging'); });
drop.addEventListener('drop', event => { event.preventDefault(); drop.classList.remove('dragging'); addFiles([...event.dataTransfer.files]); });
// A misplaced file drop should not navigate away and discard an in-progress arrangement.
for (const type of ['dragover', 'drop']) document.addEventListener(type, event => { if (event.dataTransfer.types.includes('Files')) event.preventDefault(); });
on('pdf-all', 'click', () => { pages.forEach(page => { page.selected = true; }); renderPages(); if (pages.length) focusPage(pages[0].id, 'check'); });
on('pdf-none', 'click', () => { pages.forEach(page => { page.selected = false; }); renderPages(); if (pages.length) focusPage(pages[0].id, 'check'); });
for (const where of ['first', 'last']) on(`pdf-${where}`, 'click', () => {
  statusAt('pdf-workspace');
  const chosen = selectedPages(), rest = pages.filter(page => !page.selected);
  pages = where === 'first' ? [...chosen, ...rest] : [...rest, ...chosen]; renderPages(); status(`Selected pages moved to the ${where === 'first' ? 'start' : 'end'}.`);
});
on('pdf-clear', 'click', () => { statusAt('pdf-add'); sources = []; pages = []; renderSources(); renderPages(); $('pdf-files').focus(); status('Files cleared. Add PDFs to start again.'); });
for (const input of document.querySelectorAll('input[name="pdf-format"]')) input.addEventListener('change', counts);
async function build(chosen) {
  const output = await PDFLib.PDFDocument.create();
  for (const page of chosen) { const [copy] = await output.copyPages(page.source.doc, [page.index]); output.addPage(copy); }
  return output.save();
}
async function previewPage(page) {
  statusAt('pdf-workspace');
  const opener = document.activeElement;
  let url;
  await run(async () => { status('Preparing page preview…'); url = URL.createObjectURL(new Blob([await build([page])], { type: 'application/pdf' })); });
  if (!url) return;
  previewUrl = url; $('pdf-preview-title').textContent = `${page.source.name} · page ${page.index + 1}`;
  $('pdf-preview-frame').src = `${url}#view=Fit&toolbar=0&navpanes=0`; $('pdf-preview-open').href = url; opener?.focus(); $('pdf-preview').showModal(); status();
}
$('pdf-preview-close').addEventListener('click', () => $('pdf-preview').close());
$('pdf-preview').addEventListener('close', () => { $('pdf-preview-frame').removeAttribute('src'); $('pdf-preview-open').removeAttribute('href'); if (previewUrl) URL.revokeObjectURL(previewUrl); previewUrl = null; });
on('pdf-download', 'click', () => run(async () => {
  statusAt('pdf-export');
  const chosen = selectedPages(); if (!chosen.length) throw Error('Select at least one page.');
  const name = $('pdf-name').value.trim().replace(/\.(pdf|zip)$/i, '').replace(/[<>:"/\\|?*\x00-\x1f]/g, '-').replace(/[. ]+$/, '') || 'selected-pages';
  status('Preparing your download…'); await ready;
  if (!separate()) download(new Blob([await build(chosen)], { type: 'application/pdf' }), `${name}.pdf`);
  else {
    const files = {};
    for (let i = 0; i < chosen.length; i++) {
      files[`page-${String(i + 1).padStart(3, '0')}.pdf`] = await build([chosen[i]]);
      if (i % 10 === 0) { status(`Preparing PDF ${i + 1} of ${chosen.length}…`); await new Promise(resolve => setTimeout(resolve, 0)); }
    }
    download(new Blob([fflate.zipSync(files, { level: 0 })], { type: 'application/zip' }), `${name}.zip`);
  }
  status(separate() ? `Downloaded a ZIP with ${chosen.length} separate PDFs, numbered in the order shown.` : `Downloaded one PDF with ${chosen.length} ${plural(chosen.length)}, in the order shown.`);
}));
counts();
