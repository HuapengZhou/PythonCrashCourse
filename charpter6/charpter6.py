
# 定义和访问字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 添加键—值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 删除键—值对
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)

# 遍历所有的键—值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 遍历所有的键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

# 遍历所有的值
for language in favorite_languages.values():
    print(language.title())

# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
