class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        result = [0, 0]
        count = 0
        for i in range(len(nums)):
            hashtable[nums[i]] = count
            count += 1
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in hashtable and hashtable[diff] != j:
                result[0] = j
                result[1] = hashtable.get(diff)
                break
        return result
