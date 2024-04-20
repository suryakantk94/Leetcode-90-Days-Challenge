class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        # Fixed Len SLiding window 
        # Enumeration problem
    
        #DC - as the ith index, i will see if adding myself to my subordinat's solution would make it an anagram or not 
        #if not i will pass the window with me to the next
        #if i make it, then i will add the index i-len(p) to the result array

        ans = []
        p_hmap = {}
        hmap = {}
        k = len(p)
        n = len(s)

        # Edge case
        if n < k:
            return []
            
        for i in range(k):
            if p[i] in p_hmap:
                p_hmap[p[i]] += 1
            else:
                p_hmap[p[i]] = 1
        
        for i in range(k):
            if s[i] in hmap:
                hmap[s[i]] += 1
            else:
                hmap[s[i]] = 1
        if (hmap == p_hmap):
            ans.append(0)
        
        for i in range(k, n):
            # if ith element belongs to hmap already else add it
            if(s[i] in hmap):
                hmap[s[i]] += 1
            else:
                hmap[s[i]] = 1

            # if i-k th ele belongs to hmap, reduce its freq    
            # if(s[i-k] in hmap): #this if is redundant as it will always belong
            hmap[s[i-k]] -= 1 
            if(hmap[s[i-k]] == 0): #since we have to maintain the elements only present in our window
                del hmap[s[i-k]]

            if (hmap == p_hmap):
                ans.append(i-k+1)

        return ans