# ==============================================================================
# ATIVIDADE 3: Validação de Entradas de Usuário (Idade Positiva)
# ==============================================================================

def solicitar_idade_valida():
    """
    Pede ao utilizador para inserir a idade e valida se é um número inteiro e positivo.
    """
    idade = 0
    
    # Loop para continuar a pedir a entrada até que seja válida
    while True:
        try:
            # 1. Pede a entrada e tenta convertê-la para um número inteiro
            entrada = input("Por favor, insira a sua idade: ")
            idade = int(entrada)
            
            # 2. Validação Lógica (se o valor está nos critérios esperados)
            if idade <= 0:
                # Se a idade for zero ou negativa, lança (raise) um erro de VALOR.
                # Não é um erro de sintaxe, mas sim um erro de lógica de negócio.
                raise ValueError("A idade deve ser um número positivo (maior que zero).")
            
            # Se o código chegar aqui, a entrada é válida
            break
            
        # 3. Captura o erro se a conversão para int falhar (ex: utilizador inseriu "vinte")
        except ValueError as e:
            # Imprime a mensagem de erro específica, seja ela do Python ou a que definimos acima.
            print(f"\nERRO de Validação: {e}. Por favor, tente novamente.")
            
    # Se o loop for quebrado, a idade é válida
    print(f"\nIdade validada com sucesso! Você tem {idade} anos.")
    return idade

# Chama a função para iniciar a validação
if __name__ == "__main__":
    solicitar_idade_valida()