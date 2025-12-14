# Desafio Extra: Sistema de Biblioteca com Livro e Biblioteca

class Livro:
    """
    Classe Livro: Representa um item na biblioteca.
    Usa __init__ e __str__ (Atividade 3).
    """
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.emprestado = False # Atributo de estado para rastrear empréstimos.

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - Status: {status}"

class Biblioteca:
    """
    Classe Biblioteca: Gerencia a coleção de livros e os empréstimos.
    """
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = {} # Dicionário: ISBN como chave, objeto Livro como valor.
        self.emprestimos = [] # Lista de ISBNs emprestados.

    def adicionar_livro(self, livro):
        """Adiciona um objeto Livro ao catálogo."""
        if livro.isbn not in self.catalogo:
            self.catalogo[livro.isbn] = livro
            print(f"Livro '{livro.titulo}' adicionado ao catálogo.")
        else:
            print(f"Erro: Livro com ISBN {livro.isbn} já existe.")

    def emprestar_livro(self, isbn):
        """Marca um livro como emprestado, se estiver disponível."""
        if isbn in self.catalogo:
            livro = self.catalogo[isbn]
            if not livro.emprestado:
                livro.emprestado = True
                self.emprestimos.append(isbn)
                print(f"Livro '{livro.titulo}' emprestado com sucesso.")
            else:
                print(f"Erro: Livro '{livro.titulo}' já está emprestado.")
        else:
            print(f"Erro: Livro com ISBN {isbn} não encontrado no catálogo.")

    def devolver_livro(self, isbn):
        """Marca um livro como disponível e remove do registro de empréstimos."""
        if isbn in self.catalogo:
            livro = self.catalogo[isbn]
            if livro.emprestado:
                livro.emprestado = False
                self.emprestimos.remove(isbn)
                print(f"Livro '{livro.titulo}' devolvido com sucesso.")
            else:
                print(f"Erro: Livro '{livro.titulo}' não estava emprestado.")
        else:
            print(f"Erro: Livro com ISBN {isbn} não encontrado no catálogo.")
            
    def listar_catalogo(self):
        """Lista todos os livros no catálogo."""
        print(f"\n--- Catálogo da Biblioteca {self.nome} ({len(self.catalogo)} Livros) ---")
        if not self.catalogo:
             print("O catálogo está vazio.")
             return
             
        for livro in self.catalogo.values():
            # O print usa o método __str__ definido na classe Livro
            print(f"- {livro}") 

# --- Demonstração do Sistema de Biblioteca ---

# 1. Configuração inicial
minha_biblioteca = Biblioteca("Conhecimento Livre")

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-8573216897")
livro2 = Livro("1984", "George Orwell", "978-8535914849")
livro3 = Livro("Pequeno Príncipe", "Antoine de Saint-Exupéry", "978-8580572832")

minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.adicionar_livro(livro3)

# 2. Listar o catálogo inicial
minha_biblioteca.listar_catalogo()

# 3. Realizar empréstimos
minha_biblioteca.emprestar_livro("978-8535914849") # Empresta '1984'
minha_biblioteca.emprestar_livro("978-8580572832") # Empresta 'Pequeno Príncipe'

# 4. Listar o catálogo após empréstimos (para ver a mudança de status)
minha_biblioteca.listar_catalogo()

# 5. Devolver um livro
minha_biblioteca.devolver_livro("978-8580572832") # Devolve 'Pequeno Príncipe'

# 6. Listar o catálogo final
minha_biblioteca.listar_catalogo()