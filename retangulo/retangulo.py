N = int(input())

L = list(map(int, input().split()))

soma = sum(L)

if 4 <= N and N <= 10**5:
    verificacao = True
    if soma % 2 != 0:
        print('N')
    
    else:
        posicao = [0]
        for i in range(N):
            posicao.append(posicao[-1] + L[i])

        posicao.pop(0)

        s = set(posicao)
        cont = 0
        for x in posicao:
            oposto = (x + soma // 2) % soma
            if oposto in s:
                cont += 1
                if cont >= 2:
                    break
        print('S' if cont >= 2 else 'N')

