# serveur.py

import http.server
import socketserver
import os

# Définir le port
PORT = 8000
# Définir le chemin vers le répertoire (le répertoire où se trouve ce script)
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("🎉 Serveur Web Python Démarré !")
        print(f"📁 Dossier servi : {os.getcwd()}")
        print(f"🌐 Accédez à l'adresse : http://localhost:{PORT}/index.html")
        print("\n(Appuyez sur Ctrl+C pour arrêter le serveur)")
        
        # Le serveur tourne jusqu'à ce que vous l'arrêtiez (Ctrl+C)
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\n👋 Serveur arrêté.")
except Exception as e:
    print(f"\n❌ Erreur lors du démarrage du serveur: {e}")