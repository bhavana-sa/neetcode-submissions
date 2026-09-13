class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #creates an empty set, We're going to use it to remember numbers we've already encountered
        for num in nums: #loops through each number in the input list
            if num in seen: #This asks:"Have I already encountered this number?"
                return True 
            else:
                seen.add(num) #If the number wasn't already in seen, we add it.
        return False #This happens after the entire list has been checked.If we make it through the entire loop without finding