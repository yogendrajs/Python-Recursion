# def fac(num):
#     if num == 1:
#         return 1
#     else:
#         return fac(num-1)*num
# user = int(input("Enter an input: "))
# print fac(user)

# from itertools import cycle
# for t in cycle(range(0, 4)):
#     print(t)
########################################################################################
# to find the sum of internal lists and then find the totalsum of all the numbers in all the lists
# a = [[1,2,3,4,5],[6,7,8,9,12,11,3],[12,43,22,12,56,98,9]]
# i = 0
# j = 0
# sum = 0
# total = 0
# while i < len(a):
#     j = 0
#     sum = 0
#     while j < len(a[i]):
#         sum = sum + a[i][j]
#         j += 1
#     print sum
#     total = total + sum
#     print "---------"
#     i += 1
# else:
#     print "total is " + str(total)
