from utilidades.grafo import Grafo
from utilidades.vertice import Vertice
from utilidades.funcoes import *

endereco_estacoes = "C:/Users/Luiz Miguel/Desktop/projeto-grafos/principal/database/as_estacoes.json"
pasta_linhas = "C:/Users/Luiz Miguel/Desktop/projeto-grafos/principal/database/"

metro = Grafo()

# colocando as estações no grafo (no metrô)
for estacao in json_para_dict(endereco_estacoes):
  metro.add_vert(Vertice(estacao["Name"], (estacao["Lat"], estacao["Lon"])))

# definindo as distâncias entre elas
linhas = ["blue", "green", "orange", "red", "silver", "yellow"]

for linha in linhas:
  dici = json_para_dict(pasta_linhas + linha + "_distances.json")
  
  for i in range(1,len(dici)):
    # pegando o nome de uma, o nome de outra, e colocando a distancia entre elas
    metro.ligar(dici[i-1]["StationName"],dici[i]["StationName"],dici[i]["DistanceToPrev"])

# calcula e imprime a distância mínima entre duas estações (pelo algoritmo de bellman-ford)
origem = "Estação A"
# coloquei como teste mas é para substituir pelo input ou alguma estação real da base de dados
destino = "Estação D"
# coloquei como teste mas é para substituir pelo input ou alguma estação real da base de dados
distancia_minima = metro.bellman_ford(origem, destino)
print(f"A distância mínima entre {origem} e {destino} é {distancia_minima}.")

