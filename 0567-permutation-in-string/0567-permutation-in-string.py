class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Fixed Length SLiding window
        # Maintain two hmaps with the frequencies of the elements in s1 and for the window of s2

        # Take the complement of the problem - there are n! permutations of s1, checking every permutation will be very costly
        # but we can check if the s2 contain any consecutive sqequence of characters of s1 as its a Decision Problem

        # DC: As the ith index in s2, i will see if i belong to any charachter in s1 or not 
        # And whehter i have occurred previously in s2 (use hashmap with freq for that)

        s1_hmap = {}
        hmap = {}
        k = len(s1)
        n = len(s2)

        # Edge case
        if n < k:
            return False
            
        for i in range(len(s1)):
            if s1[i] in s1_hmap:
                s1_hmap[s1[i]] += 1
            else:
                s1_hmap[s1[i]] = 1
        
        for i in range(k):
            if s2[i] in hmap:
                hmap[s2[i]] += 1
            else:
                hmap[s2[i]] = 1
        if (hmap == s1_hmap):
                return True
        
        for i in range(k, n):
            # if ith element belongs to hmap already else add it
            if(s2[i] in hmap):
                hmap[s2[i]] += 1
            else:
                hmap[s2[i]] = 1

            # if i-k th ele belongs to hmap, reduce its freq    
            # if(s2[i-k] in hmap): #this if is redundant as it will always belong
            hmap[s2[i-k]] -= 1 
            if(hmap[s2[i-k]] == 0): #since we have to maintain the elements only present in our window
                del hmap[s2[i-k]]

            if (hmap == s1_hmap):
                return True

        return False









        