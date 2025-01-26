class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            "": 0,
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        retorno = 0

        for i,cha in enumerate(s):
            if cha == "I":
                try:
                    if s[i+1] == "V" or s[i+1] == "X":
                        retorno -= 1
                    else:
                        retorno += hmap[cha]
                except:
                    retorno += hmap[cha]
            elif cha == "X":
                try:
                    if s[i+1] == "L" or s[i+1] == "C":
                        retorno -= 10
                    else:
                        retorno += hmap[cha]
                except:
                    retorno += hmap[cha]
            elif cha == "C":
                try:
                    if s[i+1] == "D" or s[i+1] == "M":
                        retorno -= 100
                    else:
                        retorno += hmap[cha]
                except:
                    retorno += hmap[cha]
            else:
                retorno += hmap[cha]

        return retorno
    
def intToRoman(num: int) -> str:
        hmap = {
            0: "",
            1: 'I',
            2: "II",
            3: "III",
            4: 'IV',
            5: 'V',
            6: "VI",
            7: "VII",
            8: "VIII",
            9: 'IX',
            10: 'X',
            20: "XX",
            30: "XXX",
            40: 'XL',
            50: 'L',
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: 'XC',
            100: 'C',
            200: "CC",
            300: "CCC",
            400: 'CD',
            500: 'D',
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: 'CM',
            1000: 'M',
            2000: "MM",
            3000: "MMM"
        }

        strnum = str(num)
        retorno = ""
        lennum = len(strnum) - 1

        for cha in strnum:
            retorno += hmap[(int(cha) * (10 ** lennum))]
            lennum -= 1

        return retorno


teste = Solution()
for i in range(4000):
    valor = intToRoman(i)
    print(teste.romanToInt(valor))