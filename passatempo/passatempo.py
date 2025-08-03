L, C = input().split()

l, c = int(L), int(C)
variaveis = {}
lista_var = []
xs = []
S = []
if 1 <= l and l <= 100:
    for linha in range(l+1):
        if linha == l:
            for lin in range(c):
                x = input().split()
                for num in x:
                    xi = int(num)
                    if -10**8 <= xi and xi <= 10**8:
                        xs.append(xi)
                    else:
                        break
                break
            break
        var = input().split()
        s = int(var[-1])
        if -10**8 <= s and s <= 10**8: 
            S.append(s)
            sub_var = []
            for indice in range(len(var)-1):
                if var[indice] not in variaveis:
                    variaveis[var[indice]] = 0
                sub_var.append(var[indice])
            lista_var.append(sub_var)
            
lista_var_copia = lista_var

# print(variaveis)
cont1 = 0
volta = 0
for i in range(len(lista_var_copia)):
    i_certo = i
    cont2 = 0
    verificacao = True
    indiceLinha = 's'
    indiceColuna = 's'
    nome_var_linha = ''
    while cont2 < len(lista_var_copia):
        if volta >= 1:
            i_certo = i - 1
            print('z')
        if lista_var_copia[i_certo][cont2] == lista_var_copia[i_certo][cont2+1]:
            cont2 +=1
            indiceLinha = cont1 - volta
            nome_var_linha = lista_var_copia[i_certo][cont2-volta]
        else:
            indiceLinha = -1
            verificacao = False
            break
    cont2 = 0
    nome_var_coluna = ''
    while cont2 < len(lista_var_copia):
        if lista_var_copia[i_certo][cont2] == lista_var_copia[i_certo][cont2+1]:
            cont2 +=1
            indiceLinha = cont1
        else:
            indiceLinha = -1
            verificacao = False
            break      
    print(nome_var_linha)
    if verificacao and indiceLinha != 's':
        print(indiceLinha)
        valor_var = S[indiceLinha] / len(lista_var_copia[indiceLinha])
        S[indiceLinha] = S[indiceLinha] - valor_var
        variaveis[nome_var_linha] = valor_var
        lista_var_copia.pop(indiceLinha)
    elif verificacao and indiceColuna != 's':
        pass
    print()
    print(lista_var_copia)
    print(S)
    print(variaveis)

    cont1 += 1
    volta += 1

print(xs)