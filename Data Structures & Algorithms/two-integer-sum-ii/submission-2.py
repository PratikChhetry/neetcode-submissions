class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            total = numbers[j] + numbers[i]
            if total > target:
                j -= 1
            elif total < target:
                i += 1
            else:
                arr = [i+1, j+1]
                return arr
        return []

'''
    1, 2, 2, 2, 4, 6 tar = 5
    i = beginning
    j starts at the end
    1 + 6 > target
    decrease the j


'''

        