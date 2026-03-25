# 🤖 Jarvis - Bot de Assistência e Moderação para Discord

## 📌 Sobre o projeto

O **Jarvis** é um bot desenvolvido em Python com foco em automação, moderação e interação com usuários dentro de servidores Discord.

O projeto foi criado com o objetivo de demonstrar conhecimentos em programação, eventos assíncronos e manipulação de dados, utilizando uma estrutura simples e funcional.

---

## 🚀 Funcionalidades

### 🤖 Assistente Inteligente

* Responde a mensagens como **"hey jarvis"**
* Interação natural sem necessidade de comandos

### 👋 Boas-vindas automáticas

* Envia mensagem privada para novos membros ao entrarem no servidor

### 🛡️ Moderação

* `.limpar <quantidade>` → apaga mensagens do chat

### 📋 Sistema de comandos

* `.ola` → saudação simples
* `.ajuda` → lista de comandos disponíveis
* `.conhecer` → informações sobre o desenvolvedor

### 📝 Sistema de cadastro

* `.cadastro` → coleta nome e idade do usuário
* Dados são armazenados em um arquivo JSON (`cadastros.json`)

### 🚫 Anti-spam

* Detecta e remove mensagens com excesso de links

### 🗑️ Logs

* Registra no terminal mensagens apagadas

---

## 🧠 Tecnologias utilizadas

* Python 3
* discord.py
* JSON (armazenamento de dados)

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/cauakssz/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install discord.py
```

### 3. Configure o bot

* Crie um bot no Discord Developer Portal
* Copie o token
* Substitua no código:

```python
bot.run("SEU_TOKEN_AQUI")
```

### 4. Crie o arquivo de dados

Crie um arquivo chamado:

```
cadastros.json
```

Com o conteúdo:

```json
{}
```

### 5. Execute o bot

```bash
python main.py
```

---

## 💡 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos como:

* Programação assíncrona com eventos
* Manipulação de mensagens em tempo real
* Criação de comandos personalizados
* Persistência de dados com JSON
* Organização de lógica para interação com usuários

---

## 📌 Observações

Este projeto tem fins educacionais e pode ser expandido com:

* Banco de dados (SQLite, MongoDB)
* Sistema de permissões mais avançado
* Interface com botões (Discord UI)
* Sistema de logs em canais específicos

---

## ⭐ Contribuição

Sinta-se à vontade para contribuir ou sugerir melhorias!
