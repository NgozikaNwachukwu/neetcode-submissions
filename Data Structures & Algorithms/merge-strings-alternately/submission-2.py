class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        res.append(word1[i:])
        res.append(word2[j:])

        # what this means is [start : stop]
        # if its [:] it means starting at the beginning of the list and stoping at the end of the list
        # you can specify e.g [i:] means stsrting at index i and stopping at the end
        # [:j] means starting at the first element and ending at index j
        # so for this problem, one string can be longer than the other
        # so if thats the case saying res.append(word1[i:]) will append the letters
        # starting at index i and stopping at the END of the string(aka the remaining letters)
        # since we will be incrementing the pointers, where it ends up will be the reminants
        #same goes for res.append(word1[j:]) for the j pointer. if lets say index i or j is past the last element(out of bounds)
        # it will append nothing but if the index is in bounds itll append the remaining. so its just a safety check

        return "".join(res)