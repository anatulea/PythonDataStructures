def rev_words(s):
    words = []
    length = len(s)
    spaces =[' ']

    i=0
    while i < length:
        if s[i] not in spaces: # if the element at index i from the string is not a " "(space):
            word_start = i
            while i < length and s[i] not in spaces: # keep going until we find nother space
                i+=1
            words.append(s[word_start:i]) # append all the elements/ letters from the first space to the next space
        i+=1
    return " ".join(reversed(words)) # join the words list together as a string with spaces between letters in a reverse order

print(rev_words("     hello, it's me     "))