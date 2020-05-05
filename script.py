#Speed Typing Test - Python Project
from time import time

def typingSpeed(typed_text, start_time, end_time):
	global time
	global words
	
	words = typed_text.split()
	wordLen = len(words)
	speed = wordLen / (time / 60)
	return speed

given_text="A quick brown fox jumped over a lazy dog."
print("Speed Typing Test")
print("Type this - :")
print(given_text)

input("Press Enter Key when you are ready")

start_time = time()

typed_text = input()

end_time = time()

time_taken =  end_time - start_time

time = round(time_taken, 2)
speed = typingSpeed(typed_text, start_time, end_time)

print("Average Speed ",round(speed, 2)," words per minute ")

