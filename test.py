m = 111

def tamanho(num):
    tam = 0
    while num != 0:
        num //= 10
        tam += 1
    return tam

tamanho(1)



def soma_dig(num):
    tam = tamanho(num)
    i = 0
    soma = 0
    while i != tam:
        soma += num % 10

        num //= 10

        i += 1
    print(soma)

soma_dig(19844)