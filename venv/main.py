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
        row_index = 0
        for row in self.numbers:
            new_row = []
            for value in row:
                node = Node(value, row_index)
                new_row.append(node)
            nodes.append(new_row)
            row_index += 1
        return nodes

    def create_family(self):
        self.head_node = self.nodes[0][0]
        row_index = 0
        for row in self.nodes:
            node_index = 0
            for node in row:
                left, right = self.get_children(row_index, node_index)
                node.assign_children(left, right)
                left, right = self.get_parents(row_index, node_index)
                node.assign_parents(left, right)
                node_index += 1
            row_index += 1

    def get_children(self, row_id, item_id):
        if row_id == self.height - 1:
            return None, None
        return self.nodes[row_id + 1][item_id], self.nodes[row_id + 1][item_id + 1]

    def get_parents(self, row_id, item_id):
        if row_id == 0:
            return None, None
        left = None if item_id == 0 else self.nodes[row_id-1][item_id-1]
        right = None if item_id == len(self.nodes[row_id]) - 1 else self.nodes[row_id-1][item_id]
        return left, right

    def generate_paths(self):
        return self.look_deeper(self.head_node)

    def look_deeper(self, node):
        value = node.value

        if node.if_visited:
            return node.best_path_to_bottom, node.best_path_to_bottom_sum
        else:
            node.if_visited = True
            if node.has_children():
                left = self.look_deeper(node.left_child)
                right = self.look_deeper(node.right_child)
                node.best_path_to_bottom, node.best_path_to_bottom_sum = self.analyse_results(left, right, node)
            else:
                node.best_path_to_bottom_sum = value
                node.best_path_to_bottom = [value]
            return node.best_path_to_bottom, node.best_path_to_bottom_sum

    @staticmethod
    def analyse_results(left_result, right_result, node):
        value = node.value
        l_path, l_sum = left_result
        r_path, r_sum = right_result
        if l_sum < r_sum:
            return [value] + l_path, l_sum + value
        else:
            return [value] + r_path, r_sum + value


class Node:
    def __init__(self, value, height):
        self.value = value
        self.best_path_to_bottom = None
        self.best_path_to_bottom_sum = inf

        self.left_child = None
        self.right_child = None
        self.left_parent = None
        self.right_parent = None
        self.if_visited = False
        self.height = height

    def assign_parents(self, left, right):
        self.left_parent = left
        self.right_parent = right

    def assign_children(self, left, right):
        self.left_child = left
        self.right_child = right

    def has_children(self):
        return True if self.left_child is not None and self.right_child is not None else False


def main():
    # triangle_name = '1-very_easy.txt'
    # triangle_name = '2-easy.txt'

    triangle_name = '3-medium.txt'

    triangle = Triangle(f'{INPUT_DIRECTORY}/{triangle_name}')
    triangle.generate_paths()

    print(triangle_name)
    print(triangle.head_node.best_path_to_bottom)
    print(triangle.head_node.best_path_to_bottom_sum)


if __name__ == "__main__":
    main()
