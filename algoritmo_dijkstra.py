import sys
import itertools

def ler_matriz_cidades(nome_arquivo):
    matriz_cidades = {}
    with open(nome_arquivo, 'r') as arquivo:
        for i, linha in enumerate(arquivo):
            valores = [float(valor) for valor in linha.split()]
            matriz_cidades[i + 1] = valores
    return matriz_cidades

def dijkstra(matriz, origem):
    n = len(matriz)
    visitados = [False] * n
    distancia = [sys.maxsize] * n
    distancia[origem - 1] = 0
    
    for _ in range(n):
        min_distancia = sys.maxsize
        for i in range(n):
            if distancia[i] < min_distancia and not visitados[i]:
                min_distancia = distancia[i]
                u = i
                
        visitados[u] = True
        
        for v in range(n):
            if not visitados[v] and matriz[u+1][v] > 0:
                if distancia[u] + matriz[u+1][v] < distancia[v]:
                    distancia[v] = distancia[u] + matriz[u+1][v]
    
    # Adicionando a distância de volta para o vértice inicial
    distancia[origem - 1] += matriz[u+1][origem - 1]  # Considera a distância de volta para o vértice inicial
    return distancia

def calcular_distancia(caminho, matriz_cidades):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i + 1]
        distancia_total += matriz_cidades[cidade_atual][proxima_cidade - 1]
    distancia_total += matriz_cidades[caminho[-1]][caminho[0] - 1]
    return distancia_total

def caixeiro_viajante(nome_arquivo, intervalo_log=1000):
    matriz_cidades = ler_matriz_cidades(nome_arquivo)
    cidades = list(matriz_cidades.keys())
    n = len(cidades)
    
    # Encontrar uma solução inicial usando Dijkstra
    menor_distancia_inicial = sys.maxsize
    melhor_caminho_dijkstra = None
    for i in range(1, n+1):
        distancia = dijkstra(matriz_cidades, i)
        distancia_total = sum(distancia)
        if distancia_total < menor_distancia_inicial:
            menor_distancia_inicial = distancia_total
            melhor_caminho_dijkstra = list(range(1, n+1))
            print("Melhor distância encontrada até agora (Dijkstra):", menor_distancia_inicial)
    
    # Refinar a solução inicial 
    menor_distancia_final = menor_distancia_inicial
    melhor_caminho_ = melhor_caminho_dijkstra
    print("Iniciando iterações a partir do caminho encontrado pelo Dijkstra...")
    iteracao = 0
    for permutacao in itertools.permutations(melhor_caminho_dijkstra):  # Começando a partir do caminho encontrado pelo Dijkstra
        distancia = calcular_distancia(permutacao, matriz_cidades)
        if distancia < menor_distancia_final:
            menor_distancia_final = distancia
            melhor_caminho_ = permutacao
            print("Melhor distância encontrada até agora:", menor_distancia_final)
        iteracao += 1
        if iteracao % intervalo_log == 0:
          print
    
    return menor_distancia_final, melhor_caminho_forca_bruta

arquivo = input("Bases:\n 1. Att48 \n 2. Dantzig42 \n 3. Fri26 \n 4. Gr17 \n 5. P01 \n Digite o número da base:")
if arquivo == "1":
    nome_arquivo = '/private/var/mobile/Containers/Data/Application/E23C257D-F2F8-4E9C-BA12-6F8822C2A917/Documents/eei2.py'
elif arquivo=="2":
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
intervalo_log = 100000  # Intervalo de iterações para mostrar o resultado parcial
menor_distancia, melhor_caminho = caixeiro_viajante(nome_arquivo, intervalo_log)
print("Menor distância encontrada pelo caixeiro viajante:", menor_distancia)
print("Melhor caminho encontrado:", melhor_caminho)
