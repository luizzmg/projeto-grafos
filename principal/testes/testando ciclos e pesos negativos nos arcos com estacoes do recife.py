class Grafo:
    # fiz o grafo usando poo porque achei mais tranquilo de entender e desenvolver
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, peso):
        self.arestas.append([u, v, peso])

    def bellman_ford(self, inicio, fim):
        # aqui informa se a estação de início ou fim não existem no quadro de metrô da cidade
        if inicio not in self.vertices or fim not in self.vertices:
            print("Estação de início ou destino não existe no grafo.")
            return None, None
        # inicializa as distâncias com infinito e o vértice de início com 0
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0

        # relaxa as arestas repetidamente (aquilo que te mandei no whatsapp)
        for _ in range(len(self.vertices) - 1):
            for u, v, peso in self.arestas:
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso

        # verifica se há ciclos negativos (eu ACHO que não corremos esse risco mas é bom manter porque faz parte do algoritmo)
        for u, v, peso in self.arestas:
            if distancias[u] + peso < distancias[v]:
                print("O grafo contém um ciclo negativo.")
                return None

        # calcula o caminho mínimo
        caminho_minimo = [fim]
        atual = fim
        while atual != inicio:
            for u, v, peso in self.arestas:
                if v == atual and distancias[u] + peso == distancias[atual]:
                    caminho_minimo.append(u)
                    atual = u
                    break

        return list(reversed(caminho_minimo)), distancias[fim]

# definindo as estações e a distância entre elas
estacoes = ["Recife", "Joana Bezerra", "Largo da Paz", "Imbiribeira", "Antônio Falcão", "Shopping",
            "Tancredo Neves", "Aeroporto", "Porta Larga", "Monte dos Guararapes", "Prazeres", "Cajueiro Seco"]

distancia_entre_estacoes = 2
# coloquei em km (distância que eu supus apenas para teste mas certamente iremos por as distâncias exatas para cada estação)
# como por exemplo:
# distancias_entre_estacoes = [2, 3, 1, 4, 2, 3, 2, 1, 3, 2, 4]
# for i in range(len(estacoes) - 1):
#    grafo_metro.adicionar_aresta(estacoes[i], estacoes[i + 1], distancias_entre_estacoes[i])
# ou
# distancias_entre_estacoes = {
#    ("Recife", "Joana Bezerra"): 1,
#    ("Joana Bezerra", "Largo da Paz"): 2,
#     ... e assim vai
#}


# criando o grafo com as distâncias entre as estações
grafo_metro = Grafo(estacoes)

for i in range(len(estacoes) - 1):
    grafo_metro.adicionar_aresta(estacoes[i], estacoes[i + 1], distancia_entre_estacoes)

# recebimento das entradas (pode alterar para um input)
inicio = "Imbiribeira"
fim = "Aeroporto"

caminho, distancia = grafo_metro.bellman_ford(inicio, fim)

if caminho is not None: 
    # deixei em km por aqui em recife serem poucas estações e bem afastadas mas em washington podemos ver a possibilidade de ser em metros
    print("O menor caminho de", inicio, "para", fim, "é:", caminho)
    print("Distância total entre as estações:", distancia, "km")