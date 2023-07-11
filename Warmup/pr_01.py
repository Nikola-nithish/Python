even = 0
odd = 0

for i in range(20,51):
    if i%2==0:
        even+=1
    else:
        odd+=1   
    
print('Even :',even)
print('Odd :',odd)