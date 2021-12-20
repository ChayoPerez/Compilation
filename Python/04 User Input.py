print("SECTION 1: Using input()\n-----------------")

user_input1 = input("Give me a number 1: ")
user_input2 = input("Give me a number 2: ")
print(int(user_input1) + int(user_input2))


print("\n\nSECTION 2: Using eval\n-----------------")

result = eval(input("Enter expression: ")) # Enter for example 1 + 2
print(result)