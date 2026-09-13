class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #If two strings have different lengths, they cannot possibly be anagrams
            return False

        countS, countt = {},{} #Create two dictionaries, countS → character frequencies in s countT → character frequencies in t
        for i in range(len(s)): #Loop through the string
            countS[s[i]] = 1 + countS.get(s[i], 0) #frequency-counting pattern
            countt[t[i]] = 1 + countt.get(t[i], 0)
        return countS == countt #Python can directly compare dictionaries.
        

#for i in range(len(s)): here why are we only looping through s and not t? Because we already checked in line 3 if the length is same. So at this point, we know s and t have the same length.
