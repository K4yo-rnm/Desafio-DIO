# 🤖 Assistente de Investimentos com RPA e IA Generativa

Automação desenvolvida como parte do laboratório da **Digital Innovation One (DIO)**, utilizando **Python, n8n, Ollama e SMTP** para automatizar o processamento de dados de clientes e o envio de informações sobre opções de investimento.

O projeto recebe os dados dos clientes, identifica o perfil de investidor, cruza essas informações com uma base de investimentos e utiliza **IA Generativa** para criar mensagens informativas personalizadas, que são enviadas automaticamente por e-mail.

---

## 🎯 Objetivo

Construir uma automação capaz de:

1. Extrair dados de clientes utilizando Python.
2. Enviar os dados para um Webhook do n8n.
3. Consultar uma base de opções de investimento.
4. Identificar investimentos compatíveis com o perfil de cada cliente.
5. Utilizar IA Generativa para criar uma mensagem personalizada.
6. Enviar a mensagem automaticamente por e-mail.
7. Retornar o resultado da execução através do Webhook.

---

## 🧩 Tecnologias utilizadas

- 🐍 **Python**
- ⚙️ **n8n**
- 🐳 **Docker**
- 🤖 **Ollama**
- 🧠 **Llama 3.2**
- 📧 **SMTP / Gmail**
- 🔗 **Webhook**
- 🌐 **HTTP Request**
- 📊 **CSV**
- ☁️ **Google Colab**
- 🔒 **ngrok**

---

## 🏗️ Arquitetura do projeto

O fluxo principal da automação funciona da seguinte forma:

```text
Python / Google Colab
        │
        │ Dados dos clientes
        ▼
     Webhook
        │
        ├──────────────► HTTP Request
        │                    │
        │                    ▼
        │              Base de investimentos
        │                    │
        └──────────────┬─────┘
                       ▼
                     Merge
                       │
                       ▼
              Processamento dos clientes
                       │
                       ▼
             Cruzamento de informações
                       │
                       ▼
                    Ollama
                  Llama 3.2
                       │
                       ▼
              Geração do e-mail
                       │
                       ▼
                  SMTP / Gmail
                       │
                       ▼
               Cliente recebe e-mail
```

---

## 🔄 Funcionamento

### 1. Extração dos clientes

O Python acessa a página disponibilizada pela DIO e realiza a extração dos dados dos clientes.

São coletadas informações como:

- Nome
- E-mail
- Saldo
- Perfil de investidor

Os dados são enviados para o Webhook do n8n em formato JSON.

Exemplo:

```json
{
  "clientes": [
    {
      "nome": "Ana Silva",
      "email": "ana@email.com",
      "saldo": "R$ 12.500,00",
      "perfil": "Conservador"
    }
  ]
}
```

---

### 2. Consulta da base de investimentos

O n8n realiza uma requisição HTTP para obter a base de investimentos disponibilizada pelo projeto.

A base contém informações como:

- Perfil
- Produto
- Investimento mínimo
- Rentabilidade

Exemplo:

```text
Conservador
Poupança
CDB Liquidez Diária
Tesouro Selic
```

---

### 3. Cruzamento dos dados

O workflow cruza o perfil do cliente com os investimentos disponíveis.

Por exemplo:

```text
Cliente:
Ana Silva

Perfil:
Conservador

Investimentos compatíveis:
- Poupança
- CDB Liquidez Diária
- Tesouro Selic
```

O objetivo é apresentar somente as opções pertencentes ao perfil identificado na base de dados.

---

## 🤖 Geração da mensagem com IA

Após o processamento dos dados, o workflow envia as informações para o **Ollama**, utilizando o modelo:

```text
llama3.2
```

A IA recebe informações como:

- Nome do cliente
- Perfil
- Saldo
- Investimentos compatíveis

E gera um e-mail informativo personalizado.

### Exemplo

```text
Olá, Ana Silva!

Foram encontradas opções compatíveis com o seu perfil:
Poupança, CDB Liquidez Diária e Tesouro Selic.

Estas informações são apenas informativas e não constituem recomendação financeira.
```

---

## 📧 Envio automático

Após a geração da mensagem, o n8n utiliza uma conexão **SMTP** para realizar o envio do e-mail.

Os campos são preenchidos automaticamente:

```text
Destinatário:
{{ $json.email }}

Assunto:
{{ $json.assunto }}

Mensagem:
{{ $json.mensagem }}
```

Dessa forma, cada cliente recebe uma mensagem correspondente aos seus próprios dados.

---

## 🧠 Regras utilizadas pela IA

