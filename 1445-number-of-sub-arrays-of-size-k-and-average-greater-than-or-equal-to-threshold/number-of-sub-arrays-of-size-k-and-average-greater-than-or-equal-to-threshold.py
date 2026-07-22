class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        res = 0
        curSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]

            if (curSum / k) >= threshold:
                res += 1

            curSum -= arr[L]

        return res


        