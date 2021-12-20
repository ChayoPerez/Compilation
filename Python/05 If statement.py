print("SECTION 1: Booleans are used in conditions\n-----------------")


condition1 = False

if condition1:
	print("The condition1 is True")
if not condition1:
   print("The condition1 is False")    

condition2 = 2 > 1 # True

if condition1 and condition2:
   print("Both conditions are true")
elif condition2 or condition1:
   print("One condition is true")
else:
   print("No condition is true")
