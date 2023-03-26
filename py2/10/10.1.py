from collections import Counter

with open('10/names.txt', 'r') as file:
    names = file.read().splitlines()

name_counts = Counter(names)

for name, count in name_counts.items():
    print(f"{name}: {count}")
