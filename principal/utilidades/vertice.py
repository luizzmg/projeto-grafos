class Vertice():
  def __init__(self, nome, coordenada):
    self.nome = nome
    self.vizinhos = {}
    self.coordenada = coordenada
  
  def set_distancia(self, nome_viz, dist_viz):
    self.vizinhos.update({nome_viz: dist_viz})