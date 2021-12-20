def a_random_function():
   print("This is am imported function")

print("Imported module")
print(__name__) # when opening "14 Modules.py" prints the name of the module
# When opening this file, it prints "__main__"


if __name__ == "__main__":
	print("Stuff that will only run when file is opened (not used as module")

