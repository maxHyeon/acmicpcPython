import datetime
class schedule:
    def __init__(self,title,date):
        self.title = title
        self.date = date

def multiLineInputProc(lineAmount):
    inputs=[]
    for i in range(int(lineAmount)):
        inputs.append(input())
    return inputs

def splitData(rawData,index):
    return rawData.split(' ',index)

def strToDate(str):
    proceedDate = datetime.datetime.strptime(str, "%Y %m %d")
    return proceedDate

def procInputs(inputs):
    proceedInputs = []
    splitIndex = 1
    for i in inputs:
        proceedInputs.append(splitData(i,splitIndex))
    return proceedInputs

def mkSchedule(proceedInputs):
    schedules = []
    for i in proceedInputs:
        schedules.append(schedule(i[0],strToDate(i[1])))
    return schedules

def main(input):
    print ( procInputs(multiLineInputProc(input)) )

if __name__ == "__main__":
    main(input())