class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Given integer array prices 
            prices[i] is the price of NeetCoin on the ith day
            set two pointers l and r to 0 and 1.
            l is buy r is sell
            Set maxDif = 0. 
            We need to iterate through the array and find lowest and highest.
            first check if l < r if not then make l = r
            if yes, then find the max between maxDif and r - l and set that as maxDif
            make r = r+1
            return maxDif

        '''

        l, r = 0, 1
        maxDif = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                maxDif = max(maxDif, prices[r] - prices[l])
            r += 1
        
        return maxDif
        