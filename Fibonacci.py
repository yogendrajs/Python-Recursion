# must read about functools and lru_cache
# from functools import lru_cache as caching
# @caching()
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
# for i in range(100):
#     print (f(i))

# # to have a list of fibonacci numbers, we need to define list
# def list(n):
#     i = 1
#     new_list = []
#     while i < n:
#         new_list.append(f(i))
#         i+=1
#     return new_list
# # to print list we need to call it with suitable argument
# print (list(10))
# ---------------------------------------------------------
# ---------------------------------------------------------
# another way to solve this problem

# def f(n):
#     if n == 2:
#         return [1,1]
#     else:
#         pre = f(n-1)
#         sum = pre[-1] + pre[-2]
#         pre.append(sum)
#         lista = pre
#         return lista
# print (f(10))

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
