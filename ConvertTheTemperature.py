"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        answer = []
        into_kelvin = celsius + 273.15
        into_fahrenheit = celsius * 1.80 + 32.00
        answer.append(into_kelvin)
        answer.append(into_fahrenheit)
        
        return answer
