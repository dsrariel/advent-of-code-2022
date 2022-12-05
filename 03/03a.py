def get_item_priority(item: str) -> int:
    if item >= "a" and item <= "z":
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


total_priority = 0
with open("03.input") as f:
    for line in f.readlines():
        first_compartment_end = len(line) // 2
        rucksack_first_compartment = set(i for i in line[:first_compartment_end])
        for item in line[first_compartment_end:]:
            if item in rucksack_first_compartment:
                total_priority += get_item_priority(item)
                break

print(total_priority)
