import random
rn=random.randint(1,100)
count=0 
while True:
    n=int(input("Enter a number between 1-100 :"))
    count+=1
    if(n==rn):
        print("the number is found after ",count,"th comparision")
        break
    elif(n>rn):
        print("guess a small number")
    else:
         print("guess a larger number")    
