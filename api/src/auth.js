import crypto from 'crypto';

const TOKEN_TTL_MS = 8 * 60 * 60 * 1000; // 8h
const USER_TOKEN_TTL_MS = 30 * 24 * 60 * 60 * 1000; // 30d

function secret() {
  return process.env.SESSION_SECRET || process.env.ADMIN_PASSWORD || 'dev-insecure-secret';
}

function sign(payloadB64) {
  return crypto.createHmac('sha256', secret()).update(payloadB64).digest('base64url');
}

function createToken(payload, ttlMs) {
  const full = { ...payload, exp: Date.now() + ttlMs };
  const payloadB64 = Buffer.from(JSON.stringify(full)).toString('base64url');
  return `${payloadB64}.${sign(payloadB64)}`;
}

function verifyToken(token) {
  if (!token || typeof token !== 'string' || !token.includes('.')) return null;
  const [payloadB64, sig] = token.split('.');
  if (sign(payloadB64) !== sig) return null;
  try {
    const payload = JSON.parse(Buffer.from(payloadB64, 'base64url').toString('utf8'));
    if (!payload.exp || Date.now() > payload.exp) return null;
    return payload;
  } catch {
    return null;
  }
}

function bearer(req) {
  const header = req.headers.authorization || '';
  return header.startsWith('Bearer ') ? header.slice(7) : '';
}

export function createAdminToken() {
  return createToken({ role: 'admin' }, TOKEN_TTL_MS);
}

export function createUserToken(user) {
  return createToken({
    role: 'user',
    userId: user.id,
    username: user.username,
    ageGroup: user.age_group,
  }, USER_TOKEN_TTL_MS);
}

export function verifyAdminToken(token) {
  const payload = verifyToken(token);
  if (!payload || payload.role !== 'admin') return null;
  return payload;
}

export function verifyUserToken(token) {
  const payload = verifyToken(token);
  if (!payload || payload.role !== 'user' || !payload.userId) return null;
  return payload;
}

export function requireAdmin(req, res, next) {
  const payload = verifyAdminToken(bearer(req));
  if (!payload) {
    return res.status(401).json({ error: 'Admin-Login erforderlich.' });
  }
  req.admin = payload;
  return next();
}

export function requireUser(req, res, next) {
  const payload = verifyUserToken(bearer(req));
  if (!payload) {
    return res.status(401).json({ error: 'Login erforderlich.' });
  }
  req.user = payload;
  return next();
}

export function checkAdminPassword(password) {
  const expected = process.env.ADMIN_PASSWORD;
  if (!expected) {
    throw new Error('ADMIN_PASSWORD is not set');
  }
  const a = Buffer.from(String(password || ''));
  const b = Buffer.from(String(expected));
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}
