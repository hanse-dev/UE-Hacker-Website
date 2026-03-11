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
      '@': path.resolve(__dirname, './src'),
      '@content': path.resolve(__dirname, './content'),
    },
  },
})
