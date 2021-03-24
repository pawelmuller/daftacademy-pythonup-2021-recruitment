from numpy import inf


INPUT_DIRECTORY = 'input'


class Triangle:
    def __init__(self, filename=None):
        self.nodes = self.import_triangle(filename) if filename else []
        self.height = len(self.nodes)
        self.head_node = None
        if self.nodes:
            self.create_tree()

    @staticmethod
    def import_triangle(filename):
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file]
        try:
            nodes = []
            line_index = 0
            for line in lines:
                temp = []
                for element in line.split(' '):
                    new_node = Node(int(element), line_index)
                    temp.append(new_node)
                nodes.append(temp)
                line_index += 1
        except TypeError:
            print('Weird things happened')
        return nodes

    def create_tree(self):
        self.head_node = self.nodes[0][0]
        row_index = 0
        for row in self.nodes:
            node_index = 0
            for node in row:
                # Children:
                left, right = self.get_children(row_index, node_index)
                node.assign_children(left, right)
                # Parents:
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
        if not node.has_been_visited():
            node.set_visited(True)
            if node.has_children():
                left = self.look_deeper(node.left_child)
                right = self.look_deeper(node.right_child)
                node.best_path_to_bottom, node.best_path_to_bottom_sum = self.choose_better_result(left, right, node)
            else:
                node.best_path_to_bottom_sum = node.value
                node.best_path_to_bottom = [node.value]
        return node.best_path_to_bottom, node.best_path_to_bottom_sum

    @staticmethod
    def choose_better_result(left_result, right_result, node):
        value = node.value
        left_path, left_sum = left_result
        right_path, right_sum = right_result
        if left_sum < right_sum:
            return [value] + left_path, left_sum + value
        else:
            return [value] + right_path, right_sum + value


class Node:
    def __init__(self, value, height):
        self.value = value
        self.best_path_to_bottom = None
        self.best_path_to_bottom_sum = inf

        self.left_child = None
        self.right_child = None
        self.left_parent = None
        self.right_parent = None
        self.visited = False
        self.height = height

    def assign_parents(self, left, right):
        self.left_parent = left
        self.right_parent = right

    def assign_children(self, left, right):
        self.left_child = left
        self.right_child = right

    def has_children(self):
        return True if self.left_child is not None and self.right_child is not None else False

    def set_visited(self, new_state):
        self.visited = True if new_state else False

    def has_been_visited(self):
        return self.visited


def main():
    # triangle_name = '1-very_easy.txt'
    # triangle_name = '2-easy.txt'
    triangle_name = '3-medium.txt'

    triangle = Triangle(f'{INPUT_DIRECTORY}/{triangle_name}')
    triangle.generate_paths()

    print(triangle_name)
    print(triangle.head_node.best_path_to_bottom)
    print(triangle.head_node.best_path_to_bottom_sum)

    # For copying purposes:
    string = ""
    for digit in triangle.head_node.best_path_to_bottom:
        string += str(digit)
    print(string)


if __name__ == "__main__":
    main()
