#函数
def greet_user(username):
	"""显示简单的问候语"""
	print("hello "+username)

greet_user('shell')

#关键字实参
def describle_pet(animal_type,pet_name):
	"""显示宠物的信息"""
	print("\n I have a " + animal_type +".")
	print("my " + animal_type + "'s name is " + pet_name.title() + ".")

describle_pet(animal_type = 'hamster',pet_name = "harry")

