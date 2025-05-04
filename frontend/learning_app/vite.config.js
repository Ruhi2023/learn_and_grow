import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// const path = require('__path__')

// https://vite.dev/config/
export default defineConfig({
  // root: path.resolve(__dirname, 'src'),
  // resolve: {
  //   alias: {
  //     '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
  //   }
  // },
  server: {
    port: 2222,
    hot: true
  },
  plugins: [react()],
})

// const path = require('path')

// export default {
//   root: path.resolve(__dirname, 'src'),
//   server: {
//     port: 8080,
//     hot: true
//   }
// }