class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if f'{nums[j]}{nums[j+1]}' < f'{nums[j+1]}{nums[j]}':
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return str(int("".join(map(str,nums))))