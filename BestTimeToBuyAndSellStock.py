"""
  @Author: Doğan Seyfi Şen
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0] #At first, we assume that the zeroth index is the minimum
        maxProfit = 0
        
        for i in range(1, len(prices)): #We elliminate that the 0th one and search others on the list
            if prices[i] < minPrice: #If one of them is lower than recent minPrice
                minPrice = prices[i] #We change old value with the new minimum
            else:
                maxProfit = max(maxProfit, prices[i] - minPrice) #And we try to find that the max. profit among other potential max. profits
        
        return maxProfit
