class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            We have an integer array of nums
            We have an int k 
            We need to find the k most frequent elements within the array

            We can have an empty hash called count
            iterate through nums and we can update the frequency on count
            checking if that num is in count if not then we add 1

            Check the hash for the highest frequency, remove it from the hash and minus one from k. 
            Continue until k = 0 and return the new list.
        '''

        count = {}
        final = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        while k > 0: 
            final.append(max(count, key=count.get))
            count[max(count, key=count.get)] = -1
            k -= 1
        return final

        