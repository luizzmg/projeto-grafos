import json

with open("C:/Users/Luiz Miguel/Desktop/projeto/red_distances.json") as arquivo:
  dict = json.load(arquivo)

print(dict["Path"][0]["StationCode"])

