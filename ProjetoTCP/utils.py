import random

# ===== Cifra de César =====
def cifra_cesar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + chave) % 26 + base)
        else:
            resultado += char
    return resultado

def decifra_cesar(texto, chave):
    return cifra_cesar(texto, -chave)


# ===== Teste de primo (fast) =====
def primo_fast(N: int) -> bool:
    i = 2
    while i * i <= N:  # só precisa testar até a raiz de N
        if N % i == 0:
            return False
        i += 1
    return True


# ===== Diffie-Hellman =====
def escolher_primo(min_val=1000, max_val=5000):
    """Escolhe um primo aleatório no intervalo"""
    while True:
        p = random.randint(min_val, max_val)
        if primo_fast(p):
            return p

def gerar_chave(socket, servidor=False, p=None, g=None):
    """Troca de chaves Diffie-Hellman"""
    segredo = random.randint(1, p-1)
    pub = pow(g, segredo, p)

    print(f"Parâmetros usados -> p={p}, g={g}")

    if servidor:
        pub_cliente = int(socket.recv(1024).decode())
        socket.send(str(pub).encode())
        chave = pow(pub_cliente, segredo, p)
    else:
        socket.send(str(pub).encode())
        pub_servidor = int(socket.recv(1024).decode())
        chave = pow(pub_servidor, segredo, p)

    return chave