from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordToInsert = ""
        before = ""
        lista: List[str] = []
        for word in words:
            if (wordToInsert == ""):
                wordToInsert += word
            else:
                wordToInsert += " " + word
            if (len(wordToInsert) > maxWidth):
                lista.append(before)
                wordToInsert = word
            before = wordToInsert
        if (not lista[-1].endswith(words[-1])):
            lista.append(wordToInsert)


        for index, line in enumerate(lista):
            while len(line) != maxWidth:
                timesAdded = 0
                for i in range(len(line)):
                    if (index == len(lista)-1):
                        tamanho = len(line)
                        lista[index] += " " * (maxWidth-tamanho)
                    else:
                        line = lista[index]
                        if (len(line) == maxWidth):
                            break
                        i+= timesAdded
                        if (line[i] == " " and not len(line.split()) == 1):
                            lista[index] = lista[index][:i] + " " + lista[index][i:]
                            timesAdded += 1
                        elif (i == len(line)-1 and len(line.split()) == 1):
                            lista[index] += " "
        return lista
    

a = Solution()
print(a.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))