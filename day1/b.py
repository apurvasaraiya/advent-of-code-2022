with open("input.txt", "r") as f:
    lines = f.readlines()
    
    calories = []
    runningSum = 0
    for line in lines:
        l = line.strip()

        if l == "":
            runningSum = 0
            continue

        runningSum += int(l)

    calories.append(runningSum)
    calories.sort(reverse=True)


    print(calories[:3])
    print(sum(calories[:3]))
