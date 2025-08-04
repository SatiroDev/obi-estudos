L, C = input().split()

l, c = int(L), int(C)
variaveis = {}
lista_var = []
xs = []
S = []
variaveis_achadas = []

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
                    variaveis[var[indice]] = '0'
                sub_var.append(var[indice])
            lista_var.append(sub_var)
            
lista_var_copia = lista_var

# print(variaveis)
# while len(lista_var_copia) > 0:
def dar_bom_por_favor():
    voltaC = 0
    cont1C = 0
    cont2C = 0
    contColunaC = 0

    for i in range(len(lista_var_copia)):


        verificacaoLinha = True
        indiceLinha = 's'
        indiceColuna = 's'
        nome_var_linha = ''
        
        while cont2C < len(lista_var_copia[0])-1:

            if len(lista_var_copia[0]) != 1 and len(lista_var_copia[0]) != 0:

                
                if lista_var_copia[i][cont2C] == lista_var_copia[i][cont2C+1]:

                    
                    indiceLinha = i


                    nome_var_linha = lista_var_copia[i][cont2C]
                    
                else:
                    indiceLinha = -1
                    verificacaoLinha = False
                    break
            else:
                verificacaoLinha = False
            cont2C += 1
            
        nome_var_coluna = ''
        
        # while contColunaC < len(lista_var_copia):
        #     linhas = len(lista_var_copia)
        #     colunas = len(lista_var_copia[0])
        verificacaoColuna = True
        for lin in range(len(lista_var_copia)-1):
            if contColunaC < len(lista_var_copia[0]):
                if lista_var_copia[lin][contColunaC] == lista_var_copia[lin+1][contColunaC]:
                    indiceColuna = contColunaC

                    nome_var_coluna = lista_var_copia[lin][contColunaC]
                else:
                    contColunaC += 1  
                    verificacaoColuna = False
                    break  
        

        if verificacaoLinha == True and indiceLinha != 's':
            print(verificacaoLinha)
            valor_var = S[cont1C] / len(lista_var_copia[i])
            S.remove(S[cont1C])
            xs[cont1C] -= valor_var
            variaveis[nome_var_linha] = valor_var
            lista_var_copia.pop(indiceLinha)
            variaveis_achadas.append(nome_var_linha)
            # for ind in range(len(lista_var_copia[0])):
            #     for lista in lista_var_copia:

            #         if lista[ind] == nome_var_linha:
            #             S[ind] -= valor_var
            #             xs[ind] -= valor_var
        elif verificacaoColuna and indiceColuna != 's':

            valor_var = xs[indiceColuna] / len(lista_var_copia)
            S[indiceColuna] -= valor_var
            variaveis[nome_var_coluna] = valor_var
            variaveis_achadas.append(nome_var_coluna)

            for linha in range(len(lista_var_copia)):
                lista_var_copia[linha].pop(indiceColuna)
                if linha == len(lista_var_copia)-1:
                    xs.remove(xs[indiceColuna])
            # for ind in range(len(lista_var_copia[0])):
            #     for lista in lista_var_copia:

            #         if lista[ind] == nome_var_coluna:
            #             S[ind] -= valor_var
            #             xs[ind] -= valor_var
        voltaC += 1
        for index in range(len(lista_var_copia)):
            conta = 0
            for lista in range(len(lista_var_copia[index][0])):
                print(lista_var_copia)
                print()
                print(conta)
                print(lista)
                print(lista_var_copia[lista][conta])
                if lista_var_copia[lista][conta] in variaveis_achadas:
                    lista_var_copia.remove(lista_var_copia[lista][conta])
                conta += 1

    if len(lista_var_copia) == 1:
        return 'deu certo'
    else:
        for lista in lista_var_copia:
            print(lista)
        print()
        return dar_bom_por_favor()
ind = 0

dar_bom_por_favor()

print(S)
print(xs)
for k, v in variaveis.items():
    print(k, v)
