b = int(input("Enter the range: "))
a = []
for i in range(b):
    if i%2==0:
        print("%d is divisible by 2" %i)
    elif i%3==0:
        print("%d is divisible by 3" %i)
    elif i%5==0:
        print("%d is divisible by 5" %i)
    elif i%7==0:
        print("%d is divisible by 7" %i)
    elif i%11==0:
        print("%d is divisible by 11" %i)
    else:
        print("%d is a prime number" %i)
        a.append(i)

print(a)
