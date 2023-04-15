import random # random module

def validate(xx):
    num1 = xx
    while True:
        if num1 < 20 :
            num1 = int(input('Entered Number is below 20 ! Reenter:  '))
        elif num1 > 80:
            num1 = int(input('Entered Number is above 80 ! Reenter:  '))
        elif (num1 >= 20)and (num1 <= 80) :
            num1 = xx
            break
def valnum(xxx) :
    while True:
        try:
            global num
            num = int(xxx)
            break
        except ValueError:
            xxx = input( "Error! Please enter only numeric number: ")

answer = random.randint(20,80) #this provide random number and is saved in answer var
#input from user
name = input("What is Your Name: ") 
print(" *** " + "Good Day " + str.upper(name) + " *** ") #first print line 
#blank line 
#print("Random Number: " , answer) # value from random module 
num = input("Guess a number btw 20 to 80 : ")
valnum(num)
validate(num)
#logic 
for i in range (1,5):
    if num > answer:
        print(str.upper("Your guess is high! "))
        if i == 4:
            break
        else:
            num = (input("Take another guess : "))
            valnum(num)
            validate(num)
    elif num < answer:
        print(str.upper("Your guess is low! "))
        if i == 4:  
            break
        else:
            num = input("Take another guess : ")
            valnum(num)
            validate(num)
    else:
        break
#end of for loop 
if num != answer:
    print("Opss! You had exceded " +str(i)+" guess limit.")
else:
    print ( "CORRECT! Congartulation for taking only  " + str(i) + " guess...")

print("\n")
print("Correct Number is: " + str(answer))
print("\n")
print(" E*N*D ")
