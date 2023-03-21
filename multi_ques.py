print("*welcome*")
print("Start the quiz")
a=input("Type *yes* to start the quiz: ")

if(a.lower()=="yes"):
    n=0
    x=0
    v=0
    print("Choose options a,b,c,d for answering: ")
    print("Q1: What is the PH of H2O")
    d={"a":"6","b":"7","c":"9","d":"5"}
    print(d)
    m=input("Select options= ")
    
    while(m.lower()=="b"):
        print("Correct answer scored 1 points!")
        
        v=n+1
        print(v)
        break;

    
    print("Wrong answer!")
    print("Which of the following gas is reduced in the reduction process?")

    r=["oxygen","helium","carbon","hydrogen"]
    print(r)
    e=input ("Type answer ") 
    #e="Hydrogen"
    
    if e.lower() in r:
        print("Correct answer scored 1 points!")
        x=0
        x=n+1
        print(x)
    else:
        print("wrong answer")

    print("Total scores:",(x+v),"out of two questions")
 # type: ignore

else:
 print("As you said no,so no further moves")