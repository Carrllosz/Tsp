import heapq
import itertools
import time

def ler_matriz_cidades(nome_arquivo):
    matriz_cidades = {}
    with open(nome_arquivo, 'r') as arquivo:
        for i, linha in enumerate(arquivo):
            valores = [float(valor) for valor in linha.split()]
            matriz_cidades[i + 1] = valores
    return matriz_cidades
    

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def calcular_distancia(caminho, graph):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i + 1]
        # Verifica se as cidades estão presentes no grafo
        if cidade_atual in graph and proxima_cidade in graph:
            # Verifica se os índices das cidades estão dentro do intervalo válido
            if 0 < cidade_atual <= len(graph) and 0 < proxima_cidade <= len(graph):
                distancia_total += graph[cidade_atual][proxima_cidade - 1]  # -1 para ajustar o índice
            else:
                # Se algum dos índices estiver fora do intervalo, retorna um valor alto
                return float('inf')
        else:
            # Se alguma das cidades não estiver presente no grafo, retorna um valor alto
            return float('inf')
    # Adiciona a distância de volta para a cidade inicial
    distancia_total += graph[caminho[-1]][caminho[0] - 1]  # -1 para ajustar o índice
    return distancia_total


def caixeiro_viajante(graph, intervalo_mensagem=10):
    menor_caminho = None
    menor_distancia = float('inf')
    cidades = list(range(1, len(graph) + 1))  # Começando em 1
    inicio = time.time()
    tempo_anterior = inicio
    for permutacao in itertools.permutations(cidades):
        distancia = calcular_distancia(permutacao, graph)
        if distancia < menor_distancia:
            menor_distancia = distancia
            menor_caminho = permutacao
        if time.time() - tempo_anterior >= intervalo_mensagem:
            print(f"Tempo decorrido: {round(time.time() - inicio, 2)} segundos. Melhor distância atual: {menor_distancia}. Caminho: {menor_caminho}")
            tempo_anterior = time.time()
    return menor_caminho, menor_distancia

def imprimir_caminho_e_peso(caminho, peso):
    print("Menor caminho encontrado:", caminho)
    print("Distância total:", peso)

arquivo = input("Bases:\n 1. Att48 \n 2. Dantzig42 \n 3. Fri26 \n 4. Gr17 \n 5. P01 \n Digite o número da base:")
if arquivo == "1":
    nome_arquivo = r'C:\Users\User\Desktop\PCV\Caixeiro-viajante-main\databases\att48_d.txt'
elif arquivo == "2":
    nome_arquivo = r'C:\Users\User\Desktop\PCV\Caixeiro-viajante-main\databases\dantzig42_d.txt'
elif arquivo == "3":
    nome_arquivo = r'C:\Users\User\Desktop\PCV\Caixeiro-viajante-main\databases\fri26_d.txt'
elif arquivo == "4":
    nome_arquivo = r'C:\Users\User\Desktop\PCV\Caixeiro-viajante-main\databases\gr17_d.txt'
elif arquivo == "5":
    nome_arquivo = r'C:\Users\User\Desktop\PCV\Caixeiro-viajante-main\databases\p01_d.txt'
else:
    print("Arquivo não encontrado")
    exit()

matriz_cidades = ler_matriz_cidades(nome_arquivo)

menor_caminho, menor_distancia = caixeiro_viajante(matriz_cidades)

if menor_caminho is not None:
    imprimir_caminho_e_peso(menor_caminho, menor_distancia)
