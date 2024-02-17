class Grafo():
  def __init__(self):
    self.matriz = [[]]
    self.vertices = []
  
  def ligar(self, u, v):
    pass
  
  def check_adj(self, m, n):
    if m > n: return self.matriz[m][n]
    
    else: return self.matriz[n][m]
