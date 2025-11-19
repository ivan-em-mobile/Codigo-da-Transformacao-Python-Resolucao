'''
Configurações Iniciais

'''
import pygame
import random
import os


# 1. Inicializa todos os módulos importados do Pygame
pygame.init()

# 2. Definição de Cores (R, G, B)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# 3. Dimensões do Ecrã
LARGURA = 600
ALTURA = 480
ECRA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Logo Catch - O Jogo da Mapfre")

# 4. Fontes
FONTE = pygame.font.Font(None, 36) # Usa a fonte padrão do sistema com tamanho 36

# --- Carregamento de Ativos (Assets) ---
# Obtém o caminho (path) para a pasta atual do ficheiro
DIRETORIO_ATUAL = os.path.dirname(__file__) 
CAMINHO_LOGO = os.path.join(DIRETORIO_ATUAL, 'logo_game.png') # ASSUMIMOS que o ficheiro 'logo.png' está na mesma pasta

# Tenta carregar o logo
try:
    LOGO_IMAGEM = pygame.image.load(CAMINHO_LOGO).convert_alpha()
    # Ajusta o tamanho do logo (opcional)
    LOGO_IMAGEM = pygame.transform.scale(LOGO_IMAGEM, (100, 100)) 
    LOGO_RECT = LOGO_IMAGEM.get_rect()
except pygame.error as e:
    print(f"Erro ao carregar o logo: {e}")
    # Se o logo não carregar, usa um quadrado placeholder
    LOGO_IMAGEM = pygame.Surface((100, 100))
    LOGO_IMAGEM.fill(VERDE)
    LOGO_RECT = LOGO_IMAGEM.get_rect()


# --- Classes de Jogo ---

class Jogador(pygame.sprite.Sprite):
    """Representa o logótipo que o jogador controla."""
    def __init__(self):
        # Chama o construtor da classe base (Sprite)
        super().__init__() 
        
        # Define a imagem e a área de colisão (rect)
        self.image = "logo_game.png"  # Usa a imagem do logo carregada
        self.rect = self.image.get_rect()
        
        # Posição inicial (centro inferior do ecrã)
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 10 
        
        # Velocidade de movimento
        self.velocidade_x = 0
        self.velocidade_movimento = 8 # Ajuste esta velocidade se necessário

    def update(self):
        """Atualiza a posição do jogador (logótipo)."""
        # Recebe o estado das teclas
        teclas = pygame.key.get_pressed()
        self.velocidade_x = 0
        
        # Controlo de movimento
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.velocidade_x = -self.velocidade_movimento
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.velocidade_x = self.velocidade_movimento

        # Aplica o movimento
        self.rect.x += self.velocidade_x
        
        # Mantém o logo dentro dos limites do ecrã
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0

class Coletavel(pygame.sprite.Sprite):
    """Representa os pequenos itens que caem (para apanhar)."""
    def __init__(self):
        super().__init__()
        
        # Cria uma superfície (imagem) simples
        self.image = pygame.Surface((20, 20))
        self.image.fill(BRANCO) # Cor do coletável
        
        self.rect = self.image.get_rect()
        
        # Posição inicial (topo do ecrã, posição x aleatória)
        self.rect.x = random.randrange(LARGURA - self.rect.width)
        self.rect.y = random.randrange(-100, -40) # Começa acima do ecrã
        
        # Velocidade de queda
        self.velocidade_y = random.randrange(3, 7)
        self.velocidade_x = random.randrange(-1, 1)

    def update(self):
        """Atualiza a posição do coletável (cai)."""
        self.rect.y += self.velocidade_y
        self.rect.x += self.velocidade_x
        
        # Se o coletável sair da parte inferior do ecrã, ele é reposicionado
        if self.rect.top > ALTURA + 10 or self.rect.left < -25 or self.rect.right > LARGURA + 25:
            self.reset()

    def reset(self):
        """Reposiciona o coletável no topo do ecrã."""
        self.rect.x = random.randrange(LARGURA - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidade_y = random.randrange(3, 7)
        self.velocidade_x = random.randrange(-1, 1)


# --- Loop Principal do Jogo ---

def jogo_loop():
    """Função que contém a lógica principal do jogo."""
    
    # Grupos de Sprites: Usados para desenhar e atualizar todos os objetos facilmente
    todos_sprites = pygame.sprite.Group()
    coletaveis = pygame.sprite.Group()

    # Cria o jogador (Logo)
    jogador = Jogador()
    todos_sprites.add(jogador)

    # Cria os coletáveis
    for i in range(10): # Número de itens a cair
        coletavel = Coletavel()
        todos_sprites.add(coletavel)
        coletaveis.add(coletavel)
    
    # Variáveis do Jogo
    pontuacao = 0
    jogo_ativo = True
    relogio = pygame.time.Clock() # Ajuda a controlar a taxa de frames

    while jogo_ativo:
        # Define a taxa de frames (ex: 60 frames por segundo)
        relogio.tick(60) 

        # 1. Processar Inputs (Eventos)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
                
        # 2. Atualizar
        todos_sprites.update()
        
        # Verificar colisões entre o jogador e os coletáveis
        # A função 'pygame.sprite.spritecollide' verifica colisões.
        # O argumento 'True' (terceiro argumento) faz com que o coletável 
        # seja automaticamente removido do grupo quando colidir.
        colisoes = pygame.sprite.spritecollide(jogador, coletaveis, True) 
        
        for coletavel_atingido in colisoes:
            pontuacao += 10
            # Adiciona um novo coletável para substituir o que foi apanhado
            novo_coletavel = Coletavel()
            todos_sprites.add(novo_coletavel)
            coletaveis.add(novo_coletavel)
            
        # 3. Desenhar / Renderizar
        ECRA.fill(PRETO) # Pinta o fundo de preto
        
        todos_sprites.draw(ECRA) # Desenha todos os sprites nos grupos
        
        # Desenhar a Pontuação
        texto_pontuacao = FONTE.render(f"Pontuação: {pontuacao}", True, BRANCO)
        ECRA.blit(texto_pontuacao, (10, 10)) # Desenha no canto superior esquerdo

        # Atualiza o ecrã para mostrar o que foi desenhado
        pygame.display.flip() 

    # Se o loop terminar (jogo_ativo = False)
    pygame.quit()

# --- Iniciar o Jogo ---
if __name__ == "__main__":
    jogo_loop()