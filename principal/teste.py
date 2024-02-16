import json

with open("C:/Users/Luiz Miguel/Desktop/projeto/red_distances.json") as arquivo:
  dict = json.load(arquivo)

# class station():
#   def __init__(self, lineCode, stationCode):
#     self.lineCode = lineCode
#     self.stationCode = stationCode
#     self.seqNum
#     self.distanceToPrev

dict_list = dict["path"]
