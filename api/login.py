from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Configurações do seu servidor (Altere os IPs para o seu servidor de jogo real)
GAME_SERVER_IP = "203.117.148.72" # Exemplo: IP do seu servidor de batalha

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode("utf-8"))
        
        print(f"Recebido pedido de login: {data}")

        response_data = {
            "account_type": 1,
            "account_id": "12345678",
            "server_time": 1700000000,
            "chat_addr": f"{GAME_SERVER_IP}:5000",
            "rank_info": {"ranking_points": 1000}
        }
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

if __name__ == '__main__':
    # Para testes locais
    server_address = ("", 8001)
    httpd = HTTPServer(server_address, handler)
    print(f"Servidor rodando em http://localhost:8001")
    httpd.serve_forever()