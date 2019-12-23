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
print(x)



encoder_caesar =
{'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c',}
def mohammad(stringin):
	stringin=input("can you type anything?")
	print(encoder_caesar[stringin])

