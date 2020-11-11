'''
Problem¶
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
'''
def uni_char2(s):
    return len(set(s)) == len(s)

print(uni_char2('adsl')) #true
print(uni_char2('adsla')) # False

def uni_char(s):
    u = set()
    for c in s:
        if c in u:
            return False
        else:
            u.add(c)
    return True

print(uni_char('adsla')) # False