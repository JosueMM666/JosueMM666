from pyngrok import ngrok
import http.server
import socketserver
import threading

# Configura tu authtoken (solo la primera vez)
ngrok.set_auth_token("3IQQqNp8qYxcvlKWEc6hap5iG4r_458KZpnptzyeXBTH2gvKr")

# Puerto donde servirá tu página
PORT = 8000

# Inicia el servidor HTTP en un hilo
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Servidor local corriendo en http://localhost:8000")

# Abre el túnel público
public_url = ngrok.connect(PORT)
print(f"URL pública: {public_url}")

# Mantener el servidor activo
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nCerrando...")
    ngrok.kill()
    httpd.shutdown()