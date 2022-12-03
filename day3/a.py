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
    for line in lines:
        l = line.strip()
        cut = len(l)//2
        first_half, second_half = l[:cut], l[cut:]
        intersection = set(first_half).intersection(set(second_half))
        for el in intersection:
            total_sum += priorities[el]

    print(total_sum)

    