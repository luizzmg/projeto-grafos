from utilidades.grafo import Grafo
from utilidades.vertice import Vertice
from utilidades.funcoes import *

endereco_estacoes = "C:/Users/Luiz Miguel/Desktop/projeto-grafos/principal/database/as_estacoes.json"

metro = Grafo()

for estacao in json_para_dict(endereco_estacoes):
  metro.add_vert(Vertice(estacao["Name"], (estacao["Lat"], estacao["Lon"])))

for chave in metro.vertices.keys():
  print(metro.vertices[chave].nome, metro.vertices[chave].coordenada)