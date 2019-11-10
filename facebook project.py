class User():
	def __init__(self,name,email,password):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list=[]
		self.posts =[]
	def add_friend(self,email):
		print(self.name + " has added " + email )
	def remove_friend(self,email):
		self.friends_list.pop(email)
		print(self.name + " has removed " + email + " from friends_list " )
	def post(self,text):
		print(self.name + " has posted : " + text )
	def get_userInfo(self):
		print("name" + self.name )
		print("email" + self.email )
		print("password" + self.password )
		print("friends" + self.friends_list )
		print("posts" + self.post )
user1 = User("Fadi","fadithebeast@gmail.com","fadithebeast@@##")
user2 = User("trevor","trevorlinkolen@gmail.com","trevorlinkolen100%")
user1.add_friend("thebeast@gmail.com") 



