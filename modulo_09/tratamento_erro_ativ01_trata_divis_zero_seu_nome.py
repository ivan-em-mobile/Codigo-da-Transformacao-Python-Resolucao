# ==============================================================================
# ATIVIDADE 1: Calculadora com tratamento de erro de Divisão por Zero
# ==============================================================================

def calculadora():
    """
    Função principal que simula uma calculadora e trata erros de divisão por zero.
    """
    print("--- Calculadora Simples ---")
    
    # 1. Usar um bloco try-except para lidar com erros de entrada de dados
    try:
        # Pede ao utilizador para inserir os dois números
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        
        # Pede ao utilizador para inserir a operação desejada
        operacao = input("Escolha a operação (+, -, *, /): ")
        
        resultado = None # Inicializa a variável resultado
        
        # 2. Verifica qual operação foi escolhida e executa o cálculo
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
            
        # 3. Bloco try-except específico para a divisão
        elif operacao == '/':
            try:
                # Tenta realizar a divisão
                resultado = num1 / num2
                
            # Captura ESPECIFICAMENTE o erro de divisão por zero
            except ZeroDivisionError:
                # Retorna uma mensagem de erro em vez de falhar o programa
                print("\nERRO: Não é possível dividir por zero!")
                return # Sai da função para evitar a impressão do resultado
        
        else:
            # Caso o utilizador insira uma operação inválida
            print("\nERRO: Operação inválida. Use apenas +, -, *, ou /.")
            return

        # 4. Imprime o resultado se o cálculo for bem-sucedido
        if resultado is not None:
            print(f"\nResultado da operação: {num1} {operacao} {num2} = {resultado}")

    # Captura outros erros, como se o utilizador inserir texto em vez de um número
    except ValueError:
        print("\nERRO: Entrada inválida. Certifique-se de inserir apenas números.")
    
    # Bloco opcional que é executado se NÃO houver exceções
    else:
        print("Operação concluída com sucesso.")

# Chama a função para iniciar a calculadora
if __name__ == "__main__":
    calculadora()