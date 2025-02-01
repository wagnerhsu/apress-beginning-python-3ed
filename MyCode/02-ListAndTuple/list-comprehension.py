# Description: 列表推导式

squares = [x**2 for x in range(1, 11)]
print(squares)  # 输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表推导式中的if语句
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # 输出: [2, 4, 6, 8, 10]

# 将一个字符串中的每个字符转换为大写
uppercase_chars = [char.upper() for char in "hello"]
print(uppercase_chars)  # 输出: ['H', 'E', 'L', 'L', 'O']

my_list = [1, 2, 3, 4, 3, 5]
my_list = [x for x in my_list if x != 3]  # 移除所有值为3的元素
print(my_list)  # 输出: [1, 2, 4, 5]