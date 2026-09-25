class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #We create an empty dictionary
        for i, val in enumerate(nums): #enumerate() gives us both the index and the value.
            diff = target - val
            if diff in map: #Have I already seen the number I need?"
                return [map[diff],i]

            map[val] = i #This is executed if we didn't find the complement.



        