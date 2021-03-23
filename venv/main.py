from copy import copy
from numpy import inf


INPUT_DIRECTORY = 'input'
# 283


class Triangle:
    def __init__(self, filename=None):
        self.numbers = self.import_numbers(filename) if filename else []
        self.nodes = self.convert_numbers_to_nodes() if self.numbers else []
        self.height = len(self.numbers)
        self.head_node = None
        if self.nodes:
            self.create_family()

    @staticmethod
    def import_numbers(filename):
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file]
        try:
            triangle = [list(map(int, line.split(' '))) for line in lines]
        except TypeError:
            print('Weird things happened')
        return triangle

    def convert_numbers_to_nodes(self):
        nodes = []
        for row in self.numbers:
            new_row = []
            for value in row:
                new_row.append(Node(value))
            nodes.append(new_row)

    def create_family(self):
        row_index = 0
        for row in self.nodes:
            node_index = 0
            for node in row:
                left, right = self.get_children(row_index, node_index)
                node.assign_children(left, right)


                node_index += 1
            row_index += 1

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


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.left_parent = None
        self.right_parent = None

    def assign_parents(self, left, right):
        self.left_parent = left
        self.right_parent = right

    def assign_children(self, left, right):
        self.left_child = left
        self.right_child = right


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
