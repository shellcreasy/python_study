#读取文件
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
	
#逐行读取文件
with open('pi_digits.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
#写文件
filename = 'programming.txt'
with open(filename,'w') as file_object:
	file_object.write('i love programming.\n')
	file_object.write('i love creating new games\n')
	
with open(filename,'a') as file_object:
	file_object.write('i love you.\n')
	
try:
	print(5/1)
	answer = 1
except ZeroDivisionError:
	print('you can not divide by zero!')
else:
	print(answer)
	
	
	

