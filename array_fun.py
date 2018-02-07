
def matrix_list(i,j):
	ai=[]
	for n in range(i):
		aj=[]
		for nj in range(j):
			aj.append(n)
		ai.append(aj)
	print(ai)
matrix_list(10,1)

