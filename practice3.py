count=0 
def greet():
    print("Congratulation goal reached!")
    global count 
    count+=1
    return
greet()

if count >=2:
    print("gud")
else:
    print("bad")