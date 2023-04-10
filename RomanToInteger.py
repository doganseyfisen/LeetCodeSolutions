"""
  @Author: Doğan Seyfi Şen
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        firstSum = 0
        for i in range(len(s) - 1, -1, -1): # inputStr (s) uzunlugundan 0'a kadar azalir, indeks icin
            number = romanDict[s[i]] # inputStr'in i'inci elemanini bulur ve onun dict'teki karsiligini yani value dondurur
            if 4 * number < firstSum: # eger value * 4 firstSum'dan kucukse yani value == 1 ve firstSum == 5 ise bu "IV, 4" demektir, bu yuzden cikarma yapilir
                firstSum = firstSum - number
            else:
                firstSum = firstSum + number
        return firstSum
