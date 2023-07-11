n = input("Your Name :")
age = int(input("Enter your Age :"))
g = input("Your Gender (M or F):")
no = int(input("No Of Days :"))

if(age>=18 and age<30 and g=='M'):
    print(n,"Amount To Be paid : ",no*700)
elif(age>=18 and age<30 and g=='F'):
    print('akcjskd :',no*750)
elif(age>=30 and age<40 and g=='M' ):
    print("svvsdv :",no*800)
else:
    print("Retry..")