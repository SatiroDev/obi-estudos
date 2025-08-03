Desafios de lógica e matemática são um ótimo passatempo, atraindo um grande número de praticantes, e um mercado que envolve aplicativos para celular, atividades on-line, revistas especializadas e até mesmo cursos na internet para melhorar o desempenho!

Neste problema sua tarefa é escrever um programa que resolva um novo passatempo, mostrado na figura abaixo. O passatempo é composto por um quadriculado com letras dentro de cada célula e números ao lado de cada linha ou coluna do quadriculado. As letras dentro de cada célula representam variáveis, e os números representam as somas dos valores das variáveis em cada linha ou coluna.


O objetivo desse passatempo é determinar o valor de cada variável de modo a satisfazer as somas das linhas e colunas mostradas. Para permitir que um número maior de pessoas consiga resolver o passatempo, ele tem uma propriedade que facilita a sua solução: sempre é possível encontrar uma linha ou coluna em que há apenas uma variável cujo valor ainda é desconhecido. Assim, uma possível maneira de resolver o problema é, a cada passo da solução, encontrar o valor de uma variável.

Sua tarefa é, dado um passatempo, determinar os valores das variáveis que o solucionam.

Entrada
A primeira linha contém dois inteiros L e C indicando o número de linhas e o número de colunas do passatempo. Cada uma das L linhas seguintes contém C nomes de variáveis, seguidos de um inteiro S, a soma resultante das variáveis dessa linha. A última linha contém C inteiros Xi, indicando respectivamente a soma das variáveis na coluna i. Nomes de variáveis são formados por precisamente duas letras minúsculas, de 'a' a 'z'. Todos os passatempos têm solução única, em que todas as variáveis são números inteiros.

Saída
Seu programa deve produzir uma linha para cada variável do passatempo, contendo o nome da variável e o seu valor inteiro. As variáveis devem ser escritas em ordem alfabética crescente, ou seja, respeitando a ordem aa, ab, …, az, ba, bb, …, za, zb, …, zz.
Restrições
1 ≤ L ≤ 100
2 ≤ C ≤ 100
-108 ≤ S ≤ 108
-108 ≤ Xi ≤ 108