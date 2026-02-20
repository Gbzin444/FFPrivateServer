from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Dados da resposta exatamente como você quer
        response_data = {
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
            "maintenance_region": "",
            "query_params": {},
            "remote_option_version": "1.0.0",
            "remote_version": "1",
            "server_url": "https://api.luna-corp.online/"
        }

        # Configuração do cabeçalho de resposta da api
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        # Importante para evitar erros de CORS se o jogo chamar via web
        self.send_header("Access-Control-Allow-Origin", "*") 
        self.end_headers()
        
        # Converte o dicionário para JSON e envia
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

