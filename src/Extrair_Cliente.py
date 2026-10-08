

# !pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

URL_PAGINA = "https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/"

N8N_WEBHOOK = "https://vastly-appetizer-whimsical.ngrok-free.dev/webhook-test/Cliente"

# 1) Baixar a página
html = requests.get(URL_PAGINA).text

# 2) Ler a tabela de clientes
soup = BeautifulSoup(html, "html.parser")
linhas = soup.select("#clientes tbody tr")

clientes = []

for linha in linhas:
    colunas = linha.find_all("td")

    cliente = {
        "nome": colunas[0].get_text(strip=True),
        "email": colunas[1].get_text(strip=True),
        "saldo": colunas[2].get_text(strip=True),
        "perfil": colunas[3].get_text(strip=True),
    }

    clientes.append(cliente)

# 3) Mostrar o resultado
print("Clientes encontrados:")

for cliente in clientes:
    print(cliente)

# 4) Enviar todos os clientes para o Webhook
response = requests.post(
    N8N_WEBHOOK,
    json={"clientes": clientes}
)

print("Status do envio:", response.status_code)
print("Resposta do n8n:", response.text)