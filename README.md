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

# ▶️ Como Executar

A seguir, o passo a passo para iniciar o servidor e o cliente, realizar a troca de chaves e visualizar a comunicação cifrada.

---

## 🖥️ 1. Iniciar o Servidor

Execute o seguinte comando no terminal:

python SimpleTCPServer.py

### saída será semelhante a esta:

TCP Server rodando...
Conexão de: ('127.0.0.1', 52751)
Parâmetros usados -> p=4057, g=5
Chave secreta compartilhada: 6
Recebido do Client (decifrado): Ola Mundo!
Enviado de volta (cifrado): URG SATJU!

## 💬 2. Iniciar o Cliente
Em outro terminal, execute:

python SimpleTCPClient.py

### Você será solicitado a inserir uma frase em letras minúsculas. Exemplo:

Input lowercase sentence: Ola Mundo!

Parâmetros usados -> p=4057, g=5
Chave secreta compartilhada: 6
Digite a mensagem para o servidor: Ola Mundo!
Resposta do servidor (decifrada): OLA MUNDO!

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


# 🔍 Módulo `primo.py`

Este módulo é responsável por testar se um número é primo, essencial para gerar o valor público `p` utilizado no protocolo Diffie-Hellman.

### 🧪 Como usar

Para realizar o teste de primalidade:

## python primo.py

Depois de executar, você poderá inserir um número e verificar se ele é primo usando dois métodos:

primo_slow(N) → Verifica todos os divisores possíveis (método mais lento)

primo_fast(N) → Verifica até a raiz quadrada de N (método otimizado)

Ambos são utilizados internamente para garantir que o número p seja realmente primo antes de iniciar a troca de chaves.


# 🧪 Demonstração com Wireshark
Para visualizar a comunicação cifrada e decifrada em tempo real:

Inicie a captura no Wireshark (interface localhost ou rede local)

### Rode o servidor:

python SimpleTCPServer.py

### Rode o cliente:

python SimpleTCPClient.py

## Envie uma mensagem pelo cliente

Observe os seguintes pontos:

📡 Mensagem cifrada visível no Wireshark (via filtro tcp.port == 1300)

🔓 Mensagem decifrada exibida no terminal do servidor

🔁 Mensagem processada (convertida para maiúsculas) retornada ao cliente