fr = int(input("Enter food rating (1-5): "))
sr = int(input("Enter service rating (1-5): "))
ar = int(input("Enter ambience rating (1-5): "))
bill_amount = float(input("Enter the bill amount: "))

if fr >= 4 and sr >= 4 and ar >= 4:
    tip = 0.1 * bill_amount
elif fr >= 4 and (sr <= 3 or ar <= 3):
    tip = 0.05 * bill_amount
elif (fr <= 3) and (sr >= 4 and ar >= 4):
    tip = 0.05 * bill_amount
else:
    tip = 0.01 * bill_amount

total_amount = bill_amount + tip

print("Tip amount: $", tip)
print("Total amount: $", total_amount)
