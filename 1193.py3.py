inNum = int(input());
offset = 1;
addCnt = 0;
i = 0;
while (i < inNum):
	addCnt += offset;
	i += addCnt;
if(addCnt%2 ==0 ):
	print (str(inNum-(i-addCnt))+'/'+str(addCnt-(inNum-(i-addCnt))+1));
else:
	print (str(addCnt-(inNum-(i-addCnt))+1)+'/'+str(inNum-(i-addCnt)));
