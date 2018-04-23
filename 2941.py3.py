inStr = input();

corAlpbtDic = {'c=':1,'c-':1,'dz=':1,
          'd-':1,'lj':1,'nj':1,
          's=':1,'z=':1};
wordLen = 0 ;
skipCnt = 0;
for i in range(0,len(inStr)):
	if(skipCnt>0):
		skipCnt -= 1;
		continue;
	if( i+1<len(inStr) and inStr[i] != 'd' ):
		if(corAlpbtDic.get(inStr[i]+inStr[i+1]) is not None): wordLen+=1; skipCnt = 1; 
		else: wordLen += 1;
	elif(i+1<len(inStr) and inStr[i] == 'd'):
		if(i+2<len(inStr) and corAlpbtDic.get(inStr[i]+inStr[i+1]+inStr[i+2]) is not None): wordLen+=1;  skipCnt =2;
		elif(corAlpbtDic.get(inStr[i]+inStr[i+1]) is not None):wordLen+=1; skipCnt =1;
		else: wordLen += 1;
	else:
		wordLen += 1;

print (wordLen);
