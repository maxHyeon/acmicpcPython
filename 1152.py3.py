sent = str(input()).strip();

word = 1;
if (len(sent)<1 ) :
	word = 0;
else:
	for i in sent:
		if (i==' '):
			word = word+1;

print (word,end='');