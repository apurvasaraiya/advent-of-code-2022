def getSlots(line):
    [elf1, elf2] = line.split(",")

    [s1, e1] = elf1.split("-")
    [s2, e2] = elf2.split("-")

    s1, s2, e1, e2 = int(s1), int(s2), int(e1), int(e2)

    return set(range(s1, e1+1)), set(range(s2, e2+1))


with open("input.txt", "r") as f:
    lines = f.readlines()

    runningCounter = 0
    for line in lines:
        slot1, slot2 = getSlots(line.strip())

        if slot1.intersection(slot2):
            runningCounter += 1

    print(runningCounter)