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

