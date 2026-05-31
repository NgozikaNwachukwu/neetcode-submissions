class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = []
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                res.append(word1[i])
                res.append(word2[j])
                i += 1
                j += 1
            elif i >= len(word1) and j < len(word2):
                res.append(word2[j:])
                break # if i dont add this it causes an infinite loop
                #because for eg if len(word1) = 3 and len(word2) = 5
                #this elif block is reached once j = 3, if we append the rest
                # we cant: 1. increment j, cuz when this elif block is reached again,
                # itll append from j = 4 till the end, and then keep going till j is 
                # out of bounds. but if we just break the while loop, thats okay
                # because weve added everything we need and dont care where j or i is
                # if we dont add this break, it creates an infinite loop cuz for example
                # using the example above, j will remain at 3, and itll keep running
                # with j=3, j=3, nothing is ever done about j. so if one gets OOO, break the loop

            elif j >= len(word2) and i < len(word1):
                res.append(word1[i:])
                break
           

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