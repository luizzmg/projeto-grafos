import json
from utilidades.grafo import Grafo

def json_para_dict(endereco_arq):

  with open(endereco_arq) as arquivo:
    dict = json.load(arquivo)

  return dict[list(dict.keys())[0]]

def criar_vertices(endereco_arq):
  print(json_para_dict(endereco_arq))

  
  return

  pass

def main():
  criar_vertices("C:/Users/Luiz Miguel/Desktop/projeto-grafos/principal/database/as_estacoes.json")

if __name__ == "__main__":
  main()