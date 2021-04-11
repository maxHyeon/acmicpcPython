import math
def makeMap (height):
	map = [[' ' for rows in range(height*2)]for cols in range(height)];
	return map;

def rcrsStar (map,x,y,h,offset):
	
	pad = offset -y ;
	if(h==3):
		map[y][x+pad] = '*';
		pad = pad -1 ;
		map[y+1][x+pad] = '*';
		map[y+1][x+pad+2] = '*';
		pad = pad-1;
		for i in range (0,5) :
			map[y+2][x+i+pad] = "*";

	else:
		rcrsStar(map,x+h,int(y+h/2),int(h/2),offset);
		rcrsStar(map,x,int(y+h/2),int(h/2),offset);
		rcrsStar(map,x,y,int(h/2),offset);
	return map	;

def printStar (map):
	for i in range(0,len(map)):
		if(i!=len(map)-1):
			for j in range(0,len(map)*2-1):
				if (j!=len(map)*2) :print(map[i][j],end="");
			else : print(map[i][j]);
		else:
			for j in range(0,len(map)*2-1):
				if (j!=len(map)*2-1) :print(map[i][j],end="");
			else : return('');
def printMap (map):
	s = '';
	for i in range(0,len(map)):
		if(i!=len(map)-1):
			print(s.join(map[i]));
		else:
			for j in range(0,len(map)*2-1):
				if (j!=len(map)*2-1) :print(map[i][j],end="");
			else : return('');


a = int(input());

# print (printStar(rcrsStar(makeMap(a),0,0,a,a-1)));
print (printMap(rcrsStar(makeMap(a),0,0,a,a-1)));
