# 🔐 Projeto TCP com Cifra de César e Diffie-Hellman

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-green)

---

## 📌 Descrição do Projeto

Este projeto implementa um sistema **cliente-servidor TCP em Python** com comunicação segura:

- 🔒 Mensagens cifradas usando **Cifra de César**  
- 🔑 Chave secreta compartilhada via **Diffie-Hellman**  
- 📊 Teste de números primos (`primo.py`) para gerar o número primo público `p`  

---

## 📂 Estrutura de Arquivos

| Arquivo               | Descrição                                           |
|-----------------------|----------------------------------------------------|
| `SimpleTCPServer.py`  | Servidor TCP                                       |
| `SimpleTCPClient.py`  | Cliente TCP                                        |
| `utils.py`            | Funções utilitárias (César e Diffie-Hellman)       |
| `primo.py`            | Teste de números primos (Slow e Fast)              |
| `README.md`           | Este arquivo                                       |

---

## ⚙️ Requisitos

- 🐍 Python **3.x**  
- 💻 Compatível com Windows, Linux e macOS  
- 📦 Nenhuma biblioteca externa necessária  

---

## ▶️ Como Executar

### 1️⃣ Rodar o Servidor

python SimpleTCPServer.py

TCP Server rodando...
Conexão de: ('127.0.0.1', <porta>)
Número primo escolhido para p: <p>
Base pública g: <g>
Chave secreta compartilhada: <chave>

### 2️⃣ Rodar o Cliente

python SimpleTCPClient.py

#### Exemplo de entrada:

Input lowercase sentence: teste de comunicação

#### Saída esperada:

Número primo escolhido para p: <p>
Base pública g: <g>
Chave secreta compartilhada: <chave>
Recebido do servidor (decifrado): TESTE DE COMUNICAÇÃO

# ⚡ Funcionamento Interno
### 🔢 1. Escolha de Primo e Base Pública
p: número primo gerado automaticamente (primo_fast)

g: base pública (geralmente 5)

### 🔑 2. Troca de Chave Diffie-Hellman
Cliente e servidor geram números secretos aleatórios

Trocam valores públicos

Calculam a mesma chave secreta compartilhada

### 🔒 3. Cifra de César
Cliente cifra a mensagem com a chave secreta

Servidor decifra, converte para maiúsculas e envia de volta cifrada

Cliente decifra a resposta e exibe a mensagem final

## 📡 Teste no Wireshark
Inicie a captura na interface usada (localhost ou rede local)

Filtre pacotes TCP da porta 1300:

tcp.port == 1300

Clique em um pacote → Follow → TCP Stream

Observe as mensagens cifradas

Compare com o terminal do servidor (mensagem decifrada)


# 🔍 Módulo primo.py
primo_slow(N): verifica todos os divisores

primo_fast(N): verifica até a raiz quadrada de N

Ambos usados para gerar p no Diffie-Hellman

⚙️ Configurações Possíveis
🔧 Alterar intervalo de primos:

p = escolher_primo(1000, 5000)

g = 5


### 🔧 Alterar função de cifragem:
Implemente outro algoritmo próprio, mantendo Diffie-Hellman para troca de chave.

💡 Observações
Funciona em uma máquina (localhost) ou em duas na mesma rede

Todas as mensagens são cifradas e seguras

Ideal para demonstrações com terminal e Wireshark

### 🧪 Demonstração
Inicie captura no Wireshark

Rode o servidor SimpleTCPServer.py

Rode o cliente SimpleTCPClient.py

Envie uma mensagem

# Mostre:

##### 📡 Mensagem cifrada no Wireshark

##### 🔓 Mensagem decifrada no terminal do servidor

##### 🔁 Mensagem processada (maiúsculas) de volta para o cliente