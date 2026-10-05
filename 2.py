nome = input("Digite seu nome: ")
ano_atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite seu ano de nascimento: "))

idade_calculada = ano_atual - nascimento

if idade_calculada >= 18:
    print("Olá, ", nome, "! Você tem ", idade_calculada, " anos e é maior de idade.")

else:
    idade_calculada <= 18
    print("Olá, ", nome, "! Você tem ", idade_calculada, " anos e é menor de idade.")