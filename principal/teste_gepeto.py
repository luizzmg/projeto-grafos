import pygame
import sys
from main import metro

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
WIDTH, HEIGHT = 850, 650
WINDOW_SIZE = (WIDTH, HEIGHT)

# Defina as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Defina o fator de zoom inicial
zoom_factor = 1.0

# Crie a janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Círculos em Coordenadas")

estacoes = [estacao.coordenada for estacao in metro.vertices.values()]

# Loop principal
while True:
    # Verifique eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Zoom in
            if event.key == pygame.K_UP:
                zoom_factor += 0.1
            # Zoom out
            elif event.key == pygame.K_DOWN:
                zoom_factor -= 0.1
            # Limita o zoom mínimo
            zoom_factor = max(0.1, zoom_factor)

    # Preencha o fundo com a cor branca
    screen.fill(WHITE)

    # Crie uma nova superfície de desenho para aplicar o zoom
    scaled_surface = pygame.Surface((WIDTH * zoom_factor, HEIGHT * zoom_factor))

    # Desenhe círculos em cada coordenada especificada
    for loc in estacoes:
        scaled_pos = (int(loc[0] * zoom_factor), int(loc[1] * zoom_factor))
        pygame.draw.circle(scaled_surface, BLACK, scaled_pos, 3)  # Desenha círculo preto de raio 3

    for linha in metro.conexoes:
        pos_ini, pos_fim = linha
        scaled_ini = (int(pos_ini[0] * zoom_factor), int(pos_ini[1] * zoom_factor))
        scaled_fim = (int(pos_fim[0] * zoom_factor), int(pos_fim[1] * zoom_factor))
        espessura = max(1, int(2 * zoom_factor))  # Ajusta a espessura da linha com base no zoom
        pygame.draw.line(scaled_surface, BLACK, scaled_ini, scaled_fim, espessura)

    # Redimensione a superfície de desenho para o tamanho da janela e desenhe-a na tela
    scaled_surface = pygame.transform.scale(scaled_surface, WINDOW_SIZE)
    screen.blit(scaled_surface, (0, 0))

    # Atualize a tela
    pygame.display.flip()
