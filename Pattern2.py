# 10, 11, 110, 111, 1110, 1111, 11110, 11111, 111110, 111111...
def pattern(num):
    if num == 1:
        return 10
    else:
        if num % 2 == 0:
            return pattern(num-1)+1
        else:
            return pattern(num-1)*10

i = 1
while i < 10:
    print pattern(i)
    i += 1
