class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
            S and T
            Returns true if s and t share all the same letters
            Brute force solution would be to iterate through both arrays
            Find the common letters and remove it.
            Check if both strings are "" and if so then return true otherwise false
        
            Initializing the set of s and turn it into a list with list()
            Go through t and find each letter within s and remove it from s
            If it doesn't return false then it's true
        '''


        for char in t:
            if s.find(char) == -1:
                return False
            s = s.replace(char, "", 1)
        if s == "":
            return True
        else:
            return False
        