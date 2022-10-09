names ={"ram", "sam", "bam", "pam"}
user=0
while user!="":
    user = input("Enter name: ")
    if user in names:
        print("Existing name.")
    if user not in names:
        names.add(user)
        print("New name.")

    if user=="":
        break
for i in (names):
    print([i])