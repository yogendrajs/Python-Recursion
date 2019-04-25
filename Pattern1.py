# 1, 4, 8, 11, 22, 25, 50, 53, 106...
def pattern(num):
    if num == 1:
        return 1
    else:
        if num % 2 == 0:
            return pattern(num-1)+3
        else:
            return pattern(num-1)*2

i = 1
while i < 10:
    print pattern(i)
    i+=1
