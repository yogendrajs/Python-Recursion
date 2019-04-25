def pal(i):
    if i == 0:
        return a[0]
    else:
        return a[i] + pal(i-1)

a = raw_input("Enter a name: ")
j = len(a)-1

if a == pal(j):
    print "Yes! it is palindrome"
else:
    print "No! it is not palindrome"
