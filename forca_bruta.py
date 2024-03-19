import itertools
import sys

def ler_matriz_cidades(nome_arquivo):
    matriz_cidades = {}
    with open(nome_arquivo, 'r') as arquivo:
        for i, linha in enumerate(arquivo):
            valores = [float(valor) for valor in linha.split()]
            matriz_cidades[i + 1] = {j + 1: valor for j, valor in enumerate(valores)}
    return matriz_cidades


def imprimir_matriz_dicionario(matriz):
    for cidade, distancias in matriz.items():
        print(f"{cidade}: {distancias}")


def calcular_distancia_total(rota, grafo):
    distancia_total = 0
    n = len(rota)
    for i in range(n):
        origem, destino = rota[i], rota[(i + 1) % n]
        distancia_total += grafo[origem][destino]
    return distancia_total


def forca_bruta_pcv(grafo):
    menor_distancia = sys.maxsize
    melhor_rota = None

    for rota in itertools.permutations(grafo.keys()):
        distancia_total = calcular_distancia_total(rota, grafo)
        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            melhor_rota = rota

    return menor_distancia, melhor_rota



def processar_base(arquivo):
    bases = {
        "1": r'C:\Users\Liedson\Desktop\TRABALHO DE TG\att48\att48_d.txt',
        "2": r'C:\Users\Liedson\Desktop\TRABALHO DE TG\dantzig42\dantzig42_d.txt',
        "3": r'C:\Users\Liedson\Desktop\TRABALHO DE TG\fri26\fri26_d.txt',
        "4": r'C:\Users\Liedson\Desktop\TRABALHO DE TG\gr17\gr17_d.txt',
        "5": r'C:\Users\Liedson\Desktop\TRABALHO DE TG\p01\p01_d.txt'
    }

    if arquivo in bases:
        nome_arquivo = bases[arquivo]
        matriz_cidades = ler_matriz_cidades(nome_arquivo)
        imprimir_matriz_dicionario(matriz_cidades)
        melhor_rota, menor_distancia = forca_bruta_pcv(matriz_cidades)
        print("Melhor rota:", melhor_rota)
        print("Menor distância:", menor_distancia)
    else:
        print("Arquivo não encontrado")

arquivo = input("Bases:\n 1. Att48 \n 2. Dantzig42 \n 3. Fri26 \n 4. Gr17 \n 5. P01 \n Digite o número da base:")
processar_base(arquivo)
