inNum = int(input());
offSet = 6;
sumNum = 0;
i=1;
jumpCnt = 1 ;
while(i < inNum):
	sumNum += offSet;
	i += sumNum ;
	jumpCnt += 1;	
print (jumpCnt);
