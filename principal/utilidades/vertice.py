class Vertice():
  def __init__(self, nome, latitude, longitude):
    self.nome = nome
    self.vizinhos = {}
    self.lat = latitude
    self.lon = longitude
    
    # a coordenada vai ser definida como no pygame e plano cartesiano (x,y)
    self.coordenada = (longitude, latitude)
  
  def set_distancia(self, nome_viz, dist_viz):
    self.vizinhos.update({nome_viz: dist_viz})