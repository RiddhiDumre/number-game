import random
n=random.randint(0,20)
t=10
print('''\n
you have 10 guesses to correct ans
all the best!
''')


for i in range(10):
    you=int(input("\nEnter your guess: "))
    if(you>n):
        print(f"number of guesses left:{t}")
        print("Number entered is higher than the int")
    elif(you<n):
        print(f"number of guesses left:{t}")
        print("Number entered is lower than the int")
    elif(n==you):
        print("YOU WON YAY!!")
        break
    t-=1    
print("Game over")
             