#取最后一个元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[-1])

#取元素、调用title方法
message = "My first bicycle was a " + bicycles[0].title()
print(message)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#修改元素
motorcycles[0] = 'ducati'
print(motorcycles)

#添加元素
motorcycles.append('toyota')
print(motorcycles)

#空列表添加元素
motorcycles1 = []
motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')
print(motorcycles1)

#列表中插入元素
motorcycles1.insert(0,'ducati')
print(motorcycles1)

#弹出末尾元素
poped_motorcycle = motorcycles1.pop()
print(motorcycles1)
print(poped_motorcycle)

#pop任意位置元素
print(motorcycles1.pop(1))
print(motorcycles1)

#根据值删除元素
motorcycles1.remove('ducati')
print(motorcycles1)

#按字母sort排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#按字母反向排序
cars.sort(reverse=True)
print(cars)

#使用sorted进行临时排序
print(sorted(cars))
print(cars)

#反转列表元素排列顺序
cars1 = ['bmw','audi','toyota','subaru']
cars1.reverse()
print(cars1)

#获取列表长度
print(len(cars1))
