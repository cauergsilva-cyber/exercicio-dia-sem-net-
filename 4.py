pares = 0
impares = 0
soma_pares = 0
soma_impares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1
        soma_impares += numero

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
