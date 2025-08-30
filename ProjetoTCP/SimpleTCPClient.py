from socket import *
from utils import cifra_cesar, decifra_cesar, gerar_chave

serverName = "localhost"  # IP do servidor
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# === Receber p e g do servidor ===
p, g = map(int, clientSocket.recv(1024).decode().split(","))

# === Troca de chave (Diffie-Hellman) ===
chave = gerar_chave(clientSocket, servidor=False, p=p, g=g) % 26
print("Chave secreta compartilhada:", chave)

# === Enviar mensagem cifrada ===
sentence = input("Digite a mensagem para o servidor: ")
msg_cifrada = cifra_cesar(sentence, chave)
clientSocket.send(msg_cifrada.encode())

# === Receber resposta cifrada ===
modifiedSentence = clientSocket.recv(1024).decode()
resposta_decifrada = decifra_cesar(modifiedSentence, chave)

print("Resposta do servidor (decifrada):", resposta_decifrada)
clientSocket.close()