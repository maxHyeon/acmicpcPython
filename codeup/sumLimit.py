def sumLimit(limitNum):
    i = 0
    sumIndex = 1
    while i < int(limitNum):
        i += sumIndex
        sumIndex += 1
    print (sumIndex-1)

if __name__ == "__main__":
    sumLimit(input())