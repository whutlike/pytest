# def my_function():
# 	print('hello world!')
	
# my_function()
# my_function()

# def add(a, b):
# 	print('Calculating...')
# 	return a + b # 函数返回数值语句


# result = add(3, 5)
# print(f'The result is {result}.')

def my_func(n):
	return lambda a: a * n
mytripler = my_func(3)
print(mytripler(50))