class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            first we set area to 0
            enumerate through heights
            i = 0 and j = len(heights) - 1
            while i < j
            curr = height * width
            if the curr > area
            area = curr
            if heights[i] < heights[j]
            i+=1
            otherwise j-=1
            return area at end
        '''

        area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            curr = min(heights[i], heights[j]) * (j - i)
            if curr > area:
                area = curr
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return area
            
      


        