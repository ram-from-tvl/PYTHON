DOB=(input("enter your date of birth(ddmmyyyy): "))
year=int(DOB[4:])
age=2023-year
ticketprice=1020
if age>=60 :
    ticketprice=1020*0.8
    print("you are offered a concession of 20% for the next trip",end="\n")
    print('updated price : {0:.2f}'.format(ticketprice))
else:
    print("you are ineligible for availing concession for your next trip" , end="\n")
    print('fixed price : {0:.2f}'.format(ticketprice))
