#задача
a = 0
i = 1
while i<1000:
    if i%3 == 0 or i%5 == 0:
        a = a + i
    i = i + 1
print(a)

#2 задача
a = 0
fib1 = 1
fib2 = 1
i = 1
while fib1 <= 4000000:
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
    if fib1 % 2 == 0:
        a = a + fib1
    i = i + 1
print(a)

#3
n = 11
i = 2
while i<n:
    if n % i > 0:
        i = i + 1
    if n % i == 0 and i<n:
        print(f'число {n} составное')
        break
    else:
        print(f'число {n} простое')
        break


#5
n = 1
while True:
    if n%1 == n%2 == n%3 == n%4 == n%5 == n%6 == n%7 == n%8 == n%9 == n%10 == n%11 == n%12 == n%13 == n%14 == n%15 == n%16 == n%17 == n%18 == n%19 == n%20:
        print(n)
        break
    else:
        n = n + 1

#6
a1 = 1
an = 100
n = 100
s = (a1+an)*n*0.5
s2= s**2
s22 = n*((n+1)*(2*n+1))/6
s3 = abs(s2 - s22)
print(s3)

#7
i = 0
k = 1
h = 0
t=10000
while i <= t:
    k = k + 1
    m = 1
    n = k
    while m<=n:
        m = m + 1
        if n%m > 0:
            m = m + 1
        if n%m == 0 and m < n:
            h = 1
            break
        if m == n:
            h = 0
            break
    if h == 0:
        i = i + 1
        if i==t:
            print(k)


