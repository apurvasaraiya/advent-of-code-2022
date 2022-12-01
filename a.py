with open("input.txt", "r") as f:
    lines = f.readlines()
    
    maxSum = 0
    runningSum = 0
    for line in lines:
        l = line.strip()

        if l == "":
            maxSum = max(maxSum, runningSum)
            runningSum = 0
            continue

        runningSum += int(l)

    maxSum = max(maxSum, runningSum)
    print(maxSum)
        