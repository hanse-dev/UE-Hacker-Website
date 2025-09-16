import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  assetsInclude: ['**/*.ipynb'],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
