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
                coords = list(map(int, line.split()))
                cities.extend(coords)

    return cities

def main():
    file_path = 'gr17.tsp.txt'
    cities = read_tsp_file(file_path)

    # Imprimir as coordenadas das cidades
    num_cities = len(cities)
    for i in range(num_cities):
        x = cities[i]
        y = cities[(i + 1) % num_cities]  # O arquivo gr17.tsp.txt não contém -1, assumindo um ciclo

        print(f'Cidade {i+1}: ({x}, {y})')

if __name__ == "__main__":
    main()

