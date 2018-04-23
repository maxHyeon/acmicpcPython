from string import ascii_lowercase 

alpbts = list(ascii_lowercase) 

a = input() 
# print (alpbts);

for i in range(len(alpbts)): 

   print(a.find(alpbts[i]), end=' ');