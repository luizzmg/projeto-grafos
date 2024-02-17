from Vertice import Vertice

class Grafo():
  def __init__(self):
    self.matriz = {}
    self.vertices = {}
  
  def add_vert(self, vertice):
    self.vertices.update({vertice.nome: vertice})
    self.matriz.update({vertice.nome:{}})

    for anterior in self.matriz.keys():
      self.matriz[vertice.nome].update({anterior: False})
    
    self.matriz[vertice.nome].update({vertice.nome: False})

  
  def ligar(self, a, b):
    try:
      self.matriz[a][b] = True

    except:
      self.matriz[b][a] = True
  
  def check_adj(self, a, b):
    try: return self.matriz[a][b]
    
    except: return self.matriz[a][b]

# daqui pra baixo é teste

metro = Grafo()

metro.add_vert(Vertice("Joana Bezerra"))
metro.add_vert(Vertice("Camaragibe"))
metro.add_vert(Vertice("Jaboatão"))
metro.add_vert(Vertice("Cajueiro Seco"))

for a in metro.matriz.keys():
  print(a, "aponta para", metro.matriz[a])


print("\n\n\n\n")

print("A adj entre JB e CMRGB")

print(metro.check_adj("Camaragibe", "Joana Bezerra"))

metro.ligar("Camaragibe", "Joana Bezerra")

print("A adj entre JB e CMRGB")

print(metro.check_adj("Camaragibe", "Joana Bezerra"))