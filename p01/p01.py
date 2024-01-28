def read_tsp_file(file_path):
    cities = []
    reading_coords = False

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("EDGE_WEIGHT_SECTION"):
                reading_coords = True
                continue
            elif line.startswith("EOF"):
                break

            if reading_coords:
                weights = list(map(int, line.split()))
                cities.extend(weights)

    return cities

def main():
    file_path = 'p01.tsp.txt'
    cities = read_tsp_file(file_path)

    # Imprimir as coordenadas das cidades
    num_cities = int(len(cities) ** 0.5)
    for i in range(num_cities):
        for j in range(num_cities):
            print(f'Peso entre a Cidade {i+1} e a Cidade {j+1}: {cities[i * num_cities + j]}')

if __name__ == "__main__":
    main()
