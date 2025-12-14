# Atividade 1: Crie uma classe Carro
class Carro:
    """
    Classe Carro: Representa um veículo com marca e modelo.
    """
    
    # 3. Método Especial: __init__ (Inicializador/Construtor)
    # Este método é chamado automaticamente ao criar uma nova instância (objeto) da classe.
    # Ele inicializa os atributos específicos de cada objeto.
    def __init__(self, marca, modelo):
        # Atributos (Dados) do Carro:
        self.marca = marca   # Atributo que armazena a marca do veículo.
        self.modelo = modelo # Atributo que armazena o modelo do veículo.
        self.ligado = False  # Atributo padrão, todo carro começa desligado.

    # Método para exibir as informações do carro
    def exibir_info(self):
        print(f"\n--- Detalhes do Carro ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Status: {estado}")
    
    # Método para ligar o carro (Exemplo de uma ação/comportamento)
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} ligado. Pronto para usar!")
        else:
            print(f"{self.modelo} já está ligado.")

# --- Demonstração da Classe Carro ---

# Criação de um objeto (Instância) da classe Carro
carro_a = Carro("Ford", "Mustang")
carro_b = Carro("Chevrolet", "Camaro")

# Chamada dos métodos nos objetos
carro_a.exibir_info()
carro_a.ligar()

carro_b.exibir_info()