#遍历列表
magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician.title() + ",that was a great trick!")
	print("i can't wait to see your next trick," + magician.title() + "\n")
print("Thank you,everyone,that was a wonderful magic show")

#range函数生成数字
for value in range(1,5):
	print(value)

#使用range()创建数字列表
numbers = list(range(1,6))
print(numbers)

#range函数指定步长
numbers1 = list(range(2,11,2))
print(numbers1)

#range函数生成1-10的平方数字列表
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

#数字列表统计函数
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
squares1 = [value**2 for value in range(1,11)]
print(squares1)

#列表切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])

#没有开始索引
print(players[:4])

#没有结束索引
print(players[2:])

#遍历切片
for player in players[:3]:
	print(player.title())

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#元组：不可变的列表
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#遍历元组
for dimension in dimensions:
	print(dimension)
	
#修改元组
dimensions = (250,50)
for dimension in dimensions:
	print(dimension)
