score=int(input())
if(score<35):
    print("fail")
elif(score>35 and score<70):
     print("avg")
elif(score<70 and score<100):
    print("good")
else:
    print("invalid")
