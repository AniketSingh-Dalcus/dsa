class Solution(object):
    def maxVowels(self, s, k):
        vowel={"a","e","i","o","u"}
        curr=0
        for i in range(k):
            if s[i] in vowel:
                curr+=1
        max_val=curr
        for i in range(k,len(s)):
            if s[i] in vowel:
                curr+=1
            if s[i-k] in vowel:
                curr-=1
            max_val=max(max_val,curr)
        return max_val
            
