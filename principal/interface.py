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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Defina as coordenadas dos círculos como uma lista de tuplas (x, y)
circle_positions = [(100, 100), (200, 200), (300, 300)]

# Crie a janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Círculos em Coordenadas")

estacoes = [((estacao.lon+77.491537)*1000 +100, (estacao.lat-39.119819)*-1000 +100) for estacao in metro.vertices.values()]

print(*estacoes, sep="\n")

# Loop principal
while True:
  # Verifique eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Preencha o fundo com a cor branca
  screen.fill(WHITE)

  # Desenhe círculos em cada coordenada especificada
  # for pos in circle_positions:
  #   pygame.draw.circle(screen, BLACK, pos, 10)  # Desenha círculo preto de raio 10
  
  for loc in estacoes:
    pygame.draw.circle(screen, BLACK, loc, 3)  # Desenha círculo preto de raio 5


  # Atualize a tela
  pygame.display.flip()
