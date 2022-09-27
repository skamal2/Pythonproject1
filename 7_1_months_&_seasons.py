months_of_the_year=("January", "February", "March",
                    "April", "May", "June", "July", "August",
                    "September", "October", "November", "December")
number_of_the_months = int(input("Enter the month number (1-12): "))
months = months_of_the_year[number_of_the_months-1]
if 3<=number_of_the_months<=5:
    print(f"Month number {number_of_the_months} is {months}:Spring season!")
elif 6<=number_of_the_months<=8:
    print(f"Month number {number_of_the_months} is {months}:Summer season!")
elif 9<=number_of_the_months<=11:
    print(f"Month number {number_of_the_months} is {months}:Autumn season!")
elif 12== number_of_the_months or 0<=number_of_the_months <= 2:
    print(f"Month number {number_of_the_months} is {months}:Winter season!")
