import random
print("game started")
a={"1":"Stone","2":"paper","3":"scissor"}
print(a)
while True:
    uwin=0
    cwin=0
    for i in range(1,6):
        print("round ",i,"start:")
        b=int(input("choose 1,2,3 for start:"))
        if b==1:
            print("u selected rock")
        elif b==2:
            print("u selected paper")
        elif b==3:
            print("u selected scissors")
        else:
            print("invalid choice")

        computer_choice=int(random.choice(list(a)))
        print("no choosen by computer is:",computer_choice,";")
        
        
        if b==computer_choice:
            uwin=uwin+1
            cwin=cwin+1
            print("draw match")

        elif(b==2 and computer_choice==1) or(b==1 and computer_choice==3)or(b==3 and computer_choice==2):
            uwin+=1
            print("u win")
        else:
            cwin+=1
            print("computer win!")
    if uwin>cwin:
        print("u won this game")
        print("score is","ur score:",uwin,"& computer score:",cwin,sep=" ")
    elif cwin>uwin:
        print("computer wins this game u lost")
        print("score is","ur score:",uwin,"& computer score:",cwin,sep=" ")
    else:
        print("match draw")
        print("score is","ur score:",uwin,"& computer score:",cwin,sep=" ")

    d=input("want to play again?(yes/exit)").lower()
    if d=="yes":
        continue
    else:
        break

