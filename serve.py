"""
Asteria Control - Servidor Local de Demostración
Ejecuta un servidor web local en el puerto 8080 y abre automáticamente el prototipo en el navegador.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Log simplificado y limpio
        sys.stderr.write(f"[Asteria Control Server] {self.address_string()} - {format%args}\n")

def run():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 70)
        print(" Asteria Control — Prototipo B2B de Alta Fidelidad")
        print(f" Servidor iniciado en: {url}")
        print(" Presione Ctrl+C para detener el servidor")
        print("=" * 70)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")

if __name__ == "__main__":
    run()
