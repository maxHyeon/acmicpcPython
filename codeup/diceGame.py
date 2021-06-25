#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import random
def diceGame(input):
    gamers = input
    gamerResultList = []
    for i in range(0,gamers):
        gameResult = 0
        for i in range(0,2):        
            gameResult += random.randrange(1,6)
        gamerResultList.append(gameResult)
    gameResultDict = {i : gamerResultList[i] for i in range(len(gamerResultList))}
    sortDict = sorted(gameResultDict.items(),key =(lambda x:x[1]),reverse=True)
    print("게임 결과: (플레이어, 결과값)")
    print(sortDict)
    print("우승자")
    print(sortDict[0])


if __name__ == "__main__":
    diceGame(input("게임의 인원수를 입력하세요 : "))
