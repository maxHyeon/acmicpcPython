class schedule:
    def __init__(self):
        self.title = ''
        self.date

def multiLineInputProc(lineAmount):
    inputs=[]
    for i in range(int(lineAmount)):
        inputs.append(input())
    return inputs

def splitData(rawData,index):
    return rawData.split(' ',index)

def procInputs(inputs):
    proceedInputs = []
    splitIndex = 1
    for i in inputs:
        proceedInputs.append(splitData(i,splitIndex))
    return proceedInputs

def main(input):
    multiLineInputProc(input)

if __name__ == "__main__":
    main(input())