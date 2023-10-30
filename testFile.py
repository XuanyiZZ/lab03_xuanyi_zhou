# testFile.py

from lab03 import integerDivision
from lab03 import collectEvenInts
from lab03 import countVowels
from lab03 import reverseString
from lab03 import removeSubString

def test_integerDivion1():
    assert integerDivision(3,4) == 0
    assert integerDivision(0,3) == 0
    assert integerDivision(0,100) == 0
    
def test_integerDivion2():
    assert integerDivision(4,4) == 1
    assert integerDivision(100,4) == 25
    assert integerDivision(14,7) == 2

def test_integerDivion3():
    assert integerDivision(15,7) == 2
    assert integerDivision(100,3) == 33
    assert integerDivision(18,4) == 4
    assert integerDivision(19,4) == 4



'''
Special case here might be a list contians only odd numbers!
For this case, we need to return an empty list!
'''
def test_collectEvenInts1():
    assert collectEvenInts([]) == []
    assert collectEvenInts([1, 3, 5, 7, 9]) == []
    assert collectEvenInts([7, 9, 11, 13]) == []
    assert collectEvenInts([3]) == []

def test_collectEvenInts2():
    assert collectEvenInts([1, 1, 1, 1]) == []
    assert collectEvenInts([1, 1, 5, 5, 7, 7]) == []

def test_collectEvenInts3():
    assert collectEvenInts([1, 2, 3, 4, 5]) == [2, 4]
    assert collectEvenInts([2, 2, 3, 5]) == [2, 2]
    assert collectEvenInts([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert collectEvenInts([7, 7, 8, 9, 10, 12]) == [8, 10, 12]



def test_countVowels1():
    assert countVowels("") == 0
    assert countVowels("Ths s strng") == 0
    assert countVowels("Thsbdngtbmf") == 0

def test_countVowels2():
    assert countVowels("I") == 1
    assert countVowels("Iiii") == 4
    assert countVowels("a e i o u AEIOU") == 10

def test_countVowels3():
    assert countVowels("What? It is IMPOSSIBLE") == 7
    assert countVowels("This is an apple") == 5
    assert countVowels("Let's go!!!!") == 2



'''
Numbers are still numbers, change the last element in list to the first one!
'''
def test_reverseString1():
    assert reverseString("") == ""
    assert reverseString("11111") == "11111"
    assert reverseString("12345") == "54321"

def test_reverseString2():
    assert reverseString("CS9CS8CS16") == "61SC8SC9SC"
    assert reverseString("!1!1") == "1!1!"
    assert reverseString("BLG WBG LNG") == "GNL GBW GLB"

def test_reverseString3():
    assert reverseString("78.78.00") == "00.87.87"
    assert reverseString("!?") == "?!"
    assert reverseString("1   7   W") == "W   7   1"


'''
Idea: s or sub to be empty?
'''
def test_removeSubString1():
    assert removeSubString("", "0") == ""
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubSting("aaa", "a") == ""

def test_removeSubString2():
    assert removeSubString("What is that?", "?") == "What is that"
    assert removeSubString("What Is that", "I") == "What s that"
    assert removeSubSting("Projectpost", "po") == "Projectst"

def test_removeSubString3():
    assert removeSubString("penpensil", "pen") == "sil"
    assert removeSubString("Penpensil", "pen") == "Pencil"
    assert removeSubSting("PenPensil", "pen") == "PenPensil"