A geração das mensagens possui algumas restrições:

- Começar com uma saudação ao cliente.
- Informar que foram encontradas opções compatíveis com o perfil.
- Listar somente produtos presentes na base de dados.
- Não afirmar que o cliente já possui determinado investimento.
- Não inventar informações.
- Não prometer rentabilidade.
- Manter a mensagem curta.
- Informar que o conteúdo possui caráter exclusivamente informativo.

---

## 📂 Estrutura do projeto

```text
dio-lab-assistente-investimentos-rpa-n8n/
│
├── docs/
│   ├── index.html
│   └── data.csv
│
├── n8n/
│   └── workflow.json
│
├── src/
│   └── extrair_clientes.ipynb
│
└── README.md
```

### `docs/`

Contém os arquivos utilizados como fonte de dados do projeto.

### `n8n/`

Contém o workflow responsável pela automação.

### `src/`

Contém os códigos relacionados à extração dos dados.

---

## ⚙️ Principais etapas do workflow n8n

O workflow possui os seguintes componentes:

```text
Webhook
   ↓
HTTP Request
   ↓
Code in JavaScript
   ↓
Merge
   ↓
Code in JavaScript1
   ↓
Code in JavaScript2
   ↓
Message a model (Ollama)
   ↓
Code in JavaScript3
   ↓
Send an Email
   ↓
Respond to Webhook
```

### Webhook

Recebe os dados dos clientes enviados pelo Python.

### HTTP Request

Obtém a base de investimentos.

### Code

Realiza o tratamento e organização dos dados.

### Merge

Combina os dados dos clientes com a base de investimentos.

### Ollama

Utiliza IA Generativa para criar o conteúdo do e-mail.

### Send an Email

Realiza o envio automático através de SMTP.

### Respond to Webhook

Retorna uma resposta HTTP indicando o resultado da execução.

---

## 🔐 Segurança

As credenciais utilizadas pelo n8n **não devem ser publicadas no GitHub**.

O arquivo `workflow.json` deve ser revisado antes do envio ao repositório para garantir que não contenha:

- Senhas
- Tokens
- Chaves de API
- Senhas de aplicativo
- Credenciais SMTP

As credenciais devem ser configuradas diretamente no ambiente local do n8n.

---

## 🚀 Como executar

### 1. Executar o n8n

O n8n pode ser executado localmente através do Docker.

Exemplo:

```bash
docker compose up -d
```

Depois, acessar:

```text
http://localhost:5678
```

---

### 2. Executar o Ollama

Certifique-se de que o Ollama esteja instalado e com o modelo disponível:

```bash
ollama pull llama3.2
```

O n8n utilizará o Ollama para gerar as mensagens.

---

### 3. Executar o código Python

O código Python realiza a coleta dos clientes e envia os dados para o Webhook.

O endereço do Webhook deve ser configurado no código:

```python
N8N_WEBHOOK = "SUA_URL_DO_WEBHOOK"
```

Caso o n8n esteja sendo executado localmente, pode ser utilizado um túnel como o ngrok para permitir que o Google Colab acesse o Webhook.

---

### 4. Configurar o SMTP

Configure uma credencial SMTP no n8n.

Para Gmail, por exemplo:

```text
Host: smtp.gmail.com
Porta: 465
SSL/TLS: Ativado
Usuário: seuemail@gmail.com
Senha: Senha de aplicativo
```

A senha de aplicativo deve ser utilizada no lugar da senha normal da conta.

---

## 📌 Exemplo do resultado

Para um cliente com perfil **Conservador**, o sistema pode identificar:

```text
Poupança
CDB Liquidez Diária
Tesouro Selic
```

A IA transforma essas informações em uma mensagem curta e personalizada.

Depois, o n8n envia automaticamente o e-mail para o endereço cadastrado.

---

## ⚠️ Observação importante

Este projeto possui finalidade **educacional e demonstrativa**.

As informações apresentadas pelo sistema não constituem recomendação financeira, consultoria ou indicação de investimento.

Antes de realizar qualquer investimento, devem ser considerados fatores como:

- Objetivos financeiros
- Prazo
- Liquidez
- Risco
- Perfil do investidor
- Condições do produto

---

## 📚 Projeto de referência

Projeto desenvolvido a partir do laboratório:

**Criando um Assistente de Investimentos com RPA e IA Generativa**

da **Digital Innovation One (DIO)**.

---

## 👨‍💻 Autor

**Caio Braga**

Projeto desenvolvido para fins de estudo e demonstração de automação utilizando **RPA, IA Generativa, Python e n8n**.

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.