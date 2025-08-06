Dona Formiga é uma ótima trabalhadora e todos os dias coleta muitas folhas para seu formigueiro. Mas no final de semana, quando todas as outras formigas estão descansando, ela gosta de se divertir escorregando pelos túneis do formigueiro.

O formigueiro de Dona Formiga tem muitos túneis e salões. Cada túnel conecta exatamente dois salões diferentes. Cada salão está em uma altura no formigueiro. Se existe um túnel ligando um salão I a um salão J e o salão I está a uma altura maior do que o salão J, então Dona Formiga pode escorregar do salão I para o salão J usando esse túnel.

Dados o mapa dos túneis do formigueiro, as alturas em que estão os salões e o salão de onde Dona Formiga quer partir, escreva um programa para determinar o maior número de salões que ela pode visitar (não contando o salão do qual ela parte), usando túneis exclusivamente para escorregar entre os salões.

Entrada

A primeira linha da entrada contém três inteiros S, T e P, respectivamente o número de salões, o número de túneis e o salão do formigueiro do qual Dona Formiga quer partir. Os salões são numerados de 1 a S. A segunda linha contém S números inteiros Ai, a altura em que o salão i está no formigueiro. Cada uma das T linhas seguintes contém dois inteiros I e J, indicando que há um túnel entre o salão I e o salão J.

Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, o maior número de salões que Dona Formiga pode visitar (não contando o salão do qual ela parte), usando os túneis exclusivamente para escorregar entre os salões do formigueiro.

Restrições

- 1 ≤ S ≤ 200
- 1 ≤ T ≤ S × (S-1)/2
- 1 ≤ P ≤ S
- -1000 ≤ Ai ≤ 1000 para 1 ≤ i ≤ S
- 1 ≤ I < J ≤ S