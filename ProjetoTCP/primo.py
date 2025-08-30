import time

# -------------------------------
# Primo Slow (verifica todos os divisores)
# -------------------------------
def primo_slow(N: int) -> bool:
    cont = 0
    i = 2
    while i < N:
        if N % i == 0:
            cont += 1
        i += 1
    return cont == 0


# -------------------------------
# Primo Fast (para números grandes)
# -------------------------------
def primo_fast(N: int) -> bool:
    i = 2
    while i * i <= N:  # só precisa testar até a raiz de N
        if N % i == 0:
            return False
        i += 1
    return True


# -------------------------------
# Execução de testes
# -------------------------------
if __name__ == "__main__":
    N = int(input("Digite um número para testar se é primo: "))

    # Teste Slow
    start_time = time.time()
    if primo_slow(N):
        print(f"[SLOW] {N} é primo!")
    else:
        print(f"[SLOW] {N} não é primo!")
    print(f"Tempo execução SLOW: {time.time() - start_time:.6f} segundos\n")

    # Teste Fast
    start_time = time.time()
    if primo_fast(N):
        print(f"[FAST] {N} é primo!")
    else:
        print(f"[FAST] {N} não é primo!")
    print(f"Tempo execução FAST: {time.time() - start_time:.6f} segundos")