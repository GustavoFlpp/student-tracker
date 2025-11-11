import requests
import os
import csv
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()

URL_API = os.getenv("URL_API")
API_KEY = os.getenv("API_KEY")

if not URL_API or not API_KEY:
    print("Erro: variáveis de ambiente não carregadas corretamente.")
    exit(1)

headers = {
    "api-key": API_KEY,
}

print("Buscando dados da API...")

try:
    response = requests.get(URL_API, headers=headers, timeout=15)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Erro de conexão:", e)
    exit(1)

alunos = response.json()

agentes = defaultdict(list)
for aluno in alunos:
    agente = aluno.get("agenteDoSucesso", "Sem agente")
    agentes[agente].append(aluno)

status_possiveis = ["Ativo", "Atencao", "EmRecuperacao", "Suspenso", "Inativo"]

print("\nResumo por agente:\n")
resumo = []

for agente, lista in agentes.items():
    contagem = {status: 0 for status in status_possiveis}
    for aluno in lista:
        status = aluno.get("status", "Desconhecido")
        if status in contagem:
            contagem[status] += 1
        else:
            contagem["Desconhecido"] = contagem.get("Desconhecido", 0) + 1

    total = len(lista)
    print(f"👤 {agente} — Total: {total}")
    for status in status_possiveis:
        print(f"  - {status}: {contagem[status]}")
    print()

    resumo.append({
        "Agente": agente,
        **contagem,
        "Total": total
    })

print("Gerando arquivo CSV consolidado...")

with open("resumo_agentes.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Agente", "Ativo", "Atencao", "EmRecuperacao", "Suspenso", "Inativo", "Total"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(resumo)

print("\n✅ Exportação concluída com sucesso! Arquivo: 'resumo_agentes.csv'")
