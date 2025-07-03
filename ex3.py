amount=int(input("amount"))
age=int(input("age"))
if(amount>20000 or age<25):
    loan=int(input("loan"))
    if(loan<50000):
        print("loan ok")
    else:
        print("not elg loan")
        
else:
    print("not elgible")
    

