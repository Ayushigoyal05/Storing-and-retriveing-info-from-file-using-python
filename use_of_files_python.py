from datetime import datetime
m=int(input("want to retieve=1 or lock=2"))
print("harry=1, rohan=2 , hammad=3")
n=int(input("select the client "))
l=int(input("exercise=1 and diet=2"))
if(m==2):
    if(n==1):
        if(l==1):
            f=open("harry_exe.txt","a")
            print("enter the exercise")
            f.write(input()+"  "+str(datetime.now()))
            f.close()
        elif(l==2):
            f=open("harry_diet.txt","a")
            print("enter the diet")
            f.write(input()+"  "+str(datetime.now()))
            f.close()
    elif(n==2):
        if(l==1):
            f = open("rohan_exe.txt","a")
            print("enter the exercise")
            f.write(input()+"  "+str(datetime.now()))
            f.close()
        elif (l == 2):
            f = open("rohan_diet.txt","a")
            print("enter the diet")
            f.write(input()+"  "+str(datetime.now()))
            f.close()
    elif(n==3):
        if(l==1):
            f = open("hammad_exe.txt","a")
            print("enter the exercise")
            f.write(input()+"  "+str(datetime.now()))
            f.close()
        elif (l == 2):
            f = open("hammad_diet.txt","a")
            print("enter the diet")
            f.write(input()+"  "+str(datetime.now()))
            f.close()
if(m==1):
    if(n==1):
        if(l==1):
            f=open("harry_exe.txt","r")
            print(f.read())
            f.close()
        elif(l==2):
            f = open("harry_diet.txt", "r")
            print(f.read())
            f.close()
    elif(n==2):
        if (l == 1):
            f = open("rohan_exe.txt", "r")
            print(f.read())
            f.close()
        elif (l == 2):
            f = open("rohan_diet.txt", "r")
            print(f.read())
            f.close()
    elif(n==3):
        if (l == 1):
            f = open("hammad_exe.txt", "r")
            print(f.read())
            f.close()
        elif (l == 2):
            f = open("hammad_diet.txt", "r")
            print(f.read())
            f.close()
