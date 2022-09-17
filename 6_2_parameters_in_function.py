import random
user=int(input("How many sides?"))
def main(user):
    r = random.randint(1,user)
    while r != user:
        r = random.randint(1, user)
        print(r)
main(user)