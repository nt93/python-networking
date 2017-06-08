def breaktest(arr) :
	for i in arr :
		if i == 5 :
			break
		print(i)
	print()

arr=[1,2,3,4,5,6,7]

breaktest(arr)
m=[[1,2],[3,4],[5,6]]

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

for i in rez:
	print(i,end=',',sep='-')