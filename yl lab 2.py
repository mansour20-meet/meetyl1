def new_list():
    a=[5,10,15,20,25]
    global b
    b=[]
    b.append(a[0])
    b.append(a[-1])

new_list()
print(b)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for c in a:
    if c<5:
        print(c)   

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e=[]
def common_nums():
    for c in a:
        for d in b:
            if c==d:
                e.append(c)
    print(e)

common_nums()

d=0
input1 = input("prime?")
for i in range(input1):
    if (input1%(i+1)==0):
        d=d+1
    if (d==2):
        print ("is prime number")
    else:
        print("not prime number")
