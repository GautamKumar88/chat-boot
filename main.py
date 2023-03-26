
print(" ")

time.sleep(2)

print(f"{chatbotname}: Whats your gender?")
gender = input(f"{name}: ")
print(" ")
time.sleep(2)
print(f"{chatbotname}: what is you are school name?")
school = input(f"{name}:")
print(" ")

time.sleep(2)
print(f"{chatbotname}:  what is your Roolnumber:-?")
Roolnumber = input(f"{name}:")
print("")
time.sleep(2)

print(f"{chatbotname}: What country are you from?")
country = input(f"{name}: ")
print(" ")

time.sleep(2)

print(f"{chatbotname}: What are your hobbies?")
hobbies = input(f"{name}: ")
print(" ")

time.sleep(2)

print(f"{chatbotname}: How do you feel right now? ")
feeling = input(f"{name}: ")
print(" ")

for i in range(5):
  print(" " + "." * i)
  sys.stdout.write("\033[F")
  time.sleep(1)

print(" ")
print(" ")
print(f"{chatbotname}: Wow interesting...")
print(" ")

time.sleep(2)import time
import sys

time.sleep(2)

print("Welcome to the AI Chatbot")
print(" ")

time.sleep(2)

print("Answers are not recorded!")
print(" ")

time.sleep(2)

print("Before we can start please make a gender and a name for your chatbot")
print(" ")

time.sleep(1)

chatbotname = input("Chatbot Name: ")
print(" ")

time.sleep(1)

chatbotgender = input("Chatbot Gender: ")
print(" ")

time.sleep(2)

print(f"{chatbotname}: Whats your name?")
name = input("You: ")

print(f"{chatbotname}: So your name is", name)
print(" ")

time.sleep(1)

print(f"{chatbotname}: You are a", gender)
print(" ")

time.sleep(1)

print(f"{chatbotname}: You are from", country)
print(" ")

time.sleep(1)

print(f"{chatbotname}: Your hobbies are", hobbies)
print(" ")

time.sleep(1)

print(f"{chatbotname}: And you feel", feeling)
print(" ")

time.sleep(2)


def more():
  print("Continue? (1. Yes or 2. No)")


more()
option = int(input(f"{name}: "))

if option != 2:
  if option == 1:
    print(" ")
    print(f"{chatbotname}: Alright")
    print(" ")

    time.sleep(2)

    print("?: Hahaha lets try mind reading!")
    print(" ")

    time.sleep(2)

    print("Before we start please give a name for your mind reader")
    print(" ")

    time.sleep(1)

    mindname = input("Mind Reader Name: ")
    print(" ")

    time.sleep(1)

    print("Mind Reader Gender: Locked as no gender")
    print(" ")

    time.sleep(2)

    print(f"{name}: Why dont I try mind reading!")
    print(" ")

    time.sleep(2)

    print(f"{mindname}: Alright! Bring it on!")
    print(" ")

    time.sleep(2)

    print("You are now", mindname)
    print("")

    time.sleep(1)

    print("Why? Because I dont know how to script anything better")
    print("")

    time.sleep(2)

    print(f"{name}: Whats your name?")
    print(f"Remember! You are at {mindname}'s perspective")
    mindname2 = input(f"{mindname}: ")
    print(" ")

  elif option == 0:
    print(" ")
    print("WOW SECRET ENDING!!!!1111!!!")
  else:
    print("Invalid option! Please restart the Chatbot!")
