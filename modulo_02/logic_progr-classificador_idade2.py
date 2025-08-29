# A função input() obtém a idade do usuário como texto.
# A função int() converte o texto para um número inteiro.
idade = int(input("Digite a sua idade: "))

# Verifica a idade e exibe a categoria correspondente.
if idade < 13:
    print("Você é uma Criança.")
elif idade < 18:
    print("Você é um Adolescente.")
elif idade < 60:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")