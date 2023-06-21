

class Solution(object):
    def romanToInt(self, s: str):
        roman = {
            'I': 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        number = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[(i + 1)]]:
                number -= roman[s[i]]
            else:
                number += roman[s[i]]
        return number + roman[s[-1]]

    """ 
    : type s: str
    :rtype: int
    """



class Solution:
    def fizzBuzz(self, n: int):
        list_ = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                list_.append("fizzBuzz")
            elif i % 3 == 0:
                list_.append("fizz")
            elif i % 5 == 0:
                list_.append("Buzz")
            else:
                list_.append(str(i))
        return list_




class Solution:
    def twoSum(self, nums: list, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j





class Solution:
    def IsPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False





class Solution:
    def longestCommonPrefix(self, strs: list):
        stts = ""
        for i in strs[0]:
            for j in strs:
                if i in j:
                    stts += i
        return stts