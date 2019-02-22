class Dog():
	"""一次模拟小狗的简单尝试"""
	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
	
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + "rolled over.")
		
my_dog = Dog('willie',6)
your_dog = Dog('luck',3)
	
print(my_dog.sit())
print('my dog name is ' + my_dog.name)

class Dog1(Dog):
	"""继承"""
	def __init__(self, name, age):
		"""初始化父类属性"""
		super().__init__(name,age)

my1_dog = Dog1('继承狗',1)
print(my1_dog.sit())
		
	
