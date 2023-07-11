s = int(input("Enter your Salary :"))
y = int(input("ENter your Years of Service :"))

if(y>10):
    print("Your Bonus :",s*0.1)
elif(y>=6<10):
    print("Your bonus:",s*0.8)
else:
    print("Your Bonus :",s*0.5)