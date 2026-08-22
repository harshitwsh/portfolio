import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5173
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIRECTORY = os.path.join(BASE_DIR, 'public')

class StaticHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.wasm'):
            return 'application/wasm'
        if path.endswith('.glb'):
            return 'model/gltf-binary'
        if path.endswith('.ktx2'):
            return 'image/ktx2'
        if path.endswith('.otf'):
            return 'font/otf'
        if path.endswith('.webp'):
            return 'image/webp'
        if path.endswith('.mp4'):
            return 'video/mp4'
        if path.endswith('.mp3'):
            return 'audio/mpeg'
        if path.endswith('.svg'):
            return 'image/svg+xml'
        return super().guess_type(path)

print(f"Serving Portfolio from {DIRECTORY} on http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), StaticHandler) as httpd:
    httpd.serve_forever()
