# ==============================================================================
# DESAFIO EXTRA: Sistema de Login com Tratamento de Erro e Múltiplas Tentativas
# ==============================================================================

# 1. Definir o número máximo de tentativas
MAX_TENTATIVAS = 3

# 2. Credenciais corretas (simulação de um banco de dados)
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"

# 3. Exceção Personalizada para Credenciais Inválidas
class LoginInvalidoError(Exception):
    """ Exceção levantada quando o nome de utilizador ou palavra-passe estão incorretos. """
    pass # Não precisamos de um __init__ complexo para este desafio

def verificar_credenciais(usuario, senha):
    """
    Verifica se o nome de utilizador e a palavra-passe correspondem aos valores corretos.
    Lança LoginInvalidoError se as credenciais forem incorretas.
    """
    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        return True
    else:
        # Lança a exceção personalizada
        raise LoginInvalidoError("Nome de utilizador ou palavra-passe incorretos.")

def sistema_login():
    """
    Implementa o fluxo de login com limite de tentativas.
    """
    print("--- Sistema de Login ---")
    
    # 4. Loop for para limitar o número de tentativas
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        print(f"\nTentativa {tentativa} de {MAX_TENTATIVAS}:")
        
        try:
            # Pede a entrada do utilizador
            usuario_input = input("Nome de utilizador: ")
            senha_input = input("Palavra-passe: ")
            
            # Tenta verificar as credenciais
            if verificar_credenciais(usuario_input, senha_input):
                print("\n✅ LOGIN BEM-SUCEDIDO! Bem-vindo(a)!")
                return # Sai da função se o login for bem-sucedido
                
        # 5. Captura o erro de login, quebra o fluxo e continua o loop
        except LoginInvalidoError as e:
            print(f"❌ ERRO: {e}")
            # Se for a última tentativa, informa que a conta está bloqueada
            if tentativa == MAX_TENTATIVAS:
                print("\n⛔️ Número máximo de tentativas atingido. Acesso bloqueado.")
                return # Sai da função após o bloqueio

# Executa o sistema de login
if __name__ == "__main__":
    sistema_login()