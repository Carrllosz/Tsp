class City:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

def read_tsp_file(file_path):
    cities = []
    reading_coords = False

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("NODE_COORD_SECTION"):
                reading_coords = True
                continue
            elif line.startswith("EOF") or line.startswith("TOUR_SECTION"):
                break

            if reading_coords:
                parts = line.split()
                if len(parts) == 3:
                    index, x, y = map(int, parts)
                    cities.append(City(index, x, y))

    return cities

def main():
    files = ["att48.tsp.txt"]

    for file_name in files:
        cities = read_tsp_file(file_name)

        print(f"\nCidades para o arquivo {file_name}:\n")
        for city in cities:
            print(f'City {city.index}: ({city.x}, {city.y})')

if __name__ == "__main__":
    main()
