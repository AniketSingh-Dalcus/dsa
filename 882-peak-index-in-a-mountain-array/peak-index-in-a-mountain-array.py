class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left = 1 # start value will never be peak so start with 2nd value
        right = len(arr) - 2 # end value will never be peak so end with 2nd last value
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]: # peak found
                return mid
            if arr[mid-1] < arr[mid]: # inc order => go right
                left = mid+1
            if arr[mid] > arr[mid+1]: # dec order => go left
                right = mid-1
        