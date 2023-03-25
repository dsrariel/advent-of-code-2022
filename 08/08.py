import sys
from collections import namedtuple
from itertools import product
from typing import List

Tree = namedtuple("Tree", "x y")


class Forest:
    def __init__(self, tree_matrix: List[List[int]]):
        self._matrix = tree_matrix
        self.x = len(tree_matrix)
        self.y = len(tree_matrix[0])

    def get_tree_height(self, tree: Tree) -> int:
        return self._matrix[tree.x][tree.y]

    def _is_tree_smaller_than_any_neighbor(self, neighbors: List[Tree], tree: Tree) -> bool:
        for neighbor in neighbors:
            if self.get_tree_height(neighbor) >= self.get_tree_height(tree):
                return True
        return False

    def _is_tree_left_hidden(self, tree: Tree):
        neighbors = [Tree(tree.x, y) for y in range(0, tree.y)]
        return self._is_tree_smaller_than_any_neighbor(neighbors, tree)

    def _is_tree_right_hidden(self, tree: Tree):
        neighbors = [Tree(tree.x, y) for y in range(tree.y + 1, self.y)]
        return self._is_tree_smaller_than_any_neighbor(neighbors, tree)

    def _is_tree_up_hidden(self, tree: Tree):
        neighbors = [Tree(x, tree.y) for x in range(0, tree.x)]
        return self._is_tree_smaller_than_any_neighbor(neighbors, tree)

    def _is_tree_down_hidden(self, tree: Tree):
        neighbors = [Tree(x, tree.y) for x in range(tree.x + 1, self.x)]
        return self._is_tree_smaller_than_any_neighbor(neighbors, tree)

    def is_tree_hidden(self, tree: Tree):
        return (
            self._is_tree_left_hidden(tree)
            and self._is_tree_right_hidden(tree)
            and self._is_tree_up_hidden(tree)
            and self._is_tree_down_hidden(tree)
        )


def create_forest_from_file(filepath: str) -> Forest:
    with open(filepath) as f:
        return Forest([[int(i) for i in line.rstrip()] for line in f.readlines()])


def main():
    filepath = sys.argv[1]
    forest = create_forest_from_file(filepath)
    visible_trees_count = sum(
        [not forest.is_tree_hidden(Tree(i, j)) for i, j in product(range(forest.x), range(forest.y))]
    )
    print("The number of visible trees in the matrix is:", visible_trees_count)


if __name__ == "__main__":
    main()
