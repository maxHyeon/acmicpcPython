inStr = input();

def raiseFlag(inStr):
	diff = int(inStr[2]) - int(inStr[0]) ;
	if (diff < 0) :
		flag = -1 ;
	elif (diff > 0):
		flag = 1 ;
	return flag; 

# else 
# 	mixFlag = 1;

def scale(inStr,flag):
	for i in range (4,len(inStr)) :
		diff = 0;
		if (inStr[i] != ' '):
			diff = int(inStr[i]) - int(inStr[i-2]) ;
			if (diff < 0) :
				if (flag > 0 ):
					return 'mixed';
			elif (diff > 0):
				if (flag < 0 ):
					return 'mixed'
			# else 
			# 	if ()
			# 	mixFlag = 1;
	if (flag < 0 ):
		return 'descending'
	elif ( flag > 0):
		return 'ascending'

print(scale(inStr,raiseFlag(inStr)));