def sequencesCalc(input):
    sequences = input.split()
    startNo = int(sequences[0])
    diff = int(sequences[1])
    seq = int(sequences[2])
    print(str(diff * (seq-1) + startNo))

if __name__ == "__main__":
    sequencesCalc(input())