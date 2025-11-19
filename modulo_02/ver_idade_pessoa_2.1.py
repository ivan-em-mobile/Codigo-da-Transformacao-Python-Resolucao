'''
Primicias
Verifica se a pessoa é maior de idade com base na data de nascimento fornecida.
Usar biblioteca de data para manipulação de datas.


'''

from datetime import date, datetime
## Importa a biblioteca datetime para manipulação de datas

# Pede a data de nascimento no formato DD/MM/AAAA
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")



# Converte a string em um objeto datetime
nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
## Converte a string de data para um objeto date

# Pega a data atual
hoje = date.today()

# Calcula a idade
idade = hoje.year - nascimento.year

# Ajusta caso a pessoa ainda não tenha feito aniversário este ano
if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
    idade -= 1

# Mostra a idade e se é maior de idade
print(f"Você tem {idade} anos.")

if idade >= 18:
    print("Você é maior de idade! ✅")
else:
    print("Você é menor de idade. 🚸")
