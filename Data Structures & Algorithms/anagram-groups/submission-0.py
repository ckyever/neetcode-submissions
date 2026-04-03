class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #for word in strs
        #    add word to sublist
        #    compare each word to the other words
        #    if it is an anagram add to sublist
        #    if we reach end of strs we have found all anagrams
        #    add sublist to final list
        #    go to first word in the list
        #    continue until no words remain in strs
        groupedAnagrams = []

        while len(strs) > 0:
            # Pop first word in strs
            sublist = [strs.pop(0)]

            # Only one word remains so immediately add sublist
            if not strs:
                groupedAnagrams.append(sublist)
                break

            referenceWord = ''.join(sorted(sublist[0]))

            # Find all words still in strs that are anagrams
            i = 0
            while i < len(strs):
                anagramCheck = ''.join(sorted(strs[i]))

                # If we find an anagram pop the word and ensure loop still looks at the next word
                if anagramCheck == referenceWord:
                    sublist.append(strs.pop(i))
                else:
                    i += 1

            groupedAnagrams.append(sublist)

        return groupedAnagrams

            
                
                    
