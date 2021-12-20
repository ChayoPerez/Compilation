print("SECTION 1: From string to bytes\n-----------------")

c1 = "abc"
encoded1 = c1.encode("ascii")
print(encoded1)
print("bytes:")
for element in encoded1:
	print(element)
print("-----")

b = b"abc"
for x in b:
	print(x)

print("\n\nSECTION 2: From bytes to string\n-----------------")
	
print()	
print("Reverse:")
print(encoded1.decode("ascii"))


print("\n\nSECTION 3: Ord(string length 1)\n-----------------")

c2 = "a"
print(c2)
print("ORD(int):")
print(ord(c2))


print("\n\nSECTION 4: From bytearray to a string\n-----------------")

array = bytearray()
for elemento in c1:
	array.append(ord(elemento))
print(array)
print(array[0:1])

print(array.decode("ascii"))



