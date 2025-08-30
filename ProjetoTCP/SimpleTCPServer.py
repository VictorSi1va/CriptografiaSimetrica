from socket import *
from utils import cifra_cesar, decifra_cesar, gerar_chave, escolher_primo

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("TCP Server rodando...\n")

connectionSocket, addr = serverSocket.accept()
print("Conexão de:", addr)

# === Servidor escolhe p e g e envia ao cliente ===
p = escolher_primo(1000, 5000)
g = 5
connectionSocket.send(f"{p},{g}".encode())

# === Troca de chave (Diffie-Hellman) ===
chave = gerar_chave(connectionSocket, servidor=True, p=p, g=g) % 26
print("Chave secreta compartilhada:", chave)

# === Receber mensagem cifrada ===
sentence = connectionSocket.recv(65000)
received = str(sentence, "utf-8")
msg_decifrada = decifra_cesar(received, chave)

print("Recebido do Client (decifrado):", msg_decifrada)

# === Processamento (colocar em maiúsculas) ===
capitalizedSentence = msg_decifrada.upper()

# === Cifrar antes de enviar ===
resposta_cifrada = cifra_cesar(capitalizedSentence, chave)
connectionSocket.send(resposta_cifrada.encode())

print("Enviado de volta (cifrado):", resposta_cifrada)
connectionSocket.close()