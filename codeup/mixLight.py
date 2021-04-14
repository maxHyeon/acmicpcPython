def mixLight(input):
    rgb = input.split()
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])

    for i in range(r):
        for j in range(g):
            for k in range(b):
                print (str(i)+' '+str(j)+' '+str(k))
                k += 1
            j += 1
        i += 1
    print (str(r*g*b))
if __name__ == "__main__":
    mixLight(input())