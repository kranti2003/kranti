def ncr(n,r):
    return fact(n)/(fact(n-r)*fact(r))

def fact(n):
    factorial =1
    for i in range(1, n+1):
        factorial = factorial * i

    return factorial


n = int(input("Enter n :: "))
r = int(input("Enter r :: "))

print("NCR of ",n,",",r," is ", int(ncr(n,r)))
