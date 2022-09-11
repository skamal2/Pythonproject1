import random
diceroll = int(input("How many times to roll dice? \n"))
sum=0
for dicero in range(diceroll):
    r=random.randint(1,6)
    sum=sum+r
print(sum)

