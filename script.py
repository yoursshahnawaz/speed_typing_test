#Speed Typing Test - Python Project
from time import time

def typingSpeed(typed_text, start_time, end_time):
	global time
	global words
	
	words = typed_text.split()
	wordLen = len(words)
	speed = wordLen / (time / 60)
	
	return speed

def typingErrors(given_text):
        global given_words

        given_words = given_text.split()
        errors = 0
        
        for i in range(len(words)):
                if words[i]==given_words[i]:
                        continue
                else:
                        errors+=1
        return errors

        
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
speed = round(typingSpeed(typed_text, start_time, end_time),2)
errors = typingErrors(given_text)

print("You took",time,"seconds with an Average Speed of",speed,"words per minute with",errors,"errors.")
