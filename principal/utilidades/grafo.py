class Grafo():
  def __init__(self):
    self.matriz = {}
    self.vertices = {}
    self.conexoes = []
  
  # adiciona um vértice (recebe o objeto de um vértice)
  def add_vert(self, vertice):
    self.vertices.update({vertice.nome: vertice})
  
  # serve para definir a distância entre dois vertices
  # obs: tbm funciona se colocar None como argumento
  def ligar(self, nome_a, nome_b, distancia):
    self.vertices[nome_a].set_distancia(nome_b, distancia)
    self.vertices[nome_b].set_distancia(nome_a, distancia)
  
  # serve para verificar a ligação entre dois vertices
  def check_adj(self, a, b):
    try: return self.vertices[a].vizinhos[b]
    except: return None

  # função para a realização do algortimo bellman-ford
  def bellman_ford(self, origem, destino):
      distancias = {v: float('inf') for v in self.vertices}
      predecessores = {v: None for v in self.vertices}
      distancias[origem] = 0

      for _ in range(len(self.vertices) - 1):
          for nome_a, vertice in self.vertices.items():
              for nome_b, distancia in vertice.vizinhos.items():
                  if distancias[nome_a] + distancia < distancias[nome_b]:
                      distancias[nome_b] = distancias[nome_a] + distancia
                      predecessores[nome_b] = nome_a

      # aqui verifica se há ciclos de peso negativo
      for nome_a, vertice in self.vertices.items():
          for nome_b, distancia in vertice.vizinhos.items():
              if distancias[nome_a] + distancia < distancias[nome_b]:
                  raise ValueError("O grafo contém um ciclo de peso negativo.")

      # agora imprime o caminho mínimo (opcional)
      caminho = self.construir_caminho(origem, destino, predecessores)

      return distancias[destino], caminho

  # gera a lista de estações do trajeto entre a estação de origem e a estação de destino
  def construir_caminho(self, origem, destino, predecessores):
      caminho = [destino]
      anterior = predecessores[destino]
      while anterior:
          caminho.insert(0, anterior)
          anterior = predecessores[anterior]

      return caminho

  def imprimir_caminho_minimo(self, origem, destino, predecessores):
      caminho = [destino]
      anterior = predecessores[destino]
      while anterior:
          caminho.insert(0, anterior)
          anterior = predecessores[anterior]

      print(f"Caminho mínimo de {origem} para {destino}: {' -> '.join(caminho)}")
