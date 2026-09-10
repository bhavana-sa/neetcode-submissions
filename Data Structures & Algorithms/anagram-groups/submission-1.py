class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #Passing list as a default factory ensures that if a key doesn't exist yet, Python automatically creates it with an empty list ([])
        for string in strs:
            sortedA = "".join(sorted(string)) # Timsort - algorithm from Merge Sort and Insertion Sort
            #Sorts the characters of the string alphabetically and merges them back into a single string, stored in sortedA
            result[sortedA].append(string) #Uses the sorted string sortedA as the dictionary key and appends the original string s to that key's list.Because all anagrams  become identical when sorted ("aet"), they will all map to this exact same key and group together.
        return list(result.values()) #Extracts all the grouped lists from the dictionary and packages them into a standard Python list




        