import time

n = int(input())    

count = 0


def fib1(n):
    global count
    count += 1
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    if n <= 1:
        return n
    else:
        data = []
        data.append(0)
        data.append(1)
        for i in range(2, n+1):
            data.append(data[i-1] + data[i-2])
        return data[n]


def fib3(n):
    if n <= 1:
        return n
    else:
        temp1 = 0
        temp2 = 1
        for i in range(2, n+1):
            data = temp1 + temp2
            temp1 = temp2
            temp2 = data
        return data


s = time.time()  
print(fib1(n))
e = time.time()
print(e-s)
print(count)
# s = time.time()
# print(fib2(n))
# e = time.time()
# print(e-s)

# s = time.time()
# print(fib3(n))
# e = time.time()
# print(e-s)
