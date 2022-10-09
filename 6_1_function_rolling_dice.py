import random

def main():
    r = 0

    while r!=6:
        r = random.randint(1, 6)
        print(f"The result of the roll is {r}")
main()