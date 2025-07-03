a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
select=input("add/sub/mul/div")
if(select=="add"):
    print(a+b);
elif(select=="sub"):
    print(a-b)
elif(select=="mul"):
    print(a*b)
elif(select=="div"):
    print(a/b)
else:
    print("loose")

