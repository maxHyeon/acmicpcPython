scores = [];
for j in range(5):
	score = int(input());
	if (score < 40):
		score = 40 ;
	scores.append(int(score));

total = 0 ;
for i in scores :
	total += i ;

print (int(total/5));