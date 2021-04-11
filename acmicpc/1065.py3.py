a = int(input());


def checkArithSeq (strN) : 
	diff = list() ;
	for i in range(0,len(strN)-1):
		diff.insert(i,(int(strN[i]) - int(strN[i+1])));

	for i in range(0,len(diff)-1) :
		if (diff[i]-diff[i+1] != 0 ):
			return False;
	return True; 
def countArithNum (rangeN):
	cnt = 0;
	for i in range(1,a+1):
		if (checkArithSeq(str(i))==True):
			cnt += 1 ;
	return cnt;


print(countArithNum(10));