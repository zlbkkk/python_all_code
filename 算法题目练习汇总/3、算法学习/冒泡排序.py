
def maopao(lis):
    n = len(lis)

    for i in range(n-1):

        for j in range(n-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]


    return lis


lis = [3,1,2,5,6,7]

print(maopao(lis))
