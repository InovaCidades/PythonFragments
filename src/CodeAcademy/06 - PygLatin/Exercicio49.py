#Set new_word equal to the slice from the 1st index all the way to the end of new_word. Use [1:len(new_word)] to do this.

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    
    new_word = word + first + pyg
    
    print original
else:
    print 'empty'