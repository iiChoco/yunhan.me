const endpoint = '/api/store/toolbox-favorites';
const tools = document.querySelector('.tools');
const divider = document.createElement('hr');
divider.className = 'favorites-divider';
divider.setAttribute('aria-label', 'Other tools');
const status = document.querySelector('#favorites-status');
const retry = document.querySelector('#favorites-retry');
const favorites = new Set();
const pending = new Set();
let ready = false;
let loading = false;

const entries = [...document.querySelectorAll('.tool')].map(link => {
  const id = link.dataset.toolId;
  const name = link.querySelector('.tool-name').textContent;
  const wrapper = document.createElement('div');
  wrapper.className = 'tool-entry';
  link.before(wrapper);
  wrapper.append(link);
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'favorite-toggle';
  button.setAttribute('aria-label', `Favorite ${name}`);
  button.setAttribute('aria-pressed', 'false');
  button.disabled = true;
  button.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L3 9.6l6.2-.9Z"/></svg>';
  wrapper.append(button);
  button.addEventListener('click', () => toggle(id, name));
  return { id, wrapper, button };
});

function render() {
  const focused = document.activeElement;
  for (const { id, wrapper, button } of entries) {
    const selected = favorites.has(id);
    button.setAttribute('aria-pressed', String(selected));
    button.disabled = !ready;
    // Keep focus during saves; the click guard prevents duplicate requests.
    button.setAttribute('aria-disabled', String(!ready || pending.has(id)));
    button.setAttribute('aria-busy', String(pending.has(id)));
  }
  const saved = entries.filter(entry => favorites.has(entry.id));
  const others = entries.filter(entry => !favorites.has(entry.id));
  divider.hidden = saved.length === 0 || others.length === 0;
  const ordered = [...saved.map(entry => entry.wrapper), divider, ...others.map(entry => entry.wrapper)];
  // Reorder the DOM as well as the grid so keyboard navigation follows the groups.
  ordered.forEach((node, index) => {
    if (tools.children[index] !== node) tools.insertBefore(node, tools.children[index] || null);
  });
  // Moving an entry can blur its star; keep focus on the same control.
  if (focused && tools.contains(focused) && document.activeElement !== focused) {
    focused.focus({ preventScroll: true });
  }
}

async function request(path, options = {}) {
  const response = await fetch(path, {
    credentials: 'same-origin', cache: 'no-store', signal: AbortSignal.timeout(15000), ...options,
  });
  if (response.status === 401) {
    ready = false;
    render();
    window.location.replace('/login?next=/toolbox');
    throw new Error('Sign in to save favorites.');
  }
  // Removing an already-removed star is successful (another device may have done it).
  if (!response.ok && !(options.method === 'DELETE' && response.status === 404)) {
    throw new Error('Favorites are unavailable.');
  }
  return response;
}

async function load() {
  if (loading || pending.size) return;
  loading = true;
  ready = false;
  retry.hidden = true;
  status.textContent = 'Loading favorites…';
  render();
  try {
    const data = await (await request(endpoint)).json();
    if (!Array.isArray(data.keys)) throw new Error('Invalid favorites.');
    const known = new Set(entries.map(entry => entry.id));
    favorites.clear();
    for (const item of data.keys) {
      if (known.has(item.key)) favorites.add(item.key);
    }
    ready = true;
    status.textContent = '';
  } catch {
    favorites.clear();
    status.textContent = 'Couldn’t load favorites. Your tools still work.';
    retry.hidden = false;
  } finally {
    loading = false;
    render();
  }
}

async function toggle(id, name) {
  if (!ready || pending.has(id)) return;
  const adding = !favorites.has(id);
  pending.add(id);
  status.textContent = 'Saving…';
  retry.hidden = true;
  render();
  try {
    await request(`${endpoint}/${id}`, adding ? {
      method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: '{}',
    } : { method: 'DELETE' });
    if (adding) favorites.add(id);
    else favorites.delete(id);
    status.textContent = `${name} ${adding ? 'added to' : 'removed from'} favorites.`;

  } catch {
    status.textContent = `Couldn’t save ${name}. Retry to refresh your favorites.`;
    retry.hidden = false;
  } finally {
    pending.delete(id);
    render();
  }
}

retry.addEventListener('click', load);
// Refresh when returning from another device or tab, without interrupting a save.
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible') load();
});
window.addEventListener('pageshow', event => { if (event.persisted) load(); });
load();
