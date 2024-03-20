# Projeto Caixeiro viajante
## Descrição
 O Problema do Caixeiro Viajante (PCV) é um problema clássico de otimização combinatória, onde o objetivo é encontrar o menor caminho que visita cada cidade exatamente uma vez e retorna à cidade de origem. Este projeto tem como objetivo aplicar a teoria dos grafos para resolver o PCV. Cada cidade será representada por um nó no grafo, e as arestas entre os nós representarão as conexões entre as cidades, com a ponderação das arestas sendo a distância entre as cidades.

## Bases de Dados

O projeto trabalhará com as seguintes bases de dados:
- *ATT48*
- *DANTZIG42*
- *FRI26*
- *GR17*
- *P01*

Os valores das soluções para cada base de dados estão indicados na página da base de dados.

## Software necessário
O projeto foi desenvolvido usando Python 3.11.6.

## Como Usar
1. Na seção <> Code:
   Faça o download ZIP do código

2. Em seguida, desempacote o arquivo zip.

3. Abra a pasta no VSCode.

4. Por fim, rode o código do arquivo (Geral.py) utilizando o seguinte comando:
   python Geral.py //Exemplo, pois pode rodar os outros códigos disponíveis.


## Algoritmos

Serão implementados inicialmente programas para ler e armazenar as informações numa estrutura de dados(nesse caso, utilizamos um dicionário). Logo em seguida, serão implementados algoritmos para encontrar os caminhos mínimos para cada base de dados. Os resultados serão comparados com os valores conhecidos de solução para avaliação da eficácia dos algoritmos.

## Resultados obtidos:
| Algoritmo     | Base de Dados | Peso Total | Valor Esperado |
|---------------|---------------|------------|----------------|
| Prim          | ATT48         | 27670      | 27670          |
| Prim          | DANTZIG42     | 591        | 591            |
| Prim          | FRI26         | 741        | 741            |
| Prim          | GR17          | 1421       | 1421           |
| Prim          | P01           | 260        | 260            |
| Dijkstra      | ATT48         | 35235.0    | 33523          |
| Dijkstra      | DANTZIG42     | 699        | 699            |
| Dijkstra      | FRI26         | 1436.0     | 937            |
| Dijkstra      | GR17          | -          | 2085           |
| Dijkstra      | P01           | -          | 291            |
| Força Bruta   | ATT48         | -          | 33523          |
| Força Bruta   | DANTZIG42     | -          | 699            |
| Força Bruta   | FRI26         | -          | 937            |
| Força Bruta   | GR17          | -          | 2085           |
| Força Bruta   | P01           | -          | 291            |
| Christofides  | ATT48         | 1176       | 33523          |
| Christofides  | DANTZIG42     | 3393       | 699            |
| Christofides  | FRI26         | 3322       | 937            |
| Christofides  | GR17          | 6759       | 2085           |
| Christofides  | P01           | 761        | 291            |


## Licença MIT

Direitos autorais (c)  2024 João Carlos

É concedida permissão, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e arquivos de documentação associados (o "Software"), para lidar
no Software sem restrições, incluindo, sem limitação, os direitos
usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender
cópias do Software e permitir que as pessoas a quem o Software é
capacitado para fazê-lo, sujeito às seguintes condições:

O aviso de direitos autorais acima e este aviso de permissão serão incluídos em todos
cópias ou partes substanciais do Software.

**O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITAS, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM HIPÓTESE ALGUMA
OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRAS
RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ATO ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE,
FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO
PROGRAMAS.**

## Hardware sugerido
Processador 2.6 GHz Intel Core i7, com 16 GB 1600 MHz DDR3 e HD 1TB.

## Software necessário
Todo o projeto está rodando em python 3.10

## Contato dos Desenvolvedores

1. João Carlos joaocar2003@gmail.com
1. Isaac Kawan isaakawan123456@gmail.com
1. Ana Beatriz beatriz.ana.silva1006@gmail.com
1. Liedson Santos liedson146@gmail.com
