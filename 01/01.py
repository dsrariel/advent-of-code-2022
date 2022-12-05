from heapq import heappush, heappop

heap_size = 3
top_elves = []
elf_total = 0

with open("01.input") as f:
    for line in f.readlines():
        if line == "\n":
            heappush(top_elves, elf_total)
            if len(top_elves) > heap_size:
                heappop(top_elves)
            elf_total = 0
        else:
            elf_total += int(line)

print(max(top_elves))
print(sum(top_elves))
