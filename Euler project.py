#1
a = 0
i = 1
while i<1000:
    if i%3 == 0 or i%5 == 0:
        a = a + i
    i = i + 1
print(a)

#2
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
r = 13195
arg = 5
list1 = [n for n in range(1, r)]
list2 = [2]
for n in list1:
    i = 2
    while i < n:
        if n % i > 0:
            i = i + 1
        if n % i == 0 and i < n:
            break
        if n == i:
            list2.append(n)
            break
for k in list2:
    if r%k == 0:
        print(k)
        r = r / k

#3
i = 0
k = 1
h = 0
t=1000
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

#4
list1 = []
list2 = []
n1 = [i for i in range(10,1000)]
n2 = [i for i in range(10,1000)]
for i in n1:
    for n in n2:
        list1 = list(str(n*i))
        h = len(list1)
        if (h == 6 and list1[0] == list1[-1] and list1[1] == list1[-2] and list1[2] == list1[-3]) or (h == 5 and list1[0] == list1[-1] and list1[1] == list1[-2]):
            list2.append(int(''.join(list1)))
print(max(list2))



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
t = 10000
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

#8
a = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
list1 = list(a)
lista = list(map(int, list1))
res = []
n = 0
while n <= 999:
    h = lista[0+n] * lista[1+n] * lista[2+n] * lista[3+n] * lista[4+n] * lista[5+n] * lista[6+n] * lista[7+n] * lista[8+n] * lista[9+n] * lista[10+n] * lista[11+n] * lista[12+n]
    n = n + 1
    res.append(h)
    if n == 986:
        break
print(max(res))

#10
import time
start_time = time.time()
lim = 2000000
res = [2]
n = 2
while n < lim:
    n = n + 1
    i = 2
    while i < n:
        if n % i > 0:
            i = i + 1
        if n % i == 0 and i < n:
            break
        if n % i == 0 and i == n:
            res.append(n)
            break
print(sum(res))
end_time = time.time()
print(f"It took {end_time-start_time:.10f} seconds to compute")

#11
a1 = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
a2 = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
a3 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
a4 = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
a5 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
a6 = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
a7 = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
a8 = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
a9 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
a10 = [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95]
a11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
a12 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57]
a13 = [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
a14 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
a15 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
a16 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
a17 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
a18 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
a19 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
a20 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
main_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20]
res_list = []
n = -1
arg = 0
while n <= 15:
    n = n + 1
    if n == 15:
        arg = arg + 1
        n = -1
    if arg == 16:
        break
    res_list.append(main_list[0 + arg][0 + n] * main_list[0 + arg][1 + n] * main_list[0 + arg][2 + n] * main_list[0 + arg][3 + n])
    res_list.append(main_list[1 + arg][0 + n] * main_list[1 + arg][1 + n] * main_list[1 + arg][2 + n] * main_list[1 + arg][3 + n])
    res_list.append(main_list[2 + arg][0 + n] * main_list[2 + arg][1 + n] * main_list[2 + arg][2 + n] * main_list[2 + arg][3 + n])
    res_list.append(main_list[3 + arg][0 + n] * main_list[3 + arg][1 + n] * main_list[3 + arg][2 + n] * main_list[3 + arg][3 + n])
    res_list.append(main_list[0 + arg][0 + n] * main_list[1 + arg][0 + n] * main_list[2 + arg][0 + n] * main_list[3 + arg][0 + n])
    res_list.append(main_list[0 + arg][1 + n] * main_list[1 + arg][1 + n] * main_list[2 + arg][1 + n] * main_list[3 + arg][1 + n])
    res_list.append(main_list[0 + arg][2 + n] * main_list[1 + arg][2 + n] * main_list[2 + arg][2 + n] * main_list[3 + arg][2 + n])
    res_list.append(main_list[0 + arg][3 + n] * main_list[1 + arg][3 + n] * main_list[2 + arg][3 + n] * main_list[3 + arg][3 + n])
    res_list.append(main_list[0 + arg][0 + n] * main_list[1 + arg][1 + n] * main_list[2 + arg][2 + n] * main_list[3 + arg][3 + n])
    res_list.append(main_list[0 + arg][3 + n] * main_list[1 + arg][2 + n] * main_list[2 + arg][1 + n] * main_list[3 + arg][0 + n])
print(max(res_list))

