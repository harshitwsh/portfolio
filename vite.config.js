import { defineConfig } from 'vite';

export default defineConfig({
  root: 'public',
  publicDir: false,
  server: {
    port: 5173,
    host: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
  },
  build: {
    outDir: '../dist',
    emptyOutDir: true,
  },
  assetsInclude: [
    '**/*.ktx2',
    '**/*.glb',
    '**/*.wasm',
    '**/*.otf',
    '**/*.webp',
    '**/*.mp4',
  ],
});
