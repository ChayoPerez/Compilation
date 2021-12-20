print("SECTION 1: Recursion\n-----------------")

# Example: FACTORIALS

def factorial(actual_value, result=1):
   if actual_value == 1:
      return result
   else:
      return factorial(actual_value - 1, result * actual_value)

print(factorial(4))