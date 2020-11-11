'''
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

def string_compression(s):
    table = {}
    result = []
    for i in s:
        if i not in table:
             table[i] = 1
        else:
            table[i]+=1
    
    for k, v in table.items():
        result.append(k)
        result.append(str(v))  

    return  ''.join(result)

print(string_compression('AAAAAABBABEEEDDDdd')) #A7B3E3D3d2

# run length compression algorithm
def compress(s):
    run = ""
    length = len(s)

    if length == 0:
        return ''
    
    if length == 1:
        return s+'1'
    
    last = s[0] 
    count = 1
    idx = 1

    while idx < length:
        if s[idx] == s[idx-1]:
            count += 1
        else:
            run = run + s[idx-1]+str(count)
            count = 1
        idx += 1
    run = run + s[idx-1] + str(count)
    return run
print(compress('AAAAAABBABEEEDDDdd')) # A6B2A1B1E3D3d2