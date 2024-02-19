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

def escrever(texto, tamanho, coordenada, cor):
  text_surface = pygame.font.Font(None, int(2*zoom_factor)).render(estacao.nome, True, BLACK)
  text_rect = text_surface.get_rect(topleft=(x-10*zoom_factor, y - 3*zoom_factor))  # Posição do texto na tela
  screen.blit(text_surface, text_rect) 

# Crie a janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Círculos em Coordenadas")

estacoes = [estacao.coordenada for estacao in metro.vertices.values()]

print(*estacoes, sep="\n")

zoom_factor = 1
move_hori = 0
move_vert = 0
movimento = 15

# Fonte e tamanho
font = pygame.font.Font(None, 32)

# Variável para armazenar o texto
input_text = ''

# para conseguir repetir uma tecla segurando ela
pygame.key.set_repeat(300, 30)

# Loop principal
while True:
  # Verifique eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      # Zoom in
      if event.key == pygame.K_PAGEUP:
        zoom_factor += 0.1
        move_hori -= 50
        move_vert -= 30
      # Zoom out
      elif event.key == pygame.K_PAGEDOWN:
        zoom_factor -= 0.1
        move_hori += 50
        move_vert += 30

      movimento = (zoom_factor/3)*15

      # mover direita
      if event.key == pygame.K_RIGHT:
        move_hori -= movimento
      # mover esquerda
      elif event.key == pygame.K_LEFT:
        move_hori += movimento
      # mover cima
      elif event.key == pygame.K_UP:
        move_vert += movimento
      # mover baixo
      elif event.key == pygame.K_DOWN:
        move_vert -= movimento
      # Limita o zoom mínimo
      zoom_factor = max(0.1, zoom_factor)

  # Preencha o fundo com a cor branca
  screen.fill(WHITE)
  
  # Obtenha a posição atual do mouse
  # mouse_pos = pygame.mouse.get_pos()
  
  # move_hori, move_vert = mouse_pos
  
  for estacao in metro.vertices.values():
    loc = estacao.coordenada

    x = loc[0]*zoom_factor + move_hori
    y = loc[1]*zoom_factor + move_vert
    
    coord = (x, y)
    pygame.draw.circle(screen, BLACK, coord, 5)

    escrever(estacao.nome, 2*zoom_factor, ((x-10)*zoom_factor, (y-3)*zoom_factor), BLACK)
  
  for linha in metro.conexoes:
    xa = linha[0][0]*zoom_factor + move_hori
    ya = linha[0][1]*zoom_factor + move_vert

    xb = linha[1][0]*zoom_factor + move_hori
    yb = linha[1][1]*zoom_factor + move_vert

    espessura = 2

    pygame.draw.line(screen, BLACK, (xa,ya), (xb,yb), espessura)

    text_surface = pygame.font.Font(None, int(10)).render("Pg Up - zoom in", True, BLACK)
    text_rect = text_surface.get_rect(topleft=(10,10))  # Posição do texto na tela
    screen.blit(text_surface, text_rect) 

  # Atualize a tela
  pygame.display.flip()