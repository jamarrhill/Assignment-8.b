# Name: Jamar Hill
# Date: 11/18/20
# Description: Assignment 8.b

"""Define both sentences as w1 and w2"""
def words_in_both(w1, w2):
    sent1 = w1.lower().split(" ")# intiates action to slip words
    sent2 = w2.lower().split(" ")
    result = [] #Combines result
    for i in sent1:
        if (i in sent2) and (i not in result):
             result.append(i)
    return result

#test
print(words_in_both("Not the comfy chair test1", "Not The comfy Chair test2"))
