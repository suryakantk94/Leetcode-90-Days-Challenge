class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Fixed length Sliding Window
        # DC - as an ith element, i will check if i am a vowel or not, if i am then increase the count
        # I will expect from my subordinates to have the maxcount till their index
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in range(k):
            if s[i] in vowels:
                count += 1

        maxCount = count 
        n = len(s)
        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            maxCount = max(count, maxCount)    
        return maxCount