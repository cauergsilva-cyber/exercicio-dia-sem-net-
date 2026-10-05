soma_pares = 0
quantidade_pares = 0

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))

    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

if quantidade_pares == 0:
    print("Não há números pares para calcular a média.")
else:
    media = soma_pares / quantidade_pares
    print(f"A média dos números pares digitados é: {media}")
