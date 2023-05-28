def getdata(a):
	max1 = a[0]
	temp = a[0]
	for i in a:
		if i > max1:

			max1 = i
			temp = i

	print("The largest number is", temp)
	
	for i in a:
		if  i < max1:

			max1 = i
			temp = i

	print("The smallest number  is:", temp)
	
def sum(a):
	sum=0
	for i in a:
		sum+=i
	print(sum)




a=[1,2,3,4,5,6,7]
getdata(a)
sum(a)
