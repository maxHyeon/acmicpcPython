from string import ascii_uppercase
alpbt = ascii_uppercase;
word = input();
uWord = word.upper();
cntLst = [];
def mkCntLst(inUWord):
	for a in alpbt:
		aCnt = inUWord.count(a);
		if (aCnt > 0 ):
			cntLst.append([a,aCnt]);
	return sorted(cntLst,reverse =True ,key =lambda alpbets: alpbets[1]);
alpbtCntLst = mkCntLst(uWord);
if (len(alpbtCntLst)==1):
	print(alpbtCntLst[0][0]);
else :	
	if (int(alpbtCntLst[0][1]) == int(alpbtCntLst[1][1])):
		print ('?');
	else:
		print (alpbtCntLst[0][0]);
