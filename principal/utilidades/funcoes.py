import json
from utilidades.grafo import Grafo
from utilidades.vertice import Vertice

def json_para_dict(endereco_arq):

  with open(endereco_arq) as arquivo:
    dict = json.load(arquivo)

  return dict[list(dict.keys())[0]]

def main():
  pass

if __name__ == "__main__":
  main()