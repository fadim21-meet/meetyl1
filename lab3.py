class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat (self,food):
		print("yummy!!"+ self.name + "is eating"+ food)
	def description(self):
		print(self.name + "is" + str(self.age) + "years old and loves the color"+ self.favorite_color)
	def make_sound(self):
		print("the sound is "+self.sound)
cat = Animal("meow","citty",9,"red")
cat.eat("food")
cat.description()
cat.make_sound()

