def sum(i):
    if i == 0:
        return a[0]
    else:
        return sum(i-1) + a[i]


a = [1,2,3,4,5,6]
i = len(a)-1
print sum(i)
