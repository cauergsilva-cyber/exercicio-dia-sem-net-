maior_idade = -1
nome_mais_velho = ""

for i in range(1, 6):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))

    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

print(f"A pessoa mais velha é: {nome_mais_velho}")
print(f"Idade: {maior_idade} anos")
