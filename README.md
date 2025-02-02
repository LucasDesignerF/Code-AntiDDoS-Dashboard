# Dashboard de Monitoramento - Anti-DDoS

Este é um dashboard de monitoramento de tráfego de rede, requisições por segundo, status do sistema e alertas de ataques DDoS. Ele foi desenvolvido para fornecer uma visão clara do comportamento do seu sistema, ajudando a identificar potenciais ataques e monitorar a saúde do servidor.

## Funcionalidades

### Monitoramento do Sistema
- **Uso de CPU**: Exibe a porcentagem de uso da CPU.
- **Uso de RAM**: Exibe a porcentagem de uso da memória RAM.
- **Uso de Disco**: Exibe a porcentagem de uso do disco rígido.
- **Tráfego de Rede**: Mostra o tráfego total em bytes (enviado + recebido).

### Ataques DDoS
- **Ataque HTTP Flood**: O sistema pode simular um ataque de negação de serviço distribuída (DDoS) do tipo HTTP Flood, enviando requisições repetidas a um servidor para sobrecarregá-lo.
  - **Iniciar Ataque**: Inicia o ataque HTTP com parâmetros configuráveis, como o IP de destino, porta, duração, e número de threads.
  - **Parar Ataque**: Permite interromper o ataque em andamento.

### Dashboard de Monitoramento
- **Métricas em Tempo Real**: O dashboard exibe métricas em tempo real, como uso de CPU, RAM, disco, e tráfego de rede.
- **Alertas de Ataques**: Exibe alertas simulados de tentativas de ataque e ações de defesa, como bloqueio de IPs.
- **Gráficos Interativos**: Utiliza gráficos interativos para exibir o tráfego de rede e requisições por segundo ao longo do tempo.

## Tecnologias Utilizadas

- **HTML5 & CSS3**: Estrutura e estilos do frontend.
- **JavaScript**: Interatividade e atualizações em tempo real do dashboard.
- **Chart.js**: Biblioteca de gráficos para exibição de dados em tempo real.
- **Bootstrap 5**: Framework CSS para criar um layout responsivo e amigável.
- **Flask**: Framework Python para a criação da API que fornece os dados do sistema e gerencia o ataque.
- **psutil**: Biblioteca Python para monitoramento de recursos do sistema como CPU, RAM, e disco.
- **socket**: Para a simulação de ataques HTTP Flood.
- **threading**: Para executar ataques em múltiplas threads simultaneamente.

## Rotas da API

### `/start_attack` (POST)
Inicia um ataque do tipo especificado.
- **Parâmetros**:
  - `target_ip`: IP do alvo.
  - `port`: Porta do alvo.
  - `threads`: Número de threads para o ataque.
  - `duration`: Duração do ataque em segundos.
  - `attack_type`: Tipo de ataque (atualmente, apenas `http_flood` está implementado).
- **Resposta**: Mensagem confirmando o início do ataque.

### `/stop_attack` (POST)
Interrompe o ataque em andamento.
- **Resposta**: Mensagem confirmando a interrupção do ataque.

### `/get_system_status` (GET)
Retorna informações sobre o sistema e o ataque em andamento.
- **Resposta**:
  - `cpu_usage`: Percentual de uso da CPU.
  - `ram_usage`: Percentual de uso da RAM.
  - `disk_usage`: Percentual de uso do disco.
  - `network_traffic`: Tráfego de rede total em bytes.
  - `uptime`: Tempo de execução do ataque (se estiver em andamento).
  - `attack_running`: Indica se o ataque está em andamento.
  - `attack_type`: Tipo do ataque (caso esteja em andamento).
  - `target_ip`: IP do alvo do ataque (caso esteja em andamento).
  - `port`: Porta do alvo (caso esteja em andamento).

### `/get_alerts` (GET)
Retorna uma lista simulada de alertas relacionados a ataques DDoS.
- **Resposta**: Lista de alertas, como "Tentativa de DDoS detectada" e "Bloqueio de IP realizado".

## Estrutura do Projeto

```
- app.py          # Código backend da aplicação Flask
- index.html      # Frontend (Dashboard) em HTML
- assets/
  - CSS e imagens relacionadas
- scripts/
  - Scripts JS para o funcionamento do dashboard
- requirements.txt # Dependências do projeto
```

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- Flask
- psutil
- requests
- pyshark
- scapy

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/anti-ddos-dashboard.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd anti-ddos-dashboard
   ```

3. Instale as dependências do backend:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o servidor Flask:
   ```bash
   python app.py
   ```

5. Abra o navegador e acesse:
   ```
   http://localhost:5000
   ```

## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para fazer um fork, criar uma branch, e enviar um pull request.

### Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça as alterações necessárias.
4. Commit as alterações (`git commit -am 'Adicionando nova funcionalidade'`).
5. Envie a branch (`git push origin feature/nova-funcionalidade`).
6. Abra um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- **Bootstrap 5**: Framework CSS.
- **Chart.js**: Biblioteca para gráficos.
- **Flask**: Framework Python.
- **psutil**: Para monitoramento de recursos do sistema.
- **scapy**: Para simulação de ataques de rede.
