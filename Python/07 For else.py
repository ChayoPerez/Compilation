print("SECTION 1: For Else\n-----------------")


nums = [12,16,18,21,24]

for num in nums:

   if num % 5 == 0:
      print(num)
else:
   print("This is printed because the for ended naturally")
# prints Not found only 

print("--------------")

for num in nums:

   if num % 5 == 0:
      print(num)
   if num == 18:
   	  print("Number is 18.")
   	  break
else:
   print("This is NOT printed because it ended on a break")