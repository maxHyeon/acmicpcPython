def checkGroupWord(word):
	tmpChr = set();
	for i in range(1,len(word)):
		if (word[i] != word[i-1]):
			tmpChr.add(word[i-1]);
		if (word[i] in tmpChr):
			return 0;
	return 1;
line = int(input());
words = [];
cnt =0 ;
for i in range(0,line):
	cnt += checkGroupWord(input());
print (cnt);
