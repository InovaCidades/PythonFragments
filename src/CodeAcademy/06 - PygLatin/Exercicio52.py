#Use and to add a second condition to your if statement. In addition to your existing check that the string contains characters, you should also use .isalpha() to make sure that it only contains letters.

#Don't forget to keep the colon at the end of the if statement!

print 'Welcome to the Pig Latin Translator!'

original = raw_input("Enter a word:")

if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"
