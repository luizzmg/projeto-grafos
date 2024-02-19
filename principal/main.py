import pygame
import sys
from algoritmo import *

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
ORANGE = (255, 165, 0)

# Definindo as coordenadas dos círculos como uma lista de tuplas (x, y)
circle_positions = [(100, 100), (200, 200), (300, 300)]

def escrever(texto, tamanho, coordenada, cor):
  text_surface = pygame.font.Font(None, int(tamanho)).render(texto, True, cor)
  text_rect = text_surface.get_rect(topleft=(coordenada))  # Posição do texto na tela
  screen.blit(text_surface, text_rect) 

# Criando a janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("The Wash Way")

zoom_factor = 1
move_hori = 0
move_vert = 0
movimento = 15

# Fonte e tamanho
font = pygame.font.Font(None, 32)

# Variável para armazenar o texto
input_text = ''

# para conseguir repetir uma tecla segurando ela
pygame.key.set_repeat(300, 20)

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

    escrever(estacao.nome, 3*zoom_factor, (x+10, y-3), BLACK)
  
  for linha in metro.conexoes:
    xa = linha[0][0]*zoom_factor + move_hori
    ya = linha[0][1]*zoom_factor + move_vert

    xb = linha[1][0]*zoom_factor + move_hori
    yb = linha[1][1]*zoom_factor + move_vert

    espessura = 3

    pygame.draw.line(screen, BLACK, (xa,ya), (xb,yb), espessura)

  if origem == "" and destino == "":
    pygame.draw.rect(screen, (230,230,230),(0,0, WIDTH,90))
    escrever("Origem: "+input_text, 50, (10,10), BLACK)
    escrever("Destino: ", 50, (10,55), BLACK)

  elif origem in metro.vertices.keys() and destino == "":
    pygame.draw.rect(screen, (230,230,230),(0,0, WIDTH,90))
    escrever("Origem: "+origem+" - ok", 50, (10,10), BLACK)
    escrever("Destino: "+input_text, 50, (10,55), BLACK)
  
  elif destino in metro.vertices.keys():

    if not resolveu:
      trajeto, distancia_minima = algoritmo_final(origem, destino, metro)
      resolveu = True

    for i in range(1,len(trajeto)):
      coord_ori = metro.vertices[trajeto[i-1]].coordenada
      coord_dest = metro.vertices[trajeto[i]].coordenada
      
      x_ori, y_ori = coord_ori
      x_dest, y_dest = coord_dest

      pygame.draw.line(screen, ORANGE, (x_ori*zoom_factor + move_hori,y_ori*zoom_factor + move_vert), (x_dest*zoom_factor + move_hori,y_dest*zoom_factor + move_vert), espessura-2)
    
    pygame.draw.rect(screen, (230,230,230),(0,0, WIDTH,90))
    escrever("Origem: "+origem+" - ok", 50, (10,10), BLACK)
    escrever("Destino: "+destino+" - ok", 50, (10,55), BLACK)

    pygame.draw.rect(screen, (230,230,230),(0,HEIGHT - 45, WIDTH,45))
    percorrido_km = "{:.2f}".format(distancia_minima*0.3048/1000)
    escrever("Melhor trajeto: "+percorrido_km+" km", 50, (10,HEIGHT-40), BLACK)

  elif origem in metro.vertices.keys() and destino not in metro.vertices.keys():
    destino = ""
    pygame.draw.rect(screen, (230,230,230),(0,0, WIDTH,90))
    escrever("Origem: "+origem+" - ok", 50, (10,10), BLACK)
    escrever("Destino: "+input_text, 50, (10,55), BLACK)

  else:
    destino = ""
    origem = ""
    pygame.draw.rect(screen, (230,230,230),(0,0, WIDTH,90))
    escrever("Origem: "+input_text, 50, (10,10), BLACK)
    escrever("Destino: ", 50, (10,55), BLACK)
  
  pygame.draw.rect(screen, (20,20,20),(WIDTH/1.5,0, WIDTH/3,90))
  escrever("PgUp/Dn - zoom", 40, (WIDTH/1.5,10), WHITE)
  escrever("Setas - movimentar", 40, (WIDTH/1.5,55), WHITE)

  
  # Atualizar a tela
  pygame.display.flip()