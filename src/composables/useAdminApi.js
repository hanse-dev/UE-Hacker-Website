const ADMIN_TOKEN_KEY = 'ue-hacker-admin-token';

export function getAdminToken() {
  return sessionStorage.getItem(ADMIN_TOKEN_KEY) || '';
}

export function setAdminToken(token) {
  if (token) sessionStorage.setItem(ADMIN_TOKEN_KEY, token);
  else sessionStorage.removeItem(ADMIN_TOKEN_KEY);
}

async function request(path, { method = 'GET', body, token } = {}) {
  const headers = { Accept: 'application/json' };
  if (body !== undefined) headers['Content-Type'] = 'application/json';
  const auth = token ?? getAdminToken();
  if (auth) headers.Authorization = `Bearer ${auth}`;

  const res = await fetch(path, {
    method,
    headers,
    body: body !== undefined ? JSON.stringify(body) : undefined,
  });

  if (res.status === 204) return null;

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

export function adminLogin(password) {
  return request('/api/admin/login', { method: 'POST', body: { password }, token: '' });
}

export function listUsers() {
  return request('/api/admin/users');
}

export function createUser(payload) {
  return request('/api/admin/users', { method: 'POST', body: payload });
}

export function updateUser(id, payload) {
  return request(`/api/admin/users/${id}`, { method: 'PATCH', body: payload });
}

export function deleteUser(id) {
  return request(`/api/admin/users/${id}`, { method: 'DELETE' });
}
