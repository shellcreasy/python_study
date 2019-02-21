#字典
alien = {'color':'green','points':5}
print(alien)
print(alien['color'])

#添加键值对
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

#修改字典的值
alien['color'] = 'yellow'
print(alien)

#删除键值对
del alien['points']
print(alien)

#遍历索引键值对
user = {
	'username':'efermi',
	'firname':'enrico',
	'lastname':'fermi',
}
for key,value in user.items():
	print("\nkey:"+key)
	print("value:"+value)

#遍历所有键
for key in user.keys():
	print("\n key:" + key)

#遍历所有值
for value in user.values():
	print("\n value:"+value)
	
#去重
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	
}
print("the following language have been mentioned")
for language in set(favorite_languages.values()):
	print("language is :" + language)
