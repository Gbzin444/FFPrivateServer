from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler ):
    def get_response_data(self):
        # Centralizei os dados para não precisar repetir no GET e no POST
        return {
            "appstore_url": "https://discord.gg/freefirebeta",
            "billboard_msg": "Projeto Encerrado! | Project Closed! | Proyecto Cerrado! ...", 
            "cdn_url": "https://dl.cdn.freefiremobile.com/live/ABHotUpdates/", 
            "client_ip": "109.215.144.208",
            "code": 0,
            "country_code": "FR", 
            "force_to_restart_app": "false", 
            "gdpr_version": 2,
            "is_firewall_open": "false",
            "is_review_server": "false", 
            "is_server_open": "true", 
            "maintenance_announcement": "", 
            "maintenance_region": "FR",
            "query_params": {},
            "remote_option_version": "1.0.0", 
            "remote_version": "1",
            "server_url": "https://api.luna-corp.online/"
        }

    def send_json_response(self, data ):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        # Responde a requisições GET (como o ver.php inicial)
        self.send_json_response(self.get_response_data())

    def do_POST(self):
        # Responde a requisições POST (essencial para o Free Fire)
        # Opcional: Você pode ler o que o jogo enviou no POST com o código abaixo:
        # content_length = int(self.headers['Content-Length'])
        # post_data = self.rfile.read(content_length)
        # print(f"Dados recebidos do jogo: {post_data}")

        self.send_json_response(self.get_response_data())

    def do_OPTIONS(self):
        # Necessário para navegadores e alguns emuladores que testam a conexão antes
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
