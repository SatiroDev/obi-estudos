A, B = input().split()

a = int(A)
b = int(B)

c = 0
if 1 <= a and a <= b and b <= 10**9:

    for i in range(-b, a + 1):
        media = (a + i + b) / 3
        if media == a:
            c = i
            break
print(c)
