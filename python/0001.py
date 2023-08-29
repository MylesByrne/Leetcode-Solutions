# Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    mem = []

    for i in range(len(nums)):
        if target - nums[i] in mem:
            return [i, nums.index(target - nums[i])]

        else:
            mem.append(nums[i])

    return []
