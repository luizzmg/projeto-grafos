from utilidades.grafo import Grafo
from utilidades.vertice import Vertice
from utilidades.funcoes import *

endereco_estacoes = "C:/Users/Luiz Miguel/Desktop/projeto-grafos/principal/database/as_estacoes.json"
pasta_linhas = "C:/Users/Luiz Miguel/Desktop/projeto-grafos/principal/database/"

metro = Grafo()

# colocando as estações no grafo (no metrô)
for estacao in json_para_dict(endereco_estacoes):
  metro.add_vert(Vertice(estacao["Name"],(estacao["Lat"]-39.119819)*-1300 +40, (estacao["Lon"]+77.491537)*1100 +40))

# definindo as distâncias entre elas
linhas = ["blue", "green", "orange", "red", "silver", "yellow"]

for linha in linhas:
  dici = json_para_dict(pasta_linhas + linha + "_distances.json")
  
  for i in range(1,len(dici)):
    # pegando o nome de uma, o nome de outra, e colocando a distancia entre elas
    nome_a = dici[i-1]["StationName"]
    nome_b = dici[i]["StationName"]

    metro.ligar(nome_a, nome_b, dici[i]["DistanceToPrev"])

    conexao = (metro.vertices[nome_a].coordenada, metro.vertices[nome_b].coordenada)

    if conexao not in metro.conexoes:
      metro.conexoes.append(conexao)

# criei um laço para solicitar entrada do usuário para a estação de origem
# adicionei algumas condicionais para caso ele coloque alguma estação fora da base de dados
while True:
    origem = input("")
    if origem in metro.vertices:
        break
    else:
        print("Estação não encontrada. Por favor, insira uma estação válida.")

# criei um laço para solicitar entrada do usuário para a estação de destino
# e adicionei algumas condicionais para caso ele coloque alguma estação fora da base de dados ou igual a origem
while True:
    destino = input("")
    if destino in metro.vertices and destino != origem:
        break
    elif destino == origem:
        print("A estação de destino deve ser diferente da estação de origem.")
    else:
        print("Estação não encontrada. Por favor, insira uma estação válida.")

# agora sim ele calcula e imprime a distância mínima e o trajeto entre as estações (pelo algoritmo de Bellman-Ford)
distancia_minima, trajeto = metro.bellman_ford(origem, destino, retornar_trajeto=True)
# adicionei o retornar trajeto para imprimir no fim da solicitação
print(f"A distância mínima entre {origem} e {destino} é {distancia_minima}.")

# aqui imprime o trajeto que falei, para deixar claro o percurso de uma estação para outra
if trajeto:
    print("Trajeto:")
    for estacao in trajeto:
        print(estacao)
# caso não haja caminhos válidos      
else:
    print("Não há um caminho válido entre as estações.")

