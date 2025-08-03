S = input()
A = input()
B = input()

s, a, b = int(S), int(A), int(B)
def tamanho(num):
    tam = 0
    while num != 0:
        num //= 10
        tam += 1
    return tam

def soma_dig(num):
    tam = tamanho(num)
    i = 0
    soma = 0
    while i != tam:
        soma += num % 10

        num //= 10

        i += 1
    return soma


cont = 0
if 1 <= s and s <= 36:
    if 1 <= a and a <= 10000:
        if 1 <= b and b<= 10000:
            if a <= b:
                for i in range(a, b+1):
                    soma = soma_dig(i)
                    if soma == s:
                        cont +=1

                        
print(cont)
