from socket import*
import time

# Pegar o tempo inicial
tempo_inicial = time.time()

alvo = input("Infore o IP para ser escaneado: ")

ip_alvo = gethostbyname(alvo)

print("Comecando scan: ", ip_alvo)

for i in range(50, 500):
    # IPV4
    # TCP
    s = socket(AF_INET, SOCK_STREAM)

# TENTO CONECTAR NA PORTA
    conexao = s.connect_ex((ip_alvo, i))

    if conexao == 0:
        print("Porta: ", i, "aberta!")

    s.close()


print("Tempo que levou: ", time.time() - tempo_inicial)
