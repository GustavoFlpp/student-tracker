# 🎯 Student Tracker — Automação de Acompanhamento de Alunos

Um script em **Python** desenvolvido para facilitar o acompanhamento de alunos vinculados a um agente de sucesso, consultando uma API interna e gerando **relatórios automáticos em CSV**.

O projeto serve como base para automações de monitoramento, análise de engajamento e futuras integrações com dashboards e alertas inteligentes.

---

## 🚀 Funcionalidades

- Consulta dados de alunos via API autenticada  
- Filtra automaticamente:
  - Alunos **ativos** vinculados a um agente específico  
  - Alunos em **atenção** ou **recuperação**  
- Gera relatórios em **CSV**:
  - `alunos.csv` → todos os alunos ativos  
  - `alunos_em_alerta.csv` → alunos que exigem acompanhamento mais próximo  
- Estrutura pensada para expansão futura (planilhas, e-mails automáticos, dashboards etc.)

---

## 🧠 Tecnologias Utilizadas

- **Python 3.10+**
- **Requests** → integração com API  
- **dotenv** → variáveis de ambiente seguras  
- **CSV (nativo)** → exportação de relatórios  

---

## ⚙️ Configuração

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seuusuario/student-tracker.git
cd student-tracker
```

### 2️⃣ Crie o arquivo .env com as variáveis

```bash
URL_API= # URL da API interna
API_KEY= # Chave de autenticação fornecida
AGENTE_EMAIL= # E-mail do agente de sucesso
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o script

```bash
python main.py
```
---

## 🖥️ Exemplo de Saída no Terminal

```bash
Buscando dados da API...

Total de alunos ativos vinculados: 12

Lista completa de alunos:
- Ana Paula Oliveira | PDITA123 | Status: Atencao
- Bruno Henrique Santos | PDITA456 | Status: Ativo
- Carla Menezes Rocha | PDITA789 | Status: EmRecuperacao
...

Alunos em atenção ou recuperação:
- Ana Paula Oliveira | PDITA123 | Status: Atencao
- Carla Menezes Rocha | PDITA789 | Status: EmRecuperacao

Total em alerta: 2
```
## 📂 Arquivos gerados automaticamente:

- alunos.csv

- alunos_em_alerta.csv

## 🔄 Próximos Passos

- 🔔 Envio automático dos relatórios por e-mail

- 📈 Integração com Google Sheets e dashboards dinâmicos

- 🧭 Análises preditivas de risco de evasão

- 💬 Notificações automáticas para alunos em atenção

- ☁️ Execução agendada em servidor (automação contínua)

## 🧑‍💻 Autor

Desenvolvido por **Gustavo Felippe Barbosa** 💡  
📬 Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/gustavofelippebarbosa/)