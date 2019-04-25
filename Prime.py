def prime(num):
    if num == 2:
        return 2
    else:
        new = 0
        for i in range(2, num):
            if num%i == 0:
                new +=1
                break
        if new == 0:
            print (num)
        return prime(num-1)
(prime(20))
