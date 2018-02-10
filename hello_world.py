print ("hello world")
n= 1000
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)

total=0
n1=1000
for i in range(n1+1):
	total=total+i
print(total)


s="hello world hi "

s1=s.replace(' ','%20')
print(s1)


s2='%20'.join(s.split(' '))
print(s2)

a=[]

for i in range(len(s)):
	print()