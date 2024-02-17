import json

with open("principal/red_distances.json") as arquivo:
  dict = json.load(arquivo)



dict_list = dict["Path"]

for item in dict_list:
  print(item)
