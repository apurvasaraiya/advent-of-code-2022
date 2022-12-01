import heapq

input_file = "input.txt"

def getTopNSum(calories, N):
    return -sum(calories[:N])

with open(input_file, "r") as f:
    lines = f.readlines()
    calories = []
    heapq.heapify(calories)

    runningSum = 0
    for line in lines:
        l = line.strip()

        if l == "":
            heapq.heappush(calories, -runningSum)
            runningSum = 0
            continue

        runningSum += int(l)

    heapq.heappush(calories, -runningSum)

    ans1 = getTopNSum(calories, 1)
    ans2 = getTopNSum(calories, 3)

    # print(calories)
    print(ans1)
    print(ans2)