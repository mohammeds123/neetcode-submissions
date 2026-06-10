class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum = numbers[left] + numbers[right]
        while sum != target and left < right:
            if sum > target and left < right:
                right-=1
            elif sum < target and left < right:
                left += 1
            sum = numbers[left] + numbers[right]
        return [left+1, right+1]