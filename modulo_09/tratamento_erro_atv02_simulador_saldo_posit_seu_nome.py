# ==============================================================================
# ATIVIDADE 2: Exceção Personalizada SaldoInsuficienteError
# ==============================================================================

# 1. DEFINIÇÃO DA EXCEÇÃO PERSONALIZADA
# Criamos uma nova classe que herda de 'Exception' para criar uma exceção específica.
class SaldoInsuficienteError(Exception):
    """
    Exceção levantada quando um saque tenta ultrapassar o saldo atual.
    """
    # O método __init__ é usado para inicializar a exceção com uma mensagem personalizada.
    def __init__(self, saldo_atual, valor_saque):
        # Chama o construtor da classe base (Exception) com a mensagem de erro.
        super().__init__(f"Tentativa de saque de R$ {valor_saque:.2f} falhou. Saldo atual: R$ {saldo_atual:.2f}")
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque

# 2. CLASSE PARA SIMULAR A CONTA BANCÁRIA
class ContaBancaria:
    """
    Simula uma conta bancária simples com funções de consulta e saque.
    """
    def __init__(self, saldo_inicial=0.0):
        # Inicializa a conta com um saldo
        self.saldo = saldo_inicial
        print(f"Conta criada. Saldo inicial: R$ {self.saldo:.2f}")

    def consultar_saldo(self):
        """ Retorna o saldo atual da conta. """
        return self.saldo

    def sacar(self, valor):
        """
        Realiza um saque, levantando SaldoInsuficienteError se necessário.
        """
        if valor <= 0:
            # Validação básica de entrada
            raise ValueError("O valor do saque deve ser positivo.")

        if valor > self.saldo:
            # 3. Lança (raise) a exceção personalizada quando o saldo é insuficiente
            raise SaldoInsuficienteError(self.saldo, valor)
        else:
            # Se houver saldo suficiente, o saque é realizado
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            print(f"Novo saldo: R$ {self.saldo:.2f}")

# 4. IMPLEMENTAÇÃO E TESTE
if __name__ == "__main__":
    # Cria uma nova conta com saldo inicial de 500.00
    minha_conta = ContaBancaria(saldo_inicial=500.00)

    print("\n--- TESTE 1: Saque bem-sucedido ---")
    try:
        minha_conta.sacar(200.00) # Saque OK
    except (SaldoInsuficienteError, ValueError) as e:
        # Este bloco só será executado se houver um erro
        print(f"Falha na transação: {e}")

    print("\n--- TESTE 2: Saque com Saldo Insuficiente ---")
    try:
        # Tenta sacar 400.00, mas o saldo é apenas 300.00
        minha_conta.sacar(400.00) 
        
    # 5. Captura ESPECIFICAMENTE a exceção personalizada que foi lançada
    except SaldoInsuficienteError as e:
        # A mensagem de erro da nossa exceção personalizada é exibida
        print(f"\nERRO DE NEGÓCIO: {e}")
        print("A transação não pôde ser concluída.")

    print(f"\nSaldo Final da Conta: R$ {minha_conta.consultar_saldo():.2f}")