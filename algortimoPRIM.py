import time

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def minKey(self, key, mstSet):
        min_val = float("inf")
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and mstSet[v] == False:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self, time_limit):
        key = [float("inf")] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        start_time = time.time()
        time_elapsed = 0

        while time_elapsed < time_limit:
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

            time_elapsed = time.time() - start_time

        mst_weight = sum(self.graph[i][parent[i]] for i in range(1, self.V))
        return mst_weight


def ler_matriz_cidades(nome_arquivo):
    matriz_cidades = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            valores = [float(valor) for valor in linha.split()]
            matriz_cidades.append(valores)
    return matriz_cidades


import time

def calcular_limite_inferior(bases, limite_tempo):
    resultado = {}
    for base, arquivo in bases.items():
        start_time = time.time()
        matriz_cidades = ler_matriz_cidades(arquivo)
        V = len(matriz_cidades)
        g = Graph(V)
        g.graph = matriz_cidades
        limite_inferior = g.primMST(limite_tempo)
        end_time = time.time()
        tempo_processamento = end_time - start_time
        resultado[base] = (limite_inferior, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)), tempo_processamento)
    return resultado

limite_tempo = 12 * 60 * 60  # 12 horas em segundos

bases = {
    "Att48": r'C:\Users\João Carlos\Trabalho de TG\att48\att48_d.txt',
    "Dantzig42": r'C:\Users\João Carlos\Trabalho de TG\dantzig42\dantzig42_d.txt',
    "Fri26": r'C:\Users\João Carlos\Trabalho de TG\fri26\fri26_d.txt',
    "Gr17": r'C:\Users\João Carlos\Trabalho de TG\gr17\gr17_d.txt',
    "P01": r'C:\Users\João Carlos\Trabalho de TG\p01\p01_d.txt'
}

resultado = calcular_limite_inferior(bases, limite_tempo)

for base, (limite, hora, tempo) in resultado.items():
    print(f"Lower bound for TSP ({base}): {limite}, calculated at {hora}, took {tempo} seconds.")
