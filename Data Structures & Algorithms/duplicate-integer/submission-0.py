class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            Brute force solution: nested loop. Iterate two loops and an element
            at nums[i] and nums[j] are equal, return false. O(n^2)

            Hashmap -> start with empty hash. Enumerate through the array
            Check if the current value is in hashmap
            if so, return false
            add the value to the hash after the if statement. 
            Return true at the end of the for loop
        
        '''

        seen = {}      # Empty Hash

        for num in nums:  # Going to iterate through nums and give index
            if num in seen:
                return True
            seen[num] = num   # We are mapping to itself

        return False


        