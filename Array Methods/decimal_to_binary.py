# 7. Write a program to accept a decimal number and convert it to binary.
n = int(input())
arr = []

while n != 0:
    rem = n % 2
    arr.append(rem)
    n //= 2


size = len(arr)
s, e = 0, size - 1

while s < e:
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp
    s += 1
    e -= 1
print(arr)
