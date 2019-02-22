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

#有返回值的函数
def get_formatted_name(first_name,last_name):
	"""返回整洁的名字"""
	full_name = first_name + ' ' + last_name
	return full_name.title() 

musician = get_formatted_name('jimi','hendrix')
print(musician)
