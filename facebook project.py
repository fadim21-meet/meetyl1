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
		for x in posts:
			if(self.email==x.user):
				print("post:"+str(x.content))
	def get_userInfo(self):
		print(" name " + self.name )
		print(" email " + self.email )
		print(" password " + self.password )
		print(" friends " + str(self.friends_list) )
		print("posts" + str(self.post)