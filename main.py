print("welcome to tip calculator!")

bill=float(input("what was the total bill? $"))

tip=int(input("how much tip would you like to give?10,2,15? "))

people=int(input("how many people to split the bill with? "))

bill_with_tip= tip/100*bill + bill

bill_per_person=bill_with_tip/people

final_bill_per_person=round(bill_per_person)

print(f"Bill per person:${final_bill_per_person}" ) 




