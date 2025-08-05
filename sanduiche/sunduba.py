n, m = input().split()
ingredientes = ['queijo', 'presunto', 'goiabada', 'azeitona']
N = int(n)
M = int(m)

quantidade = 0
verificacao = True
lista = []
cont = 0
if 1 <= N and N <= 20 and 0 <= M and M <= 400:
    for i in range(M):
        x, y = input().split()
        X = int(x)
        Y = int(y)
        if 1 <= X and X <= N and 1<= X and X < Y:
            lista.append([X, Y])
            continue
        else:
            verificacao = False
    # if verificacao:
    #     for y in range(1, N+1):
    #         for z in  range(1, y+1):
    #             quant = len(lista)
    #             aux = 0
    #             while aux < quant:
    #                 if y in lista[aux] and z in lista[aux]:
    #                     lista.remove(lista[aux])
    #                     cont += 1
    #                 aux += 1


if verificacao and M == 0:
    quantidade = (2 ** N) - 1
elif verificacao:
    quantidade = (2 ** N) - M - 2
print(quantidade)




# Entrada
# 3 2
# 2 3
# 1 2

s = 0
# Por exemplo, suponha que num determinado dia N é igual a quatro e os ingrediantes são queijo, presunto, goiabada e azeitona, e M é igual a dois: os pares (goiabada, presunto) e (azeitona, goiabada) não podem ser utilizados no mesmo sanduíche. Nesse dia, alguns dos sanduíches que podem ser feitos são:

# presunto, queijo X
# azeitona 
# presunto, azeitona, queijo 
# goiabada, queijo 

# Alguns dos sanduíches que não podem ser feitos são:

# presunto, queijo, goiabada 
# azeitona, goiabada 
# goiabada, presunto, azeitona 