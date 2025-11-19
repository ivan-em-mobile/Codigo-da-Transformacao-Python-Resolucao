from datetime import date

# Obtém a data atual
hoje = date.today()
##constante hoje recebe a função date.today() 
# que retorna a data atual do sistema

# Acessa o dia, mês e ano
ano_atual = hoje.year
## constante ano_atual recebe o atributo year do objeto hoje

nome = input('Qual seu nome? ')
idade = int(input("Qual sua idade? "))


print(f'Olá {nome}, Você tem {idade} anos de idade ')

# se (if) variavel idade_pessoa FOR (=> igual ou maior) que 18,
# a condição é ativada se nao (else) manda outra mensagem
if idade >= 18:
    print("Aparentemente você é maior de idade 😎 ta safe")
else:
    print("Aparentemente você é menor de idade 😅 ")


date.today
nascimento = (ano_atual - idade)
print(f'Você nasceu no ano de {nascimento} ')