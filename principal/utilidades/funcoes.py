import json

# serve para transformar um json em dicionário
def json_para_dict(endereco_arq):

  with open(endereco_arq) as arquivo:
    dict = json.load(arquivo)

  return dict[list(dict.keys())[0]]