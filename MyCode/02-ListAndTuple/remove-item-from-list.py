# use remove() method to remove an item from a list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # 移除值为3的元素
print(my_list)  # 输出: [1, 2, 4, 5]

# use pop() method to remove an item from a list
my_list = [1, 2, 3, 4, 5]
my_list.pop(2)  # 移除索引为2的元素
print(my_list)  # 输出: [1, 2, 4, 5]

# use del statement to remove an item from a list
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # 移除索引为2的元素
print(my_list)  # 输出: [1, 2, 4, 5]

# use list comprehension to remove an item from a list
my_list = [1, 2, 3, 4, 3, 5]
my_list = [x for x in my_list if x != 3]  # 移除所有值为3的元素
print(my_list)  # 输出: [1, 2, 4, 5]