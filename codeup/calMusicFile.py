def calMusicFile(input):
    infos = input.split()
    hzZ = float(infos[0])
    checkBits = float(infos[1])
    tracks = float(infos[2])
    recordSec = float(infos[3])

    print(str(round(((hzZ*checkBits*tracks*recordSec)/8/1024/1024),1))+" MB")

if __name__ == "__main__":
    calMusicFile(input())