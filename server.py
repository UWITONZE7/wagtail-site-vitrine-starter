from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('X-Frame-Options', 'ALLOWALL')
        SimpleHTTPRequestHandler.end_headers(self)

print("Serveur démarré sur http://127.0.0.1:8000")
HTTPServer(('127.0.0.1', 8000), MyHandler).serve_forever()