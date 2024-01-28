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

arquivo = input("Bases:\n 1. Att48 \n 2. Dantzig42 \n 3. Fri26 \n 4. Gr17 \n 5. P01 \n Digite o número da base:")

if arquivo == "1":
    nome_arquivo = r'C:\Users\João Carlos\Trabalho de TG\att48\att48_d.txt'
    matriz_cidades = ler_matriz_cidades(nome_arquivo)
    imprimir_matriz_dicionario(matriz_cidades)
elif arquivo == "2":
    nome_arquivo = r'C:\Users\João Carlos\Trabalho de TG\dantzig42\dantzig42_d.txt'
    matriz_cidades = ler_matriz_cidades(nome_arquivo)
    imprimir_matriz_dicionario(matriz_cidades)
elif arquivo == "3":
    nome_arquivo = r'C:\Users\João Carlos\Trabalho de TG\fri26\fri26_d.txt'
    matriz_cidades = ler_matriz_cidades(nome_arquivo)
    imprimir_matriz_dicionario(matriz_cidades)
elif arquivo == "4":
    nome_arquivo = r'C:\Users\João Carlos\Trabalho de TG\gr17\gr17_d.txt'
    matriz_cidades = ler_matriz_cidades(nome_arquivo)
    imprimir_matriz_dicionario(matriz_cidades)
elif arquivo == "5":
    nome_arquivo = r'C:\Users\João Carlos\Trabalho de TG\p01\p01_d.txt'
    matriz_cidades = ler_matriz_cidades(nome_arquivo)
    imprimir_matriz_dicionario(matriz_cidades)
else: 
    print("Arquivo não encontrado")