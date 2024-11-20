lista = [1,2,3,4,5]
l2 = [6,7,8]
#[1,2,3,4,5,6,7,8]
len1 = len(lista)
len2 = len(l2)
lista.append(l2)

print(lista[int((len1+len2)/2)-1])