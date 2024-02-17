dic = {
  1:{1:False},
  2:{1:False, 2:False},
  3:{1:False, 2:False, 3:False},
  4:{1:False, 2:False, 3:False, 4:False}
  }

def checar_adj(dicionario, a,b):

  try: return dicionario[a][b]

  except: return dicionario[b][a]


# print(checar_adj(dic, 1, 4))
  
dii = {"teste": {"testando": "agr sim"}}


print(list(dii.values())[0])




