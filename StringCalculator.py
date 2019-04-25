def operate(num1, operator, num2):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2

c = "3 + 5 - 2 * 4 / 2 + 8 - 10 * 9 / 3"
c = c.rstrip().split()
for i in range(len(c)):
    i = 0
    first = int(c[0])
    if len(c) == 1:
        break
    second = int(c[2])
    value = operate(first,c[1],second)
    c = c[3:]
    c.insert(0,value)
print c
# ----------------------------------------------------------------
# sum of the even fibonacci sequence numbers to 4 million
# a = 0
# b = 1
# sum = 0
# while a < 4000000:
#     c = a+b
#     if a % 2 == 0:
#         sum = sum + a
#     a = b
#     b = c
# print sum
