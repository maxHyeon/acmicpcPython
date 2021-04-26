class Score:
    def __init__(self):
        self.lineAmount = 0
        self.printAmount = 0
        self.scores = []

def procInputs(dataSize):
    metaData = list(map(int,dataSize.split()))
    score = Score()
    score.lineAmount = metaData[0]
    score.printAmount = metaData[1]
    for i in range(list(map(int,dataSize.split())).pop(0)):
        score.scores.append(list(map(lambda x: int(x) if x.isdigit() else x, input().split())))
    return score

def scoreSort(scores,sortKey,reverse):
    return sorted(scores,key=lambda input: (input[sortKey-1],input.index(input[0])),reverse=reverse)

def printScoreBoard(inputs):
    sortedScore = scoreSort(inputs.scores,2,True)
    for i in range(inputs.printAmount):
        print(sortedScore[i][0])

if __name__ == "__main__":
    printScoreBoard(procInputs(input()))