def main(integers):
    for i in integers:
        print(i)
    integers.clear()
    return
num_list=[0,5,1,5,2,0,5,1]
main(num_list)
num_list.append(9)
main(num_list)