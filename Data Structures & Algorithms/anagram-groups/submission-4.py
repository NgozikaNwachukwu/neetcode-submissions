class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i first have to create an operation that is going to sort all the items in the list
        # append all t strings to the correct key
        my_dict = {}
        
        #im going to iterate through the list and say if sorted string in dictionary append
        for string in strs:
            letter_sort = "".join(sorted(string)) # we need to actually sort it first instead of trying to sort via the dictionary
            if letter_sort in my_dict:
                my_dict[letter_sort].append(string) 
                #this allows us to add multiple values to the key, e.g {'fruit': ['apple', 'banana']}
            else:
                my_dict[letter_sort] = [string] # adds the string value to the sorted key
        return list(my_dict.values()) # returns all the values (that are each in lists) in list form