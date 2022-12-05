from collections import deque
from dataclasses import dataclass, field
from typing import Deque, List

FILEPATH = "05.input"


@dataclass
class Move:
    count: int
    source: int
    destination: int


def string_to_move(string: str) -> Move:
    items = string.split()
    return Move(int(items[1]), int(items[3]) - 1, int(items[5]) - 1)


@dataclass
class Cargo:
    stacks: List[Deque[str]] = field(default_factory=list)

    def appendCrate(self, create: str, stackNumber: int):
        while len(self.stacks) <= stackNumber:
            self.stacks.append(deque())
        self.stacks[stackNumber].append(create)

    def addCratesFromString(self, string: str):
        stackNumber = 0
        for i in range(1, len(string), 4):
            create = string[i]
            if create != " ":
                self.appendCrate(create, stackNumber)
            stackNumber += 1

    def moveCrates(self, move: Move):
        for _ in range(move.count):
            crate = self.stacks[move.source].popleft()
            self.stacks[move.destination].appendleft(crate)

    def getTopCrates(self) -> str:
        topCrates = []
        for stack in self.stacks:
            topCrates.append(stack[0])
        return "".join(topCrates)


cargo = Cargo()

with open(FILEPATH) as f:
    for line in f.readlines():
        if line.startswith("move"):
            move = string_to_move(line)
            cargo.moveCrates(move)
        elif not line or line.startswith(" 1"):
            continue
        else:
            cargo.addCratesFromString(line)

print(cargo.getTopCrates())
