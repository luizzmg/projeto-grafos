import pygame
import sys
from main import metro

origem = ""
destino = ""
resolveu = False

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da janela
WIDTH, HEIGHT = 850, 650
WINDOW_SIZE = (WIDTH, HEIGHT)

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definindo as coordenadas dos círculos como uma lista de tuplas (x, y)
circle_positions = [(100, 100), (200, 200), (300, 300)]

def escrever(texto, tamanho, coordenada, cor):
  text_surface = pygame.font.Font(None, int(tamanho)).render(texto, True, cor)
  text_rect = text_surface.get_rect(topleft=(coordenada))  # Posição do texto na tela
  screen.blit(text_surface, text_rect) 

# Criando a janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Círculos em Coordenadas")

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
  # Verificando eventos
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

      if origem == "" or destino == "":
        if event.key == pygame.K_RETURN:
          print("Texto inserido:", input_text)  # Apenas para demonstração, você pode modificar conforme necessário
          
          if origem == "":
            origem = input_text
          
          elif destino == "":
            destino = input_text
            
          input_text = ''  # Limpa o texto após pressionar Enter
        elif event.key == pygame.K_BACKSPACE:
          input_text = input_text[:-1]  # Remove o último caractere
        else:
          input_text += event.unicode  # Adiciona o caractere digitado à variável de texto

      # Limita o zoom mínimo
      zoom_factor = max(0.1, zoom_factor)

  # Preenchendo o fundo com a cor branca
  screen.fill(WHITE)
  
  for estacao in metro.vertices.values():
    loc = estacao.coordenada

    x = loc[0]*zoom_factor + move_hori
    y = loc[1]*zoom_factor + move_vert
    
    coord = (x, y)
    pygame.draw.circle(screen, BLACK, coord, 5)

    escrever(estacao.nome, 2*zoom_factor, (x+10, y-3), BLACK)
  
  for linha in metro.conexoes:
    xa = linha[0][0]*zoom_factor + move_hori
    ya = linha[0][1]*zoom_factor + move_vert

    xb = linha[1][0]*zoom_factor + move_hori
    yb = linha[1][1]*zoom_factor + move_vert

    espessura = 2

    pygame.draw.line(screen, BLACK, (xa,ya), (xb,yb), espessura)

  pygame.draw.rect(screen, (230,230,230),(0,00,150+ max(len(input_text),len(origem), len(destino))*25,90))

  if origem == "":
    escrever("Origem: "+input_text, 50, (10,10), BLACK)
    escrever("Destino: ", 50, (10,55), BLACK)
  
  elif destino == "":
    escrever("Origem: "+origem+" +", 50, (10,10), BLACK)
    escrever("Destino: "+input_text, 50, (10,55), BLACK)
  
  else:
    escrever("Origem: "+origem+" +", 50, (10,10), BLACK)
    escrever("Destino: "+destino+" +", 50, (10,55), BLACK)

    
    
  # escrever("Estação de origem: "+input_text, )  

  # Atualizar a tela
  pygame.display.flip()