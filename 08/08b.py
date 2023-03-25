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

    def _get_tree_distance(self, neighbors: List[Tree], tree: Tree) -> int:
        count = 0
        for neighbor in neighbors:
            count += 1
            if self.get_tree_height(neighbor) >= self.get_tree_height(tree):
                break
        return count

    def _get_left_distance(self, tree: Tree) -> int:
        neighbors = [Tree(tree.x, y) for y in range(tree.y - 1, -1, -1)]
        return self._get_tree_distance(neighbors, tree)

    def _get_right_distance(self, tree: Tree) -> int:
        neighbors = [Tree(tree.x, y) for y in range(tree.y + 1, self.y)]
        return self._get_tree_distance(neighbors, tree)

    def _get_up_distance(self, tree: Tree) -> int:
        neighbors = [Tree(x, tree.y) for x in range(tree.x - 1, -1, -1)]
        return self._get_tree_distance(neighbors, tree)

    def _get_down_distance(self, tree: Tree) -> int:
        neighbors = [Tree(x, tree.y) for x in range(tree.x + 1, self.x)]
        return self._get_tree_distance(neighbors, tree)

    def get_tree_scenic_score(self, tree: Tree) -> int:
        return (
            self._get_left_distance(tree)
            * self._get_right_distance(tree)
            * self._get_up_distance(tree)
            * self._get_down_distance(tree)
        )


def create_forest_from_file(filepath: str) -> Forest:
    with open(filepath) as f:
        return Forest([[int(i) for i in line.rstrip()] for line in f.readlines()])


def main():
    filepath = sys.argv[1]
    forest = create_forest_from_file(filepath)
    max_scenic_score = max(
        [forest.get_tree_scenic_score(Tree(i, j)) for i, j in product(range(forest.x), range(forest.y))]
    )
    print("The maximum scenic score is:", max_scenic_score)


if __name__ == "__main__":
    main()
