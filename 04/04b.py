from dataclasses import dataclass
from typing import Optional


FILEPATH = "04.input"


@dataclass
class Assignment:
    start: int
    end: int

    def intersection(self, other: "Assignment") -> Optional["Assignment"]:
        intersection = Assignment(max(self.start, other.start), min(self.end, other.end))
        if intersection.start > intersection.end:
            return None
        return intersection


def string_to_assignment(string: str) -> Assignment:
    numbers = string.split("-")
    return Assignment(int(numbers[0]), int(numbers[1]))


overlappingPairsNumber = 0
with open(FILEPATH) as f:
    for line in f.readlines():
        assignmentStrings = line[:-1].split(",")
        firstAssignment = string_to_assignment(assignmentStrings[0])
        secondAssignment = string_to_assignment(assignmentStrings[1])
        intersection = firstAssignment.intersection(secondAssignment)
        if intersection is not None:
            overlappingPairsNumber += 1

print(overlappingPairsNumber)
