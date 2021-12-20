import os 
# To delete files


"""
open() has four uses 

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist, replaces if it exists
"x" - Create - Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)


"rt" is the default

"""

file = open("FileToRead.txt") # "rt" is default
print(file.read())
print(file.read())
print(file.read())
print(file.read())
print(file.read())
print(file.read())
print(file.read())
print(file.read())
print(file.read())

# It doesn't care how many times you call the function.
# Once it reaches the end it just returns nothing

print(file.readlines()) # There is nothing left to get.

# Never forget to close
file.close()


# If you want all the lines at once in an array then:
file2 = open("FileToRead.txt")
lines = file2.readlines()
print(lines)

# We hit a problem here. We don't want the \n at the end of our lines
# And we don't want the first line either since it's the title
# We fix it:

def clean_info(file_array):
	fixed_lines = []
	for line in file_array:
	    if line == "Shopping list:\n":
	        continue
	    if line[-1] == "\n":
	        line = line[0:len(line)-1]
	    fixed_lines.append(line)
	return fixed_lines


print(clean_info(lines)) # There!
file2.close()

# So you don't have to close, you wan use 'with'

with open("FileToRead.txt") as file3:
	clean_lines = clean_info(file3.readlines())
	print(clean_lines)


with open("FileToRead2.txt", 'w') as file4:
	array = ["Los Fracasados :", "Nada me sacaba de esta jaula de huesos y entrañas",
	"de heridas que aún no olvido", "Y de amigos que ya me olvidaron (...)"]
	for verse in array:
		file4.write(verse + "\n") # Write does not skip lines

with open("FileToRead2.txt", 'a') as file5:
	file5.write("\n(This is my favourite comic.)\n")


# This part is commented so you can see the file
# Uncomment to delete FileToRead2.txt

"""
print(os.path.exists("FileToRead2.txt"))
print(os.path.exists("FileToRead3.txt"))

if os.path.exists("FileToRead2.txt"):
	os.remove("FileToRead2.txt")
try:
	with open("FileToRead2.txt") as file6:
		print("'FileToRead2.txt' still exixts.")
except Exception:
	print("That file does no longer exist!")
"""