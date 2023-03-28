import sys
from collections import namedtuple
from dataclasses import dataclass
from enum import Enum

Command = namedtuple("Command", "direction count")


class Direction(Enum):
    U = "U"
    D = "D"
    R = "R"
    L = "L"


@dataclass
class Position:
    x: int
    y: int

    def move(self, direction: Direction) -> None:
        if direction is Direction.U:
            self.x -= 1
        if direction is Direction.D:
            self.x += 1
        if direction is Direction.L:
            self.y -= 1
        if direction is Direction.R:
            self.y += 1

    def __sub__(self, other: "Position") -> "Position":
        return Position(self.x - other.x, self.y - other.y)


def parse_command(string: str) -> Command:
    direction, count = string.rstrip().split()
    return Command(Direction[direction], int(count))


def move_tail(tail: Position, head: Position) -> None:
    diff = head - tail

    are_touching = abs(diff.x) <= 1 and abs(diff.y) <= 1
    if are_touching:
        return

    if diff.x != 0:
        tail.move(Direction.D if diff.x > 0 else Direction.U)
    if diff.y != 0:
        tail.move(Direction.R if diff.y > 0 else Direction.L)


def get_distinct_count_of_tail_positions(filepath: str, knots_num: int) -> int:
    rope = [Position(0, 0) for _ in range(knots_num)]
    visited = set([(0, 0)])
    with open(filepath) as f:
        for line in f.readlines():
            command = parse_command(line)
            for _ in range(command.count):
                rope[0].move(command.direction)
                for i, node in enumerate(rope[1:]):
                    move_tail(node, rope[i])
                visited.add((rope[-1].x, rope[-1].y))
    return len(visited)


if __name__ == "__main__":
    filepath = sys.argv[1]
    knots_num = 2 if len(sys.argv) == 2 else int(sys.argv[2])
    count = get_distinct_count_of_tail_positions(filepath, knots_num)
    print(f"there are {count} positions the tail visited at least once.")
