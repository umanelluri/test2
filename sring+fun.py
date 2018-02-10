a="hello world!123"

def let_dig(a):
	l=d=0
	for i in range(len(a)):
		if a[i].isalpha():
			l=l+1
		
		elif a[i].isdigit():
			d=d+1
	print('letters are',l,'\n','digits are',d)
let_dig(a)			
			

