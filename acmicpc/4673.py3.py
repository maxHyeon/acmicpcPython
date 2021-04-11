def getSumNumber(n):
	if (n<10000 and n>=1000):
		return n + int(n/1000) + (int(n/100)%10) + (int(n/10)%10) + (n%10);
	elif (n<1000 and n >= 100):
		return n +  int(n/100) + (int(n/10)%10) + (n%10);
	elif ( n<100 and n >= 10):
		return n + int(n/10) + (n%10);
	elif (n<10) :
		return n + n ;
	else:
		return 0;
	
def insSumNumToList ():
	sList = list();
	for i in range(1,10001):
		sList.insert(i,0);
	for i in range(1,10000):
		if (getSumNumber(i) <10000):
			sList[getSumNumber(i)] = getSumNumber(i);				
	return sList;

def printSelfNumber (sList):
	for i in range(1,10000):
		if (sList[i]==0):
			print(i);

		
a = list() ; 
a = insSumNumToList();
printSelfNumber(a);
