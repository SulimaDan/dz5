# number1 = float(input("Введіть перше число: "))
# number2 = float(input("Введіть друге число: "))
# number3 = float(input("Введіть третє число: "))
# choice = input("Введіть 'summa' для обчислення суми або 'dobutok' для обчислення добутку: ")

# if choice == 'summa':
#     result = number1 + number2 + number3
#     print("Сума чисел:", result)
# elif choice == 'dobutok':
#     result = number1 * number2 * number3
#     print("Добуток чисел:", result)
# else:
#     print("Помилка: некоректний вибір. Введіть 'summa' або 'dobutok'.")







# number1 = float(input("Введіть перше число: "))
# number2 = float(input("Введіть друге число: "))
# number3 = float(input("Введіть третє число: "))

# print("Виберіть опцію:")
# print("1. Максимум із трьох чисел")
# print("2. Мінімум із трьох чисел")
# print("3. Середньоарифметичне трьох чисел")
# choice = input("Введіть номер опції (1, 2 або 3): ")

# if choice == '1':
#     result = max(number1, number2, number3)
#     print("Максимум із трьох чисел:", result)
# elif choice == '2':
#     result = min(number1, number2, number3)
#     print("Мінімум із трьох чисел:", result)
# elif choice == '3':
#     result = (number1 + number2 + number3) / 3
#     print("Середньоарифметичне трьох чисел:", result)
# else:
#     print("Помилка: некоректний вибір. Введіть 1, 2 або 3.")






METERS_TO_MILES = 0.000621371
METERS_TO_INCHES = 39.3701
METERS_TO_YARDS = 1.09361
meters = float(input("Введіть кількість метрів: "))

print("Виберіть опцію конвертації:")
print("1. Конвертувати в милі")
print("2. Конвертувати в дюйми")
print("3. Конвертувати в ярди")
choice = input("Введіть номер опції (1, 2 або 3): ")

if choice == '1':
    result = meters * METERS_TO_MILES
    print(f"{meters} метрів дорівнює {result} миль")
elif choice == '2':
    result = meters * METERS_TO_INCHES
    print(f"{meters} метрів дорівнює {result} дюймів")
elif choice == '3':
    result = meters * METERS_TO_YARDS
    print(f"{meters} метрів дорівнює {result} ярдів")
else:
    print("Помилка: некоректний вибір. Введіть 1, 2 або 3.")
