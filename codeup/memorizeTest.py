def procInput(valRange) : 
    valList = list(map(int,valRange.split()))
    passageRange = valList[0]
    questionRange = valList[1]
    passage = {}
    for i in range(0,passageRange):
        passage = passageProc(splitRaw(input()),passage)
    for i in range(0,questionRange):
        printAnswer(input(),passage)
def passageProc(passageData,passage):
    if passageData[0] in passage:
        passage[passageData[0]] += int(passageData[1])
    else :
        passage[passageData[0]] = int(passageData[1])
    return passage

def splitRaw(rawData):
    return rawData.split()

def printAnswer(question,passage):
    if question in passage :
        print(passage[question])
    else :
        print('0')
    
if __name__ == "__main__" :
    procInput(input())