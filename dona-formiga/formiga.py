s, t, p = input().split()

S=int(s)
T=int(t)
P=int(p)

def funcao_rec(listaP: list, lista_altura):
    lista = listaP
    quantidade = 0
    posicao_inicial = P-1
    for indice in range(0, T):

        posicao1 = lista_altura[indice][0]-1
        posicao2 = lista_altura[indice][1]-1
        if posicao1 == posicao_inicial:
            if lista[posicao1] > lista[posicao2]:
                quantidade += 1
        if posicao2 == posicao_inicial:
            if lista[posicao2] > lista[posicao1]:
                quantidade += 1


    return quantidade

lista_principal = []
lista_altura = []

if 1 <= S and S <= 200:
    if 1 <= T and T <= (S * (S-1)/2):
        if 1 <= P and P <= S:
            Ai = list(map(int, input().split()))
            lista_principal = Ai
            for x in range(T):
                ij = list(map(int, input().split()))
                lista_altura.append(ij)
            quant = funcao_rec(lista_principal, lista_altura)
            print(quant)
