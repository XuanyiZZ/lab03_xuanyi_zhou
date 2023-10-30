# lab03.py
'''
You will write five recursive functions for this lab.
Note: You must write each function recursively in order to
receive any credit, even if Gradescope’s tests pass.
For this lab, you may not (and need not) define additional
helper functions.
'''


'''
The parameters n and k are positive integers (you may assume
n is >= 0 and k is > 0). This function recursively returns
the quotient (n // k) without explicitly using
the // or / operators, or a pre-defined function.
Idea: turn division/multiplication into substraction/addtion
'''
def integerDivision(n, k):
    if n < k:
        return 0 # Base case
    else:
        return 1 + integerDivision(n-k, k) # get one k out of n, continue


'''
The parameter listOfInt is a list containing positive integer values. This
function will return a list containing only even values in listOfInt in
the order that they appear in listOfInt. If there are no even values in
listOfInt, then this function should return an empty list.
Idea: remove odd numbers in listOfInt untill the last element
Special case here might be a list contians only odd numbers!
For this case, we need to return an empty list!
'''
def collectEvenInts(listOfInt):
    if len(listOfInt) != 0:
        if listOfInt[0] % 2 == 0:
            return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
        else:
            return collectEvenInts(listOfInt[1:])
    else:
        return []

assert collectEvenInts([1,2,3,4,5]) == [2,4]



'''
This function will take a string value (someString) and return the number
of vowels (‘A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’) that exists in someString.
Idea: Similar to collectEvenInts, while here we need a number instead of list!
'''
def countVowels(someString):
    if len(someString) != 0:
        if someString[0] in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            return 1 + countVowels(someString[1:])
        else:
            return 0 + countVowels(someString[1:])
    else:
        return 0



'''
The parameter s is a string. This function will return a string in the
reverse order of s. Note that the reverse of an empty string is an empty
string.
Idea: Similar to above two functions.
Numbers are still numbers, change the last element in list to the first one!
'''
def reverseString(s):
    if len(s) != 0 :
        n = len(s)
        return s[n-1] + reverseString(s[:-1])
    else:
        return ""


'''
The parameters s and sub are strings that contain at least one
character. This function will return a string where all occurrences
of sub are removed in the order it appears in the string s
(see example test below for an interesting case).
Your solution SHOULD NOT use the string’s replace method.
Idea: s or sub to be empty?
'''
def removeSubString(s, sub):
    n = len(sub)
    if not s:
        return ""
    if s.startswith(sub):
        return removeSubString(s[n:], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)
        
    


    
