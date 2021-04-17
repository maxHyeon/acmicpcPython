def calImageFile(input):
    infos = input.split()
    r = float(infos[0])
    g = float(infos[1])
    b = float(infos[2])


    print(format(round(((r*g*b)/8/1024/1024),2),".2f")+" MB")

if __name__ == "__main__":
    calImageFile(input())