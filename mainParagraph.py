# Modules
import os

# Set file path
txtpath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyParagraph\\raw_data\\paragraph_1.txt"

#paragraph = open(txtpath,'r')
words = 0
average = 0
lines = 0
sentences = 0
num_words = 0
with open(txtpath) as paragraph:
    #Find out word count
    #print (paragraph.read())
    for line in paragraph:
        words = line.split()
        num_words += len(words)



        lines += 1

        if line.startswith('\n'):
            blanklines += 1
        else:
    # assume that each sentence ends with . or ! or ?
    # so simply count these characters
            sentences += line.count('.') + line.count('!') + line.count('?')
        

    # create a list of words
    # use None to split at any whitespace regardless of length
    # so for instance double space counts as one space


print("Number of words: " + str(num_words))
print("Number of sentences: " + str(sentences))
