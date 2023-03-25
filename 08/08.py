from itertools import product
from typing import List, Tuple, Callable

FILEPATH = "08-ex.input"


def get_tree_matrix_from_file(filepath: str):
    with open(filepath) as f:
        matrix = [[int(i) for i in line.rstrip()] for line in f.readlines()]
    return matrix


def is_border_tree(matrix: List[List[int]], tree: Tuple[int, int]):
    matrix_x, matrix_y = len(matrix) - 1, len(matrix[0]) - 1
    return tree[0] == 0 or tree[0] == matrix_x or tree[1] == 0 or tree[1] == matrix_y


def is_direction_hidden(start: int, end: int, comparison: Callable[[int], bool]):
    for i in range(start, end):
        if comparison(i):
            return True
    return False


def is_left_hidden(matrix: List[List[int]], tree: Tuple[int, int]):
    return is_direction_hidden(0, tree[1], lambda y: matrix[tree[0]][y] >= matrix[tree[0]][tree[1]])


def is_right_hidden(matrix: List[List[int]], tree: Tuple[int, int]):
    return is_direction_hidden(tree[1] + 1, len(matrix[0]), lambda y: matrix[tree[0]][y] >= matrix[tree[0]][tree[1]])


def is_up_hidden(matrix: List[List[int]], tree: Tuple[int, int]):
    return is_direction_hidden(0, tree[0], lambda x: matrix[x][tree[1]] >= matrix[tree[0]][tree[1]])


def is_down_hidden(matrix: List[List[int]], tree: Tuple[int, int]):
    return is_direction_hidden(tree[0] + 1, len(matrix), lambda x: matrix[x][tree[1]] >= matrix[tree[0]][tree[1]])


def is_tree_hidden(matrix: List[List[int]], tree: Tuple[int, int]):
    return (
        is_left_hidden(matrix, tree)
        and is_right_hidden(matrix, tree)
        and is_up_hidden(matrix, tree)
        and is_down_hidden(matrix, tree)
    )


def is_tree_visible(matrix: List[List[int]], tree: Tuple[int, int]):
    return is_border_tree(matrix, tree) or not is_tree_hidden(matrix, tree)


def main():
    matrix = get_tree_matrix_from_file(FILEPATH)
    x, y = len(matrix), len(matrix[0])
    for i, j in product(range(x), range(y)):
        print(is_tree_visible(matrix, (i, j)), end="\n" if j == y - 1 else "\t")
    visible_trees_count = sum([is_tree_visible(matrix, (i, j)) for i, j in product(range(x), range(y))])
    print("The number of visible trees in the matrix is:", visible_trees_count)


if __name__ == "__main__":
    main()
