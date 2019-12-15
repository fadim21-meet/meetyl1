#lass person(object):
#	def __init__(self,name,age,city,gender,food):
#		self.name = name
#		self.age = age
#		self.city = city
#		self.gender = gender
#		self.sport = sport
#	def breakfast(self, fav_breakfast):
#		print(self.name +" is eating "+ fav_breakfast )
#	def play_videogames(self):
#		print(self.name +" is playing"+ss)




class post():
	def __init__(self ,name ,caption ,comment=[] ):
		self.name = name
		self.caption = caption 
		self.comment = []
	def add_caption (self,caption_text):
		self.caption_text = caption_text
		self.caption.append(caption_text)
		print(self.name + " has added the caption" + caption_text)
	def add_comment (self,comment_text):
		self.comment_text = comment_text
		self.comment.append(comment_text)
		print(self.name + " has added the comment" + comment_text)
	def like_post(self):
		print(self.name + " has liked your post ")




















