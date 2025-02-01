import re

def NumberAddition(s):
    numbers = re.findall(r'\d+', s)
    return sum(map(int, numbers))

inputs = [
    "88Hello 3World!",
    "10 2One Number1"
]

for inp in inputs:
    print(NumberAddition(inp))