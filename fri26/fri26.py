class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def read_tsp_file(file_path):
    cities = []
    reading_coords = False

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("EDGE_WEIGHT_SECTION"):
                reading_coords = True
                continue
            elif line.startswith("EOF") or line.startswith("TOUR_SECTION"):
                break

            if reading_coords:
                coords = list(map(int, line.split()))
                for i in range(len(coords)):
                    cities.append(City(coords[i], coords[i]))

    return cities

def main():
    file_path = 'fri26.tsp.txt'
    cities = read_tsp_file(file_path)

    # Imprimir as coordenadas das cidades
    for i, city in enumerate(cities, start=1):
        print(f'Cidade {i}: ({city.x}, {city.y})')

if __name__ == "__main__":
    main()
