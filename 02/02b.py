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

    def getStrongest(self):
        if self is self.ROCK:
            return self.PAPER
        if self is self.PAPER:
            return self.SCISSORS
        if self is self.SCISSORS:
            return self.ROCK

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
}


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


LETTER_TO_OUTCOME = {"X": Outcome.LOSS, "Y": Outcome.DRAW, "Z": Outcome.WIN}


class Match:
    def __init__(self, opponent: Options, outcome: Outcome):
        self.opponent = opponent
        self.outcome = outcome

    def _getMe(self) -> Options:
        if self.outcome is Outcome.WIN:
            return self.opponent.getStrongest()
        if self.outcome is Outcome.DRAW:
            return self.opponent
        return self.opponent.getWeakest()

    def get_score(self) -> int:
        return self.outcome.value + self._getMe().value


def string_to_match(string: str) -> Match:
    letters = string.split()
    return Match(LETTER_TO_OPTION[letters[0]], LETTER_TO_OUTCOME[letters[1]])


total_score = 0
with open("02.input") as f:
    for line in f.readlines():
        match = string_to_match(line)
        total_score += match.get_score()

print(total_score)
