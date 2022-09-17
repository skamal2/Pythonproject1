import random

def main():
    r = random.randint(1, 6)

    while r!=6:
        r = random.randint(1, 6)
        print(f"The result of the roll is {r}")
main()