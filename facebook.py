users = []
posts = []

class post(object):
	def __init__(self,name,date,content):

		self.name = name
		self.date = date
		self.content = content

class User():
	def __init__(self,name,email,password,friends_list,posts):

		friends_list = []
		posts = []
		self.name = name
		self.email = email
		self.password = password
		self.friends_list=[]
		self.posts =[]
	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as a friend ")

	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name + " has removed " + email + " from friends_list " )

	
	def post(self,text):
		print(self.name + " has posted : " + text )
		post1 = post("som3a","30/8/1240","far3on pyrimid")
		self.posts.append(post1)	

	def get_userInfo(self):
		print(" name " + self.name )
		print(" email " + self.email )
		print(" password " + self.password )
		print(" friends " + str(self.friends_list) )
		print("post" + str(self.post))


user1 = User("Fadi","fadithebeast@gmail.com","fadithebeast@@##"," som3a "," how are you ")
user2 = User("trevor","trevorlinkolen@gmail.com","trevorlinkolen100%"," aljabra "," no pain no gain ")

user1.add_friend("som3aya5ali@gmail.com") 
user1.post(" FBI open up ")
user1.get_userInfo()
user1.remove_friend("som3aya5ali@gmail.com")
print(users)


user2.add_friend(" justsul@gmail.com ") 
user2.add_friend("amigo@gmail.com")
user2.post(" R.I.P amigos ")
user2.get_userInfo()
user2.remove_friend("amigo@gmail.com")
print(users)
