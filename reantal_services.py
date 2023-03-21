print("start with renting cars ")
print('''          1.Buy car
          2.exit ''')

a=int(input("choose 1,2  any according to the need: "))
if a==1:
    print("stocks for cars are:")
    l={"1.Maruti":"10","2.BMW":"20"}
    print(l)
    print("choose any car wanted to buy ")
    
    
    b=int(input("any no 1,2:"))
    if b==1:
        print("choosen Maruti")
        print("choose quantitiy of maruti")
        mar=10
        marv=int(input("so how many:"))
        print("Choosen ",marv,"that much quantity")
        av=mar-marv
        print("stocks left after buying:",av)
        pri=marv*1000
        print("price of quantity=",marv," ","is",pri)
    elif b==2:
        print("choosen BMW")
        print("choose quantitiy of BMW")
        bar=10
        barv=int(input("so how many:"))
        print("Choosen ",barv,"that much quantity")
        bv=bar-barv
        print("stocks left:",bv)
        price=barv*1000
        print("price of quantity=",barv,"is",price)
    else:
        print("invalid number choosen")
else:
    print("EXIT")
    

    
