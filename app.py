import requests
import os
import csv
from dotenv import load_dotenv

load_dotenv()

URL_API = os.getenv("URL_API")
API_KEY = os.getenv("API_KEY")
AGENTE_EMAIL = os.getenv("AGENTE_EMAIL")

if not URL_API or not API_KEY or not AGENTE_EMAIL:
    print("Erro: variáveis de ambiente não carregadas corretamente.")
    exit(1)

headers = {
    "api-key": API_KEY,
}

print("Buscando dados da API...")

try:
    response = requests.get(URL_API, headers=headers, timeout=15)
except requests.exceptions.RequestException as e:
    print("Erro de conexão:", e)
    exit(1)

if response.status_code == 200:
    alunos = response.json()

    meus_alunos = [
        aluno for aluno in alunos
        if aluno.get("agenteDoSucesso") == AGENTE_EMAIL
        and aluno.get("status") != "Inativo"
    ]

    print(f"\nTotal de alunos ativos vinculados: {len(meus_alunos)}\n")

    print("Lista completa de alunos:")
    for aluno in meus_alunos:
        print(f"- {aluno.get('nomeCompleto')} | {aluno.get('registrationCode')} | Status: {aluno.get('status')}")

    em_alerta = [
        aluno for aluno in meus_alunos
        if aluno.get("status") in ["Atencao", "EmRecuperacao"]
    ]

    print("\nAlunos em atenção ou recuperação:")
    for aluno in em_alerta:
        print(f"- {aluno.get('nomeCompleto')} | {aluno.get('registrationCode')} | Status: {aluno.get('status')}")
    print(f"\nTotal em alerta: {len(em_alerta)}")

    print("\nGerando arquivos CSV...")

    with open("alunos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nome Completo", "Código de Matrícula", "Status"])
        for aluno in meus_alunos:
            writer.writerow([aluno.get("nomeCompleto"), aluno.get("registrationCode"), aluno.get("status")])

    with open("alunos_em_alerta.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nome Completo", "Código de Matrícula", "Status"])
        for aluno in em_alerta:
            writer.writerow([aluno.get("nomeCompleto"), aluno.get("registrationCode"), aluno.get("status")])

    print("Exportação concluída: arquivos 'alunos.csv' e 'alunos_em_alerta.csv' gerados com sucesso!")

else:
    print(f"Erro ao buscar dados: {response.status_code}")
    print("Detalhes:", response.text[:500])
