#遍历cars
cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#不相等 !=

#与 and

#或 or

#包含 in

#不包含 not in

#真 True

#假 False

#if-elife-else 结构
age = 12
if age < 4:
	print("your admission cost is $0")
elif age < 18:
	print("your admission cost is $5")
else:
	print("your admission cost is $10")
	
#Python并不要求if-elif结构后面必须有else代码块

#确定列表不是空的
requested_toppings = []
if requested_toppings:
	print("not null")
else:
	print("null")
