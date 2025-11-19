'''
Estrutura 
Lógica de Programação
Exibição na Tela

MVC - Model View Controller
Model - Modelo (Dados) 
View - Visão (Interface)
Controller - Controlador (Lógica)

Verifica a idade de uma pessoa com base no ano 
atual e no ano de nascimento fornecidos pelo usuário.
Solicita ao usuário que insira o ano atual e o ano de nascimento.

'''

# --- 1. Obter o Ano Atual com Validação ---
while True:
    try:
        ano_atual_str = input("Por favor, digite o ANO ATUAL (ex: 2025): ")
        ano_atual = int(ano_atual_str)
        if ano_atual <= 0:
             print("Ano atual inválido. Por favor, digite um ano positivo.")
             continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas um número inteiro.")

# --- 2. Obter o Ano de Nascimento com Validação ---
while True:
    try:
        ano_nascimento_str = input("Agora, digite o seu ANO DE NASCIMENTO (ex: 1990): ")
        ano_nascimento = int(ano_nascimento_str)

        # Validação: ano de nascimento não pode ser no futuro
        if ano_nascimento > ano_atual:
            print(f"O ano de nascimento ({ano_nascimento}) não pode ser maior que o ano atual ({ano_atual}). Tente novamente.")
        else:
            break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas um número inteiro.")

# --- 3. Calcular a Idade ---
idade = ano_atual - ano_nascimento

# --- 4. Exibir o Resultado ---
print(f"\n--- Resultado ---")
print(f"O ano atual que você informou é: {ano_atual}")
print(f"Seu ano de nascimento é: {ano_nascimento}")
print(f"A sua idade (aproximada) é: {idade} anos.")