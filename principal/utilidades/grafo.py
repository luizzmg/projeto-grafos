class Grafo():
  def __init__(self):
    self.matriz = {}
    self.vertices = {}
  
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