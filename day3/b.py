import string

priorities = {}

# 1 - 26
start = 1
for i in range(len(string.ascii_lowercase)):
    ch = string.ascii_lowercase[i]
    priorities[ch] = start + i

# 27 - 52
start = 27
for i in range(len(string.ascii_uppercase)):
    ch = string.ascii_uppercase[i]
    priorities[ch] = start + i


with open("input.txt", "r") as f:
    lines = f.readlines()

    total_sum = 0
    for i in range(0, len(lines), 3):
        l1, l2, l3 = lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()

        intersection = set(l1).intersection(l2).intersection(l3)

        for el in intersection:
            total_sum += priorities[el]

    print(total_sum)

