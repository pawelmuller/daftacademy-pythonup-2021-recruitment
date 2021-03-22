from copy import copy
import numpy as np


INPUT_DIRECTORY = 'input'


class Triangle:
    def __init__(self, filename=None):
        self.numbers = self.import_numbers(filename) if filename else []
        self.height = len(self.numbers)
        self.possible_paths = []
        self.summed_shortest_path = np.inf

    @staticmethod
    def import_numbers(filename):
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file]
        try:
            triangle = [list(map(int, line.split(' '))) for line in lines]
        except TypeError:
            print('Weird things happened')
        return triangle

    def generate_paths(self):
        self.possible_paths = [[np.inf]]
        self.look_deeper()

    def look_deeper(self, row_id=0, item_id=0, path=[], summed_path=0):
        item = self.numbers[row_id][item_id]
        path.append(item)
        summed_path += item
        if row_id < self.height - 1:
            if summed_path <= self.summed_shortest_path:
                self.look_deeper(row_id + 1, item_id, copy(path), summed_path)
                self.look_deeper(row_id + 1, item_id + 1, copy(path), summed_path)
        else:
            if summed_path < self.summed_shortest_path:
                self.possible_paths = []
                self.possible_paths.append(path)
                self.summed_shortest_path = summed_path
            elif summed_path == self.summed_shortest_path:
                self.possible_paths.append(path)


def main():
    triangle_files = ['1-very_easy.txt', '2-easy.txt']

    # Don't waste your time on this one, this brute-force solution lasts forever
    # triangle_files = ['1-very_easy.txt', '2-easy.txt', '3-medium.txt']

    for triangle_name in triangle_files:
        triangle = Triangle(f'{INPUT_DIRECTORY}/{triangle_name}')
        triangle.generate_paths()

        print(triangle_name)
        for path in triangle.possible_paths:
            print(f'{path} {sum(path)}')
        print('\n\n')


if __name__ == "__main__":
    main()
