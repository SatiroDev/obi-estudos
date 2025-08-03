Lista palíndroma
Uma palavra é chamada de palíndromo se a primeira letra da palavra é igual à última letra da palavra, a segunda letra é igual à penúltima letra, a terceira letra é igual à antepenúltima letra, e assim por diante. Por exemplo, as palavras osso e sopapos são palíndromos.

Nesta tarefa estamos interessados não em palavras, mas em listas de números inteiros. Nesse caso, vamos definir que uma lista é palíndroma se L[i] = L[N-i+1], onde L[i] representa o i-ésimo elemento da lista (note que nesta notação o índices variam de 1 a N).

Você pode modificar uma lista usando a operação de contração, que é definida da seguinte forma: escolha dois elementos adjacentes da lista e substitua os dois elementos por um único elemento de valor igual à soma dos elementos substituídos. Note que ao efetuar uma operação de contração o número de elementos da lista decresce de um elemento.

Dada uma lista de números inteiros, você deve escrever um programa para determinar o menor número de operações de contração que devem ser realizadas de modo que a lista resultante seja palíndroma.

Entrada
A primeira linha da entrada contém um inteiro N, o número de elementos da lista. A segunda linha contém N inteiros Li, os elementos da lista.
Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, o menor número de operações de contração necessárias para tornar a lista palíndroma.

Restrições
1 ≤ N ≤ 106
1 ≤ Li ≤ 109, para 1 ≤ i ≤ N
Informações sobre a pontuação
Para um conjunto de casos de testes valendo 30 pontos, N ≤ 10.
Para um conjunto de casos de testes valendo outros 30 pontos N ≤ 103.
Para um conjunto de casos de testes valendo outros 40 pontos, nenhuma restrição adicional.