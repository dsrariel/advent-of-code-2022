def get_item_priority(item: str) -> int:
    if item >= "a" and item <= "z":
        priority = ord(item) - ord("a") + 1
    else:
        priority = ord(item) - ord("A") + 27
    return priority


elves_number = 3
previous_common_items = set()
common_items = set()
total_priority = 0
with open("03.input") as f:
    for i, line in enumerate(f.readlines()):
        common_items = set(item for item in line[:-1] if not previous_common_items or item in previous_common_items)
        previous_common_items = common_items

        is_last = (i + 1) % elves_number == 0
        if is_last:
            for item in common_items:
                total_priority += get_item_priority(item)
            previous_common_items = set()

        common_items = set()

print(total_priority)
