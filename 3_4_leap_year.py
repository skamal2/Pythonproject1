year = int(input("Enter a year. \n"))
if year%400==0 :
    print("This is a leap year")
elif year%100==0 and year%400==0:
    print("This is a leap year")
elif year%4==0 and not year%100==0:
    print("This is a leap year")
else:
    print("This is not a leap year.")

#another method
    #if year%400==0 or (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
    #print("This is a leap year")
    #else:
    #print("This is not a leap year.")