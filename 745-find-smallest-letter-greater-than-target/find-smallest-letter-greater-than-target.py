class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l=0
        h=len(letters)-1
        ans=0
        while l<=h:
            mid=(l+h)//2
            if letters[mid]>target:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return letters[ans]