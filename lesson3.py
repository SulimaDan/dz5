#c = 5
# while c>0:
#     print("hello,world!")
#     c-=1

# i = 2
# for i in range(0,5,3):
#     if i == 2:
#         break
#     print(f"I'm {i} house now")

# print("I'm out of the loop")


# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
# range_num1 = min(num1, num2)
# range_num2 = max(num1, num2)

# print("Числа у вказаному діапазоні:")
# for number in range(range_num1, range_num2 + 1):
#     print(number)


# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
# range_num1 = min(num1, num2)
# range_num2 = max(num1, num2)
# print("Непарні числа у вказаному діапазоні:")
# for number in range(range_num1, range_num2 + 1):
#     if number % 2 != 0:
#         print(number)

# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
# range_num1 = min(num1, num2)
# range_num2 = max(num1, num2)
# print("Непарні числа у вказаному діапазоні:")
# for number in range(range_num1, range_num2 + 1):
#     if number % 2 == 0:
#         print(number)

# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))

# range_num1 = min(num1, num2)
# range_end = max(num1, num2)

# print("Числа у вказаному діапазоні в порядку від більшого до меншого:")
# for number in range(range_end, range_num1 - 1, -1):
#     print(number)





# start = int(input("Введіть перше число: "))
# end = int(input("Введіть друге число: "))

# range_start = min(start, end)
# range_end = max(start, end)

# print("Непарні числа у вказаному діапазоні в порядку від більшого до меншого:")
# for number in range(range_end, range_start - 1, -1):
#     if number % 2 != 0:
#         print(number)







# start = int(input("Введіть перше число: "))
# end = int(input("Введіть друге число: "))


# range_start = min(start, end)
# range_end = max(start, end)


# sum_of_numbers = 0
# count_of_numbers = 0

# for number in range(range_start, range_end + 1):
#     sum_of_numbers += number
#     count_of_numbers += 1

# average = sum_of_numbers / count_of_numbers if count_of_numbers != 0 else 0


# print(f"Сума чисел у вказаному діапазоні: {sum_of_numbers}")
# print(f"Середньоарифметичне чисел у вказаному діапазоні: {average}")










# number = int(input("Введіть число: "))

# def factorial(n):
#     if n < 0:
#         return "Факторіал не визначений для від'ємних чисел"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result

# fact = factorial(number)

# print(f"Факторіал числа {number} дорівнює {fact}")







# length = int(input("Введіть довжину лінії: "))

# line = '*' * length

# print(line)





# length = int(input("Введіть довжину лінії: "))

# symbol = input("Введіть символ для заповнення лінії: ")

# line = symbol * length

# print(line)





# number = int(input("Введіть число: "))

# print(f"Таблиця множення для числа {number}:")

# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")


