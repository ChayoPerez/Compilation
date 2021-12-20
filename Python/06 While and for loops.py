print("SECTION 1: While condition\n-----------------")

index = 0
while index < 10:
   print(index)
   index += 1


print("\n\nSECTION 2: Break\n-----------------")

index2 = 0
while True:
   print(index2)
   index2 += 1
   if index2 >= 10:
      break # the loop stops


print("\n\nSECTION 3: Continue\n-----------------")

# Continue skips what is under it and begins the loop again (if the condition permits it)
index3 = 0
while True:
   if index3 == 0:
      index3 += 1
      continue # skips printing number 0
   print(index3)
   index3 += 1
   if index3 == 5:
      break # stops after printing 4



print("\n\nSECTION 4: for x in array\n-----------------")


supermarket_list = ["apples", "cereal", "tofu", "detergent", "toothpaste"]
for item in supermarket_list:
   print(item)


print("\n\nSECTION 5: for x in range\n-----------------")

for i in range(len(supermarket_list)): # The for doesn't reach the 5 (length of the array)
   print(supermarket_list[i])

print("---------")

for i in range(3, len(supermarket_list)): # The for starts in index 3
   print(supermarket_list[i])
# Prints only detergent and toothpaste
# which are the indexes 3 and 4 (len - 1)


print("\n\nSECTION 6: for _ in range\n-----------------")
# Sometimes we don't need the index or the element
# We just want to loop

for _ in range(3):
   print(":)")