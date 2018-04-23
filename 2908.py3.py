inStr = input();

strLst = inStr.split();

firNo = strLst[0];

secNo = strLst[1];

def printRvs(strX):
	for j in range(2,-1,-1):
		print(strX[j],end='');
	
def compareNoRec(i,firNo,secNo):
	if(int(firNo[i])-int(secNo[i])<0):
		printRvs(secNo);		
	elif(int(firNo[i])-int(secNo[i])>0):
		printRvs(firNo);
	else:
		i -= 1;
		compareNoRec(i,firNo,secNo);

compareNoRec(2,firNo,secNo);
