import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    tailwindcss(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  build: {
    outDir: '../staticfiles/dist',
    assetsDir: 'assets',   // 🔹 Ensures assets are inside static/dist/assets/
    manifest: true,        // 🔹 Generates manifest.json for Django integration
    emptyOutDir: true,     // 🔹 Clears old files before building
  }
})
