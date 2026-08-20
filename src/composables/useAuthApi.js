const USER_TOKEN_KEY = 'ue-hacker-user-token';
const USER_INFO_KEY = 'ue-hacker-user-info';

export function getUserToken() {
  return localStorage.getItem(USER_TOKEN_KEY) || '';
}

export function getUserInfo() {
  try {
    const raw = localStorage.getItem(USER_INFO_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

export function setUserSession(token, user) {
  if (token) localStorage.setItem(USER_TOKEN_KEY, token);
  else localStorage.removeItem(USER_TOKEN_KEY);
  if (user) localStorage.setItem(USER_INFO_KEY, JSON.stringify(user));
  else localStorage.removeItem(USER_INFO_KEY);
}

export function clearUserSession() {
  localStorage.removeItem(USER_TOKEN_KEY);
  localStorage.removeItem(USER_INFO_KEY);
}

async function request(path, { method = 'GET', body, token } = {}) {
  const headers = { Accept: 'application/json' };
  if (body !== undefined) headers['Content-Type'] = 'application/json';
  const auth = token ?? getUserToken();
  if (auth) headers.Authorization = `Bearer ${auth}`;

  const res = await fetch(path, {
    method,
    headers,
    body: body !== undefined ? JSON.stringify(body) : undefined,
  });

  let data = null;
  try {
    data = await res.json();
  } catch {
    data = null;
  }

  if (!res.ok) {
    const err = new Error(data?.error || `Request failed (${res.status})`);
    err.status = res.status;
    err.data = data;
    throw err;
  }
  return data;
}

export function loginUser(username, password) {
  return request('/api/login', {
    method: 'POST',
    body: { username, password },
    token: '',
  });
}

export function fetchMe() {
  return request('/api/me');
}

export function fetchProgress() {
  return request('/api/progress');
}

export function putProgress(payload) {
  return request('/api/progress', { method: 'PUT', body: { payload } });
}
