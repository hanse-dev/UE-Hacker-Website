/**
 * Resolves asset URLs for fetch/links. Use when the app may be deployed at a subpath.
 * E.g. with base '/app/', assetUrl('kurse.json') returns '/app/kurse.json'
 */
export function assetUrl(path) {
  const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '') + '/';
  return base + path.replace(/^\//, '');
}
