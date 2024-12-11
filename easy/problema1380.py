from typing import List

def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    algo: list = []
    for lin in matrix:
        algo.append(min(lin))
        
    resposta_lista, resposta_num = [], max(algo)

    for i, lin in enumerate(matrix):
        for j,num in enumerate(lin):
            if num == max(algo):
                index_col = j

    maior_resposta_coluna = max([linha[index_col] for linha in matrix])

    if resposta_num == maior_resposta_coluna:
        resposta_lista.append(resposta_num)
        return resposta_lista
    else:
        return []
