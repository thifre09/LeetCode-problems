from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    lista = nums1
    for i in range(len2):
        lista.append(nums2[i])
    lista.sort()
    if (len1+len2) % 2 == 0:
        return (lista[int((len1+len2)/2)] + lista[int((len1+len2)/2)-1]) / 2
    elif (len1+len2) % 2 == 1:
        return float(lista[int((len1+len2)/2)])

print(findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))