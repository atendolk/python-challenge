# Modules
import os

# Set file path
#txtpath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyParagraph\\raw_data\\paragraph_1.txt"
txtpath = os.path.join("Zip","PyParagraph","raw_data","paragraph_1.txt")

#paragraph = open(txtpath,'r')
num_words = 0
num_sentences = 0
num_chars = 0
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
        num_chars += len(line)


        lines += 1

        if line.startswith('\n'):
            blanklines += 1
        else:
    # assume that each sentence ends with . or ! or ?
    # so simply count these characters
            sentences += line.count('.') + line.count('!') + line.count('?')
         #Average word lenght
    average_chars = num_chars/num_words

        #Average sentence lenght
    average_sentence = num_words/sentences

    # create a list of words
    # use None to split at any whitespace regardless of length
    # so for instance double space counts as one space


print("Number of words: " + str(num_words))
print("Number of sentences: " + str(sentences))
print("Average letter count: " + str(average_chars))
print("Average sentence lenght: "+str(average_sentence))

file_output = "mainParagraph.txt"
with open(file_output, "w") as txt_file:
    txt_file.write("Number of words: ")
    txt_file.write(str(num_words))
    txt_file.write("\n")
    txt_file.write("Number of Sentences: ")
    txt_file.write(str(sentences))
    txt_file.write("\n")
    txt_file.write("Average Letter Count: ")
    txt_file.write(str(average_chars))
    txt_file.write("\n")
    txt_file.write("Average Sentence Count: ")
    txt_file.write(str(average_sentence))
    # txt_file.write("\n")
    # txt_file.write("Greatest Decrease: ")
    # txt_file.write(ddate + " $"+str(greatest_decrease))
