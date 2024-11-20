def addTwoNumbers(l1: list[int], l2: list[int]) -> list[int]:
    numl1 = 0
    numl2 = 0
    resultado = []
    for i in range(len(l1)):
        numl1 += (10 ** i) * l1[i]
    for i in range(len(l2)):
        numl2 += (10 ** i) * l2[i]
    soma = numl1 + numl2
    for digito in str(soma):
        resultado.append(int(digito))
    return resultado