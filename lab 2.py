list1 = [6,22,64,233]
list2 = [22,6,73,383]
list3 = [57,6,32,435]
def creat_fun(l1,l2):
	x=[]
	for num in l1:
		if num in l2:
			x.append(num)
	return (x)
x = creat_fun(list1,list2)
for num2 in x:
	
print(x)
