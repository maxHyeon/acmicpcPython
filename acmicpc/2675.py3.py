line = int(input());
inStrs = [];
for i in range(0,line):
	inStr = input();
	inStrs.append(inStr.split(' '));

def printRept(rep,inChr):
	for j in range(0,rep):
		print(inChr,end='');

for t in inStrs :
	for c in t[1]:
		printRept(int(t[0]),c);
	print();
