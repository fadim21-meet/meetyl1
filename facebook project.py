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
		print(self.name + " has added " + email )

	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name + " has removed " + email + " from friends_list " )

	def post(self,text):
		print(self.name + " has posted : " + text )

	def get_userInfo(self):
		print(" name " + self.name )
		print(" email " + self.email )
		print(" password " + self.password )
		print(" friends " + str(self.friends_list) )
		print("posts" + str(self.post) )

user1 = User("Fadi","fadithebeast@gmail.com","fadithebeast@@##"," som3a "," how are you ")
user2 = User("trevor","trevorlinkolen@gmail.com","trevorlinkolen100%"," aljabra "," no pain no gain ")

user1.add_friend("thebeast@gmail.com") 

user1.post(" hello friends ")

user1.get_userInfo()
user2.get_userInfo()

user1.remove_friend("thebeast@gmail.com")


class post(object):
	def __init__(self,num_likes,num_comments):

		self.num_likes = 0
		self.num_comments = 0
		
	
