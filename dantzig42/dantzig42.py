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
            if line.startswith("EDGE_WEIGHT_SECTION"):
                reading_coords = True
                continue
            elif line.startswith("EOF") or line.startswith("DISPLAY_DATA_SECTION"):
                break

            if reading_coords:
                parts = list(map(float, line.split()))
                if len(parts) > 1:
                    for i, value in enumerate(parts):
                        if i != 0:
                            index = len(cities) + i
                            cities.append(City(index, parts[0], value))

    return cities

def main():
    files = ["dantzig42.tsp.txt"]

    for file_name in files:
        cities = read_tsp_file(file_name)

        print(f"\nCities for the file {file_name}:\n")
        for city in cities:
            print(f'City {city.index}: ({city.x}, {city.y})')

if __name__ == "__main__":
    main()
