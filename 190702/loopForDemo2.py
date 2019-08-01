
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end=' ')
#     print()

# for first_number in range(1,10):
#     for second_number in range(1,first_number+1):
#         print(first_number,"*",second_number,"=",first_number*second_number," ",)
#     print()

wid=1
while wid<=5:
    len=1
    while len<=wid:
        print("*"," ")
        len+=1
    print("\n")
    wid+=1
