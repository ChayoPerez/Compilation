import time
import threading
import concurrent.futures


print("SECTION 1: Basic threads\n-----------------")


start = time.perf_counter() # So we can know how long it takes to
							# reach the double join

lock = threading.Lock() # Waits for an instruction to finish 
						# before going on with the thread

def start_sleeping(name, seconds):
	with lock:
		print(name + " is sleeping for " + str(seconds) + " [s]")
	time.sleep(seconds)
	with lock:
		print(name + " is done sleeping")

"""
Why the lock? Without it what was is printed is:


Katherina sleeping 1 secondEmilia sleeping 1 second
Done sleepingDone sleeping
Everyone finished sleeping for: 1 seconds

Using with lock you can make it so the printing instruction is not
interrupted by the next
"""


"""
with lock is basically:

lock.acquire()
# code
lock.release()

but in one line, just like reading files
"""

t1 = threading.Thread(target=start_sleeping, args=("Katherina", 1,))
t2 = threading.Thread(target=start_sleeping, args=("Emilia", 2,))

t1.start()
t2.start()

t1.join()
t2.join() # So both end before going forward

finish = time.perf_counter()

print("Everyone finished sleeping for: " + str(round(finish - start)) + " seconds")


print("\n\nSECTION 2: Multiple threads\n-----------------")


start = time.perf_counter()

def start_sleeping2(name, seconds):
	with lock:
		print(name + " is sleeping for " + str(seconds) + " [s]")
	time.sleep(seconds)
	with lock:
		print(name + " is done sleeping")

threads = [] # So you can create many threads and have access to them later

for _ in range(10):
	t = threading.Thread(target=start_sleeping, args=("Someone", 1,))
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()

finish = time.perf_counter()

print("Everyone finished sleeping for: " + str(round(finish - start)) + " [s]")



print("\n\nSECTION 3: Daemon threads\n-----------------")

# Pending


print("\n\nSECTION 4.1: Using concurrent.futures\n-----------------")

def random_function(seconds):
	with lock:
		print("Start sleeping..." + str(seconds))
	time.sleep(seconds)
	return "Done sleeping..." + str(seconds)

with concurrent.futures.ThreadPoolExecutor() as executor:
	f1 = executor.submit(random_function, 2)
	f2 = executor.submit(random_function, 2)

	print(f1.result())
	print(f2.result())


print("\n\nSECTION 4.2: Using concurrent.futures\n-----------------")

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = [executor.submit(random_function, sec) for sec in secs]
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())


print("\n\nSECTION 5: Using map\n-----------------")

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = executor.map(random_function, secs)
	
	for result in results:
		print(result)


"""
What is printed: 


Start sleeping...5
Start sleeping...4
Start sleeping...3
Start sleeping...2
Start sleeping...1
Done sleeping...5
Done sleeping...4
Done sleeping...3
Done sleeping...2
Done sleeping...1


All start at the same time
All end at the same time and in the order they started
"""