import random
import string
import sys

def CreateRandom():
    return random.choice(string.ascii_letters)

def Encoding():
    Line = input("Enter the line you want to encode: ")
    List = Line.split()
    for i in range (len(List)):
        if(len(List[i])==1):
            List[i]=List[i]
        # if(len(List[i])==2):
        #     List[i]=List[i][1]+List[i][0]
        if(len(List[i])>=3):
            List[i]=List[i][1:]+List[i][0]
            for j in range (3):
                Temp = CreateRandom()
                List[i]=Temp+List[i]
            for k in range (3):
                Temp = CreateRandom()
                List[i]=List[i]+Temp
    Line = ' '.join(List)
    Line = Line[::-1]
    print(f"Your encoded code is: {Line}\n")
                
def Decoding():
    Line = input("Enter the line you want to decode: ")
    Line = Line[::-1]
    List = Line.split()
    for i in range (len(List)):
        if(len(List[i])==1):
            List[i]=List[i]
        # if(len(List[i])==2):
        #     List[i]=List[i][1]+List[i][0]
        if(len(List[i])>=3):
            List[i]=List[i][3:-3]
            List[i]=List[i][-1:]+List[i][:-1]
    Line = ' '.join(List)
    print(f"Your decoded code is: {Line}")

def choose(choice):
    match(choice):
        case 1:
            Encoding()
            start()
        case 2:
            Decoding()
            start()
        case 3:
            sys.exit()
        case _:
            print("Enter a valid option")
            start()
    
def start():
    while True:
        try:
            print("Press 1 to encode a line ")
            print("Press 2 to decode a line ")
            print("Press 3 to exit ")
            choice = int(input("Enter yout choice: "))
            choose(choice)
        except ValueError:
            print("Invalid choice, choose valid option!")
        continue
start()

# The encoded line consists of the following steps:
#     ->If the word consists of 1 letter keep it as it is.
#     ->If the word consists of 2 letters reverse it.
#     ->If the word consists of 3 or more letters move the first letter of that word to the last and add 3 random alphabets to the start and the end of the word.
#     ->Now reverse the whole line.
#     ->Here I'm not following rule 2 because when we reverse the whole line it will remain same.
#     ->Decoding method is reverse of
#     -> And that's all
    
import random
import string
import sys

def CreateRandom():
    return random.choice(string.ascii_letters)

def Encoding():
    Line = input("Enter the line you want to encode: ")
    List = Line.split()
    for i in range (len(List)):
        if(len(List[i])==1):
            List[i]=List[i]
        # if(len(List[i])==2):
        #     List[i]=List[i][1]+List[i][0]
        if(len(List[i])>=3):
            List[i]=List[i][1:]+List[i][0]
            for j in range (3):
                Temp = CreateRandom()
                List[i]=Temp+List[i]
            for k in range (3):
                Temp = CreateRandom()
                List[i]=List[i]+Temp
    Line = ' '.join(List)
    Line = Line[::-1]
    print(f"Your encoded code is: {Line}\n")
                
def Decoding():
    Line = input("Enter the line you want to decode: ")
    Line = Line[::-1]
    List = Line.split()
    for i in range (len(List)):
        if(len(List[i])==1):
            List[i]=List[i]
        # if(len(List[i])==2):
        #     List[i]=List[i][1]+List[i][0]
        if(len(List[i])>=3):
            List[i]=List[i][3:-3]
            List[i]=List[i][-1:]+List[i][:-1]
    Line = ' '.join(List)
    print(f"Your decoded code is: {Line}")

def choose(choice):
    match(choice):
        case 1:
            Encoding()
            start()
        case 2:
            Decoding()
            start()
        case 3:
            sys.exit()
        case _:
            print("Enter a valid option")
            start()
    
def start():
    while True:
        try:
            print("Press 1 to encode a line ")
            print("Press 2 to decode a line ")
            print("Press 3 to exit ")
            choice = int(input("Enter yout choice: "))
            choose(choice)
        except ValueError:
            print("Invalid choice, choose valid option!")
        continue
start()

# The encoded line consists of the following steps:
#     ->If the word consists of 1 letter keep it as it is.
#     ->If the word consists of 2 letters reverse it.
#     ->If the word consists of 3 or more letters move the first letter of that word to the last and add 3 random alphabets to the start and the end of the word.
#     ->Now reverse the whole line.
#     ->Here I'm not following rule 2 because when we reverse the whole line it will remain same.
#     ->Decoding method is reverse of
#     -> And that's all
    