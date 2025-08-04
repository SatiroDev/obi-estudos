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
quantidadeFinal = l * c
def dar_bom_por_favor(quantidade):
    voltaC = 0
    cont1C = 0
    cont2C = 0
    contColunaC = 0
    quantidadeFinal = quantidade
    
    

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
        
        for indi in range(len(lista_var_copia)-1):
            if len(lista_var_copia[indi]) == 1:
                nome_var_linha = lista_var_copia[indi][0]

                lista_var_copia.remove(lista_var_copia[indi])

                variaveis_achadas.append(nome_var_linha)
                valor_var = S[cont1C]
                xs[cont1C] -= valor_var
                S[cont1C] -= valor_var
                variaveis[nome_var_linha] = valor_var

        if verificacaoLinha == True and indiceLinha != 's':
            
            valor_var = S[cont2C+1] / len(lista_var_copia[i])
            print('VALOR',valor_var)
            S.remove(S[cont2C+1])
            print(xs[cont1C])
            xs[cont1C] -= valor_var
            variaveis[nome_var_linha] = valor_var
            lista_var_copia.pop(indiceLinha)
            variaveis_achadas.append(nome_var_linha)
            for ind in range(len(lista_var_copia[0])):
                for lista in lista_var_copia:

                    if lista[ind] == nome_var_linha:
                        S.remove(S[ind])
                        xs[ind] -= valor_var
        elif verificacaoColuna and indiceColuna != 's':

            valor_var = xs[indiceColuna] / len(lista_var_copia)
            S[indiceColuna] -= valor_var
            variaveis[nome_var_coluna] = valor_var
            variaveis_achadas.append(nome_var_coluna)

            for linha in range(len(lista_var_copia)):
                lista_var_copia[linha].pop(indiceColuna)
                if linha == len(lista_var_copia)-1:
                    xs.remove(xs[indiceColuna])
                    break
            for ind in range(len(lista_var_copia[0])):
                print(lista_var_copia)
                for lista in lista_var_copia:

                    if lista[ind] == nome_var_coluna:
                        S[ind] -= valor_var
                        xs.remove(xs[ind])
        voltaC += 1
        for index in range(len(lista_var_copia)):

    
            for lista in range(len(lista_var_copia[index])-1):
                
                if len(lista_var_copia[index]) > 0:
                    if lista_var_copia[index][0] in variaveis_achadas:
                        valor = variaveis[lista_var_copia[index][0]]
                        lista_var_copia[index].remove(lista_var_copia[index][0])
                        S[lista] -= valor
                        xs[lista] -= valor

            if quantidadeFinal == 1:
                nome = lista_var_copia[0][0]
                print(xs)

                variaveis[nome] = S[0]
                    
                print('NOME', nome)

        quantidadeFinal -= 1


    if  quantidadeFinal == 0:

        return 'deu certo'
    else:
        return dar_bom_por_favor(quantidadeFinal)
ind = 0

dar_bom_por_favor(quantidadeFinal)

for k, v in variaveis.items():
    print(k, v)
