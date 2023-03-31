import sys
from collections import namedtuple
from dataclasses import dataclass
from typing import Dict, List, Tuple

SNAPSHOT_INTERVAL = 40
SNAPSHOT_CEIL = 220

Waveform = namedtuple("Waveform", "x cycle")


@dataclass
class Command:
    duration: int
    action: callable

    def execute(self, waveform: Waveform, parameters: Dict) -> Waveform:
        x = self.action(waveform.x, parameters)
        cycle = waveform.cycle + self.duration
        return Waveform(x, cycle)


commands = {
    "noop": Command(1, lambda x, _: x),
    "addx": Command(2, lambda x, p: x + int(p[0])),
}


def parse_command_line(line: str) -> Tuple[Command, Dict]:
    args = line.rstrip().split()
    return commands[args[0]], args[1:]


def update_snapshots(snapshots: List[int], snapshot_cycle: int, previous: Waveform, current: Waveform) -> int:
    wave = None
    if current.cycle == snapshot_cycle:
        wave = current
    elif current.cycle > snapshot_cycle > previous.cycle:
        wave = previous

    if wave is None:
        return snapshot_cycle

    snapshots.append(wave.x * snapshot_cycle)
    next_snapshot_cycle = snapshot_cycle + SNAPSHOT_INTERVAL
    if next_snapshot_cycle > SNAPSHOT_CEIL:
        raise OverflowError
    return next_snapshot_cycle


def get_signal_strengths_sum(filepath: str) -> int:
    current_wave = Waveform(1, 1)
    next_snapshot_cycle = 20
    snapshots = []
    with open(filepath) as f:
        for line in f.readlines():
            command, parameters = parse_command_line(line)
            new_wave = command.execute(current_wave, parameters)
            try:
                next_snapshot_cycle = update_snapshots(snapshots, next_snapshot_cycle, current_wave, new_wave)
            except OverflowError:
                break
            current_wave = new_wave
    return sum(snapshots)


if __name__ == "__main__":
    filepath = sys.argv[1]
    total = get_signal_strengths_sum(filepath)
    print(f"The sum of these signal strengths is {total}.")
