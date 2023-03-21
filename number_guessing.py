import random
print("no guessing:")
print("take any no from 1 to 1000")
b=int(input("Choose any no:"))
c=random.randint(1,1001)
print("number by system:",c)
if b==c:
    print("guessed right!")
else:
    print("guessed wrong!")




