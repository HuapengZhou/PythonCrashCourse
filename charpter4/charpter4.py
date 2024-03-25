# 遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 创建数值列表
numbers = list(range(1, 6))
print(numbers)

# 简单统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 使用切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\\nMy friend's favorite foods are:")
print(friend_foods)

# 元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 循环结束后执行操作
print("Thank you, everyone. That was a great magic show!")

# 修改元组
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\\nModified dimensions:")
for dimension in dimensions:
    print(dimension)