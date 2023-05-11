sal=int(input("enter your salary:"))
years=int(input("enter your years of experience:"))
if years>=10 :
    bonus = sal-sal*0.9
    print("bonus : ",bonus)
elif years>=6 and years<10 :
    bonus=sal-sal*0.92
    print("bonus : ",bonus)
else:
    bonus=sal-sal*0.95
    print("bonus : ",bonus)
    
