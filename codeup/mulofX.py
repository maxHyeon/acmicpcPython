def printResult(n,s):
    print("%d ~ 10 : %d" % (n, s))

def mulofX(n):
    for j in range (1,n+1,1):
        s = 0
        for i in range(1, 11, 1):
            if i % j == 0:
                s += i
        printResult(j,s)
    return s


if __name__ == "__main__":
    mulofX(int(input("1~10까지의 수를 입력하세요: ")))