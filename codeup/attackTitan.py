def inputLines(lineAmount):
    lines=[]
    for i in range(0,int(lineAmount)):
        lines.append(input())
    return lines
def attackTitan(n):
    solids = inputLines(int(n))
    solidProducts = {}
    index = 0
    for i in solids:
        splited = i.split()
        if splited[0] not in solidProducts:
            solidProducts[int(splited[0])] = int(splited[1])
    for k,v in sorted(solidProducts.items()):
        print(str(k)+" "+str(v))
if __name__ == "__main__":
    attackTitan(input())