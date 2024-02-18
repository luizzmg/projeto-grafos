import json

def json_para_dict(arquivo):

  with open("principal/red_distances.json") as arquivo:
    dict = json.load(arquivo)



  dict_list = dict["Path"]

  for item in dict_list:
    print(item)



def criar_vertices():
  pass