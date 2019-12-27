"""
Your task is very simple. Just write a function isAlphabetic(s), which takes an input string s in lowercase and returns true/false depending on whether the string is in alphabetical order or not.

For example, isAlphabetic('kata') is False as 'a' comes after 'k', but isAlphabetic('ant') is True.

Good luck :)
"""
def alphabetic(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True
  