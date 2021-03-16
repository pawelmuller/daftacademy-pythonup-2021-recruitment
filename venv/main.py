from copy import copy
from numpy import array, full, inf


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


    def get_children(self, row_id, item_id):
        return self.numbers[row_id + 1][item_id], self.numbers[row_id + 1][item_id + 1]


def main():
    very_easy = Triangle('input/1-very_easy.txt')
    print(very_easy.numbers)


if __name__ == "__main__":
    main()
