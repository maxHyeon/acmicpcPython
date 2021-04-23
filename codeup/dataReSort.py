def inputLines(lineAmount):
    lines=[]
    for i in range(0,int(lineAmount)):
        lines.append(input())
    return lines
def dataReSort(input):
    data = {}
    index = 0
    for i in sorted(list(map(int,(input[1]).split()))):
        data[int(i)] = index
        index += 1
    for i in list(map(int,(input[1]).split())):
        print(data[i],end=' ')
if __name__ == "__main__":
    dataReSort(inputLines(2))