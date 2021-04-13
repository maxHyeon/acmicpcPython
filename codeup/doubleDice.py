def calNumCase(input):
    dices = input.split()
    firstDice = int(dices[0])
    secDices = int(dices[1])

    for i in range(1,firstDice+1):
        for j in range(1,secDices+1):
            print (str(i)+' '+str(j))
            j += 1
        i += 1

if __name__ == "__main__":
    calNumCase(input())