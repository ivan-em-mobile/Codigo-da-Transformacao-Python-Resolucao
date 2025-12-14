# Atividade 2: Implemente herança com CarroEletrico
from ativ01_crie_carro_poo_seunome import Carro # Para fins práticos, assumimos que Carro está definido/importado

class CarroEletrico(Carro):
    """
    Classe CarroEletrico: Herda de Carro e adiciona um atributo específico.
    """
    
    # O método __init__ da subclasse precisa chamar o __init__ da classe pai (super).
    def __init__(self, marca, modelo, autonomia_bateria):
        # 1. Chamada ao construtor da classe pai (Carro) para inicializar marca e modelo.
        super().__init__(marca, modelo) 
        
        # 2. Adição de um novo atributo exclusivo para CarroEletrico.
        self.autonomia_bateria = autonomia_bateria 
        self.carga_bateria = 100 # Atributo padrão: começa com 100% de carga.

    # Sobrescrita de Método (Method Overriding):
    # Reimplementamos o método exibir_info() para incluir o novo atributo.
    def exibir_info(self):
        # Chamada ao método exibir_info da classe pai para mostrar marca e modelo.
        super().exibir_info() 
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")
        print(f"Carga Atual: {self.carga_bateria}%")

# --- Demonstração da Classe CarroEletrico ---

carro_eletrico = CarroEletrico("Tesla", "Model S", 500)

print("\n--- Informações do Carro Elétrico ---")
# O objeto carro_eletrico possui o método exibir_info sobrescrito e os atributos do pai.
carro_eletrico.exibir_info()

# O objeto carro_eletrico também herda o método 'ligar' da classe Carro.
carro_eletrico.ligar()