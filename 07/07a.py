from collections import deque
from dataclasses import dataclass, field
from typing import List, Optional, Union


FILEPATH = '07-ex.input'

@dataclass
class Item:
    name: str
    size: int
    parent: Optional['Directory'] = None
    items: List['Item'] = field(default_factory=list)

    def isFile(self) -> bool:
        return not self.items

    def add(self, item: 'Item'):
        self.items.append(item)
        if item.size == 0:
            return
        
        curr = self
        while curr != None:
            curr.size += item.size
            curr = curr.parent


def buildTreeFromFile(filepath: str) -> Item:
    head = Item('/', 0)
    current_directory = head
    with open(FILEPATH) as f:
        for line in f.readlines():
            line = line.strip()

            if line.startswith('$ ls') or line.startswith('dir ') or line.startswith('$ cd /'):
                continue

            if line.startswith('$ cd'):
                cd_target = line.lstrip('$ cd ')

                if cd_target == '..':
                    current_directory = current_directory.parent
                    continue

                new_directory = Item(cd_target, 0, current_directory)
                current_directory.add(new_directory)
                current_directory = new_directory
                continue
            
            file_size_str, file_name = line.split()
            new_file = Item(file_name, int(file_size_str), current_directory)
            current_directory.add(new_file)
    
    return head

head = buildTreeFromFile(FILEPATH)
directories = deque([head])
target_size = 100_000
total = 0
while directories:
    curr = directories.popleft()
    if curr.size < target_size:
        total += curr.size
    
    for item in curr.items:
        if not item.isFile():
            directories.append(item)

print(total)
