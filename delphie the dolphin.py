# delphie the dolphin
pip3 install termcolor

print("hai!!! im a dolphin!")
print("you can't see me")
print("im inside your computer...")
print("im not a virus")
print("but i would like to interview you")

#hi dolphin
print("i almost forgot...")
print ("my name is delphie")
print("this is me :D")
print("         ,-._")
print("       _.-'  '--.")
print("     .'      _  -`\_")
print("    / .----.`_.'----' ")
print("    ;/     `")
print("   /_;")

print("ill show you my magic trick")
print("ok! i have my eyes closed you write down the answers to the questions you ask")
print ("*delphie's eyes are closed, she cannot see your input*")

#number
num = int(input("whats your favorite single digit number?: "))
print("good good...")

# check if the number is greater than, less than, or equal to 5
if num > 5:
    print("i guess,,, your favorite number is greater than five")
elif num < 5:
    print("i guess,,, your favorite number is smaller than five")
elif num == 5:
    print("hmmm.....")

print("delphie is thinking....")
#concatanate
print("is your favorite number... " + str(num) + "?")
print("hehehe.. i'm right, aren't i?")

# color
from termcolor import colored

color= input("What's your favorite color? ").lower()

#options
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

if color in colors:
    print(colored("Let me guess... Your favorite color is " + color + "!", color))
else:
    print("ooops,,, delphie can't print that color.. try one of these: red, green, yellow, blue, magenta, cyan, or white.")

answer = str(input("did I get it right? (yes/no): "))

if answer == "yes":
    print("yayy!!!@11!!!1")
else: 
    print ("oops...sorry :(")
















