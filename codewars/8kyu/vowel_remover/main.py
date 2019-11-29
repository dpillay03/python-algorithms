# Create a function called shortcut to remove all the lowercase vowels in a given string.

def shortcut( s ):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in s.lower():
        if i in vowels:
            s = s.replace(i, "")
    return s