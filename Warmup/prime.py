a = int(input("Enter start value :"))
b = int(input("Enter the End Value :"))
print("The Prime nums are : ")

for i in range(a,b+1):
    if i>1:
        prime = True
        for j in range(2,i):
            if i%j==0:
                prime = False
                break

        if prime:
            print(i,end=' ')
    
    
