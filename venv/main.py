from copy import copy
from numpy import inf


INPUT_DIRECTORY = 'input'


class Triangle:
    def __init__(self, filename=None):
        self.numbers = self.import_numbers(filename) if filename else []
        self.height = len(self.numbers)
        self.head_node = None
        self.possible_paths = []

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
        self.possible_paths = [[inf]]
        self.look_deeper()

    def look_deeper(self, height=0, row_id=0, item_id=0, path=None):
        if path is None:
            path = []
        path.append(self.numbers[row_id][item_id])
        if height < self.height - 1:
            if sum(path) <= sum(self.possible_paths[0]):
                self.look_deeper(height + 1, row_id + 1, item_id, copy(path))
                self.look_deeper(height + 1, row_id + 1, item_id + 1, copy(path))
        else:
            if sum(path) < sum(self.possible_paths[0]):
                self.possible_paths = []
                self.possible_paths.append(path)
            elif sum(path) == sum(self.possible_paths[0]):
                self.possible_paths.append(path)

    def get_children(self, row_id, item_id):
        return self.numbers[row_id + 1][item_id], self.numbers[row_id + 1][item_id + 1]


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
