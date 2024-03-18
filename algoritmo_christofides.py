import os
import networkx as nx
import numpy as np
from networkx.utils import pairwise

def ler_matriz_cidades(nome_arquivo):
    matriz_cidades = {}
    with open(nome_arquivo, 'r') as arquivo:
        for i, linha in enumerate(arquivo):
            valores = [float(valor) for valor in linha.split()]
            matriz_cidades[i + 1] = valores
    return matriz_cidades

def imprimir_matriz_dicionario(matriz):
    for cidade, distancias in matriz.items():
        print(f"{cidade}: {distancias}")

def calcular_distancia_euclidiana(cidade1, cidade2):
    return np.linalg.norm(np.array(cidade1) - np.array(cidade2))

def calcular_grafo_completo(matriz_cidades):
    G = nx.Graph()
    for cidade1, coord1 in matriz_cidades.items():
        for cidade2, coord2 in matriz_cidades.items():
            if cidade1 != cidade2:
                distancia = calcular_distancia_euclidiana(coord1, coord2)
                G.add_edge(cidade1, cidade2, weight=distancia)
    return G

def algoritmo_christofides(G):
    # Etapas do algoritmo de Christofides
    # 1. Construir uma árvore geradora mínima (MST)
    mst = nx.minimum_spanning_tree(G)
    
    # 2. Encontrar vértices com grau ímpar na MST
    graus_impares = [v for v, d in mst.degree() if d % 2 == 1]
    
    # 3. Construir um emparelhamento perfeito de peso mínimo entre esses vértices
    subgrafo_graus_impares = G.subgraph(graus_impares)
    emparelhamento_perfeito = nx.algorithms.matching.max_weight_matching(subgrafo_graus_impares)
    
    # 4. Adicionar o emparelhamento à MST para formar um multigrafo euleriano
    multigrafo_euleriano = nx.MultiGraph(mst)
    for u, v in emparelhamento_perfeito:
        multigrafo_euleriano.add_edge(u, v, weight=G[u][v]['weight'])
    
    # 5. Encontrar um ciclo euleriano no multigrafo euleriano
    ciclo_euleriano = list(nx.eulerian_circuit(multigrafo_euleriano))
    
    # 6. Converter o ciclo euleriano em um ciclo hamiltoniano
    ciclo_hamiltoniano = [ciclo_euleriano[0][0]]
    for u, v in ciclo_euleriano:
        if v not in ciclo_hamiltoniano:
            ciclo_hamiltoniano.append(v)
    
    # Retorna o ciclo hamiltoniano encontrado
    return ciclo_hamiltoniano

def busca_2_opt(caminho, matriz_cidades):
    n = len(caminho)
    while True:
        melhor_caminho = caminho
        melhor_distancia = calcular_distancia_total(caminho, matriz_cidades)
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue
                novo_caminho = caminho[:]
                novo_caminho[i:j] = caminho[j - 1:i - 1:-1]
                nova_distancia = calcular_distancia_total(novo_caminho, matriz_cidades)
                if nova_distancia < melhor_distancia:
                    melhor_caminho = novo_caminho
                    melhor_distancia = nova_distancia
        if melhor_caminho == caminho:
            break
        caminho = melhor_caminho
    return caminho

def calcular_distancia_total(caminho, matriz_cidades):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i + 1]
        distancia_total += calcular_distancia_euclidiana(matriz_cidades[cidade_atual], matriz_cidades[proxima_cidade])
    distancia_total += calcular_distancia_euclidiana(matriz_cidades[caminho[-1]], matriz_cidades[caminho[0]])  # Voltar à cidade inicial
    return distancia_total

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
G = calcular_grafo_completo(matriz_cidades)
ciclo_hamiltoniano_aproximado = algoritmo_christofides(G)
ciclo_hamiltoniano_otimizado = busca_2_opt(ciclo_hamiltoniano_aproximado, matriz_cidades)
print("Caminho otimizado:", ciclo_hamiltoniano_otimizado)
print("Distância total:", calcular_distancia_total(ciclo_hamiltoniano_otimizado, matriz_cidades))
