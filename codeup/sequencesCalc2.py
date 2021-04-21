def sequencesCalc2(input):
    sequences = input.split()
    startNo = int(sequences[0])
    diff = int(sequences[1])
    seq = int(sequences[2])
    print(str(pow(diff,(seq-1)) * startNo))

if __name__ == "__main__":
    sequencesCalc2(input())