# day= {
#     1: "понеділок",
#     2: "вівторок",
#     3: "середа",
#     4: "четвер",
#     5: "п'ятниця",
#     6: "субота",
#     7: "неділя"
# }
# day_number = int(input("Введіть номер дня тижня (1-7): "))

# if day_number in day:
#     print("День тижня:", day[day_number])
# else:
#     print("введіть число від 1 до 7!!!")


# months = {
#     1: "січень",
#     2: "лютий",
#     3: "березень",
#     4: "квітень",
#     5: "травень",
#     6: "червень",
#     7: "липень",
#     8: "серпень",
#     9: "вересень",
#     10: "жовтень",
#     11: "листопад",
#     12: "грудень"
# }
# month_number = int(input("Введіть номер місяця (1-12): "))

# if month_number in months:
#     print("Місяць:", months[month_number])
# else:
#     print("введіть число від 1 до 12!!!")




# number = float(input("Введіть число: "))

# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")


number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))

if number1 == number2:
    print("Числа є рівними")
else:

    if number1 < number2:
        print("Числа у порядку зростання:", number1, number2)
    else:
        print("Числа у порядку зростання:", number2, number1)

