def f(n,l):
    l.sort()
    if len(l) == 0:
        return False
    elif len(l) == 1:
        if n == l[0]:
            return True
        else:
            return False
    else:
        a = l[:len(l)/2]
        b = l[len(l)/2:]
        mid = len(b) + (len(a) - len(b))/2
        c = l[mid]
        if c == n:
            return True
        elif c > n:
            return f(n,a)
        elif c < n:
            return f(n,b)
        else:
            return False
print (f(3, [8, 5, 7, 10, 4, 6, 3, 1, 9]))
#
# another method to find a number in a list as given in Saral
# # ---------------------------------------------
#
# def f(n,l):
#     if len(l) == 1:
#         if l[0] == n:
#             return True
#         else:
#             return False
#     elif len(l) == 0:
#         return False
#     else:
#         first = l[:len(l)/2]
#         second = l[len(l)/2:]
#         return f(n,first) or f(n,second)
# print f(8,[1,2,32,45,3,7,22])
