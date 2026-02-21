from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler ):
    def do_GET(self):
        # Pega o IP do cliente dos headers do Vercel (se disponível)
        client_ip = self.headers.get('x-forwarded-for', '0.0.0.0').split(',')[0]
        
        response_data = {
            "appstore_url": "https://discord.gg/seu-link",
            "billboard_msg": "Servidor Online! Bem-vindo!",
            "cdn_url": "https://dl.cdn.freefiremobile.com/live/ABHotUpdates/",
            "client_ip": client_ip,
            "code": 0,
            "country_code": "BR",
            "force_to_restart_app": False,
            "gdpr_version": 2,
            "is_firewall_open": False,
            "is_review_server": False,
            "is_server_open": True,
            "maintenance_announcement": "",
            "maintenance_region": "",
            "query_params": {},
            "remote_option_version": "1.0.0",
            "remote_version": "1",
            "server_url": "https://api.luna-corp.online/"
        }

        self.send_response(200 )
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

    # Adicione também o do_POST para garantir que o jogo não trave
    def do_POST(self):
        self.do_GET()

