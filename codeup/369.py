import re
def print369(num):
    result = []
    for i in range(1,int(num)+1):
        result.append(cal369(i))
    for i in result:
        print(i,end=' ')

def cal369(num):
    if re.search('([3,6,9]+)', str(num)):
        return ("X")
    else :
        return (str(num))


if __name__ == "__main__":
    print369(input())