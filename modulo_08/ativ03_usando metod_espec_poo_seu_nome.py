# Atividade 3: Uso de métodos especiais __init__ e __str__

class Pessoa:
    """
    Classe Pessoa: Demonstra o uso de __init__ e __str__.
    """
    
    # O __init__ (já visto) é o construtor, chamado para criar o objeto.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    # Método Especial: __str__
    # Define como o objeto deve ser representado como string (leitura amigável).
    # O que este método retorna é o que será exibido por print().
    def __str__(self):
        return f"Pessoa(Nome='{self.nome}', Idade={self.idade})"

    # O método __repr__ é similar, mas focado na representação oficial (debug).
    # Geralmente, é implementado para que a saída possa recriar o objeto.
    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"

# --- Demonstração da Classe Pessoa ---

pessoa1 = Pessoa("Alice", 30)

print("\n--- Representação de Objeto ---")

# 1. Uso do __str__ implícito: O print chama o método __str__
print(f"Resultado de print(pessoa1): {pessoa1}") 

# 2. Uso do __repr__ (normalmente usado em listas ou ambientes de debug)
print(f"Resultado em formato de lista: {[pessoa1]}")