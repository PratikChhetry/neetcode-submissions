class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_str = 1
        l, r = 0, 1

        if len(s) == 0:
            return 0
        else:
            seen[s[0]] = 1
        
        while r < len(s):
            if s[r] in seen and seen[s[r]] > 0:
                seen[s[l]] -= 1
                l += 1

            else:
                seen[s[r]] = 1
                max_str = max(max_str, r - l + 1)
                r += 1
            
        return max_str
            


        


            

            

            


        
            
            

            
