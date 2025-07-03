u_name="tamil"
u_password="0919"
name=input("enter name")
password=input("enter password")
def valid():
    if(u_name==name and u_password==password):
        return correct
    else:
        return invalid
valid()
