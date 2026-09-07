import { $, status, copy, busy } from './common.js';

let links = [];
let loaded = false;
async function api(path = '', options = {}) {
  const response = await fetch(`/api/links${path}`, {
    credentials: 'same-origin', cache: 'no-store', signal: AbortSignal.timeout(15000), ...options,
  });
  if (response.status === 401) {
    location.replace('/login?next=/url');
    throw Error('Sign in to manage your links.');
  }
  const data = await response.json();
  if (!response.ok) throw Error(data.reason || 'Couldn’t reach your links. Try again.');
  return data;
}
function render() {
  const active = links.filter(link => link.expires_at * 1000 > Date.now());
  $('links-list').replaceChildren();
  $('links-empty').hidden = active.length > 0;
  $('links-empty').textContent = loaded ? 'No active links. Create one above.' : 'Couldn’t load your links. Select Refresh to try again.';
  for (const link of active) {
    const card = document.createElement('article');
    card.className = 'short-link';
    card.tabIndex = -1;
    const url = new URL(link.path, document.body.dataset.homeOrigin).href;
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.textContent = url;
    anchor.target = '_blank';
    anchor.rel = 'noopener noreferrer';
    const destination = document.createElement('p');
    destination.className = 'hint';
    destination.textContent = link.destination;
    const expiry = document.createElement('time');
    expiry.dateTime = new Date(link.expires_at * 1000).toISOString();
    expiry.textContent = `Expires ${new Date(link.expires_at * 1000).toLocaleString()}`;
    const actions = document.createElement('div');
    actions.className = 'actions';
    const copyButton = document.createElement('button');
    copyButton.className = 'chip';
    copyButton.textContent = 'Copy link';
    copyButton.setAttribute('aria-label', `Copy link ${link.slug}`);
    copyButton.addEventListener('click', async () => {
      try { await copy(url); } catch (error) { status(error.message, true); }
    });
    const revoke = document.createElement('button');
    revoke.className = 'chip';
    revoke.textContent = 'Expire now';
    revoke.setAttribute('aria-label', `Expire ${link.slug} now`);
    revoke.addEventListener('click', async () => {
      await busy([revoke], async () => {
        try {
          await api(`/${link.slug}`, { method: 'DELETE' });
          links = links.filter(item => item.slug !== link.slug);
          render();
          $('refresh-links').focus();
          status('Link expired.');
        } catch (error) { status(error.message, true); }
      });
    });
    actions.append(copyButton, revoke);
    card.append(anchor, destination, expiry, actions);
    $('links-list').append(card);
  }
}
async function refresh() {
  await busy([$('refresh-links')], async () => {
    try {
      const data = await api();
      links = data.links;
      loaded = true;
      render();
    } catch (error) {
      status(error.message, true);
      if (!loaded) render();
    }
  });
}
$('duration-unit').addEventListener('change', () => {
  const max = 86400 / Number($('duration-unit').value);
  $('duration').max = max;
  if (Number($('duration').value) > max) $('duration').value = max;
});
$('shorten-form').addEventListener('submit', async event => {
  event.preventDefault();
  const expires = Number($('duration').value) * Number($('duration-unit').value);
  if (!Number.isInteger(expires) || expires < 60 || expires > 86400) {
    status('Choose an expiration from 1 minute to 24 hours.', true);
    return;
  }
  await busy([$('shorten')], async () => {
    status('Creating link…');
    try {
      const link = await api('', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination: $('destination').value.trim(), expires_in: expires }),
      });
      links.unshift(link);
      render();
      $('links-list').firstElementChild.focus();
      status('Short link created.');
    } catch (error) { status(error.message || 'Couldn’t create a link. Select Refresh before retrying.', true); }
  });
});
$('refresh-links').addEventListener('click', () => { status(); refresh(); });
// Expiration is enforced by Door; remove expired cards without moving focus.
setInterval(() => {
  if (document.activeElement?.closest('.short-link')) return;
  if (links.some(link => link.expires_at * 1000 <= Date.now())) {
    links = links.filter(link => link.expires_at * 1000 > Date.now());
    render();
  }
}, 30000);
refresh();
