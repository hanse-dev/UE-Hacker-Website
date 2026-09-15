import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  // Bei Deployment unter Subpath (z.B. /ue-hacker/) base setzen:
  // base: '/ue-hacker/',
  plugins: [vue()],
  assetsInclude: ['**/*.ipynb'],
  resolve: {
    alias: {
      '@': path.resolve(import.meta.dirname, './src'),
      '@content': path.resolve(import.meta.dirname, './content'),
    },
  },
  server: {
    // usePolling: Docker-Bind-Mounts (z.B. via Colima auf dem Mac) geben Datei-Events vom Host
    // oft nicht zuverlässig an den Container weiter — ohne Polling bleibt der Vite-Dev-Server
    // dann auf altem Stand, bis eine Datei von innerhalb des Containers angefasst wird.
    watch: {
      usePolling: true,
      interval: 300,
    },
    proxy: {
      '/api': {
        target: process.env.VITE_API_PROXY || 'http://127.0.0.1:3001',
        changeOrigin: true,
      },
    },
  },
})
