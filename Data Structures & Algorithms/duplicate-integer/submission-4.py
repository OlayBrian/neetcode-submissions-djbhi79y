class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSeen = []

        for i in nums:
            if i in numSeen:
                return True
            numSeen.append(i)
        return False