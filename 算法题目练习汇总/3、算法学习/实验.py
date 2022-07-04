
from functools import reduce

with open("c:\\1.txt",encoding="utf-8") as f:
    b=[]
    for i in f:
        a=i.split()
        b.append(a)
    print(b)

num=[1,23,4,6,7,8,9,10]

f=[i for i in num if i%2==0 and num.index(i)%2==0]
print(f)


with open("c:\\1.txt") as f:
    for i in f:
        print(i)


def zlb():
    print("hello")


with open("c:\\1.txt") as f:
    print("hello")


while i < 10:
    print("hello")