from enum import Enum


class Options(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __gt__(self, opponent: "Options") -> bool:
        for option in Options:
            if self is option and opponent is self.getWeakest():
                return True
        return False

    def getWeakest(self):
        if self is self.ROCK:
            return self.SCISSORS
        if self is self.PAPER:
            return self.ROCK
        if self is self.SCISSORS:
            return self.PAPER


LETTER_TO_OPTION = {
    "A": Options.ROCK,
    "B": Options.PAPER,
    "C": Options.SCISSORS,
    "X": Options.ROCK,
    "Y": Options.PAPER,
    "Z": Options.SCISSORS,
}


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


class Match:
    def __init__(self, me: Options, opponent: Options):
        self.me = me
        self.opponent = opponent

    def __get_outcome(self) -> Outcome:
        if self.me > self.opponent:
            return Outcome.WIN
        if self.me is self.opponent:
            return Outcome.DRAW
        return Outcome.LOSS

    def get_score(self) -> int:
        return self.__get_outcome().value + self.me.value


def string_to_match(string: str) -> Match:
    letters = string.split()
    return Match(LETTER_TO_OPTION[letters[1]], LETTER_TO_OPTION[letters[0]])


total_score = 0
with open("02.input") as f:
    for line in f.readlines():
        match = string_to_match(line)
        total_score += match.get_score()

print(total_score)
