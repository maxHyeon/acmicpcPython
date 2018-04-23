oxs = int(input());

def countScore (ans):
	score  = 0 ;
	bonus = 0 ;
	for i in ans :
		if (i == 'O'):
			bonus += 1;
			score += bonus;
		elif (i =='X'):
			bonus = 0;

	return score;

for i in range(0,oxs):
	ans = input();
	print (countScore(ans));