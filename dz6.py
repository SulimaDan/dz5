# num1 = int(input("Enter the start of the range: "))
# num2 = int(input("Enter the end of the range: "))
    
# for i in range(num1, num2 + 1):
#     if i % 7 == 0:
#         print(i)




# num1 = int(input("Enter the start of the range: "))
# num2 = int(input("Enter the end of the range: "))

    
# print("All numbers in the range:")
# for i in range(num1, num2 + 1):
#     print(i, end=" ")
# print()
    
    
# print("All numbers in descending order:")
# for i in range(num2, num1 - 1, -1):
#     print(i, end=" ")
# print()

    
# print("All numbers that are multiples of 7:")
# for i in range(num1, num2 + 1):
#     if i % 7 == 0:
#         print(i, end=" ")
#         print()


# count = 0
# for i in range(num1, num2 + 1):
#     if i % 5 == 0:
#         count += 1
# print(f"The number of numbers that are multiples of 5: {count}")




start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)