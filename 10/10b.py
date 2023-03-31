import sys
from collections import namedtuple
from dataclasses import dataclass
from typing import Dict, List, Tuple

Sprite = namedtuple("Waveform", "x cycle")


@dataclass
class Command:
    duration: int
    action: callable

    def execute(self, sprite: Sprite, parameters: Dict) -> Sprite:
        x = self.action(sprite.x, parameters)
        cycle = sprite.cycle + self.duration
        return Sprite(x, cycle)


commands = {
    "noop": Command(1, lambda x, _: x),
    "addx": Command(2, lambda x, p: x + int(p[0])),
}


def parse_command_line(line: str) -> Tuple[Command, Dict]:
    args = line.rstrip().split()
    return commands[args[0]], args[1:]


def update_pixels(pixels: List[str], previous: Sprite, current: Sprite):
    for _ in range(previous.cycle, current.cycle):
        pixel = len(pixels) % 40 + 1
        if (previous.x + 1) >= pixel >= (previous.x - 1):
            pixels.append("#")
        else:
            pixels.append(".")


def get_pixels(filepath: str) -> int:
    current_sprite = Sprite(2, 1)
    pixels = []
    with open(filepath) as f:
        for line in f.readlines():
            command, parameters = parse_command_line(line)
            new_sprite = command.execute(current_sprite, parameters)
            update_pixels(pixels, current_sprite, new_sprite)
            current_sprite = new_sprite
    return pixels


def render_pixels(pixels: List[str]) -> str:
    pixel_lines = ["".join(pixels[i * 40 : (i + 1) * 40]) for i in range(0, 6)]
    return "\n".join(pixel_lines)


if __name__ == "__main__":
    filepath = sys.argv[1]
    pixels = get_pixels(filepath)
    print(render_pixels(pixels))
