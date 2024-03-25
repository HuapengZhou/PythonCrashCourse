# 定义一个列表
my_list = [3, 1, 4, 1, 5, 9, 2]

# 使用sorted函数排序
# sorted返回一个新的列表，原始列表不变
sorted_list = sorted(my_list)
print("使用sorted后的列表:", sorted_list)
print("原始列表仍然不变:", my_list)

# 使用sort方法排序
# sort会对原始列表进行就地排序，不返回任何值
my_list.sort()
print("使用sort方法后原始列表变为:", my_list)
