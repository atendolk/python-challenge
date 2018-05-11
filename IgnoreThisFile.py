import os
import csv
# csvpath = "os.path.join('..','PyBank','raw_data','budget_data_1.csv')
#filepath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyBank\\raw_data\\budget_data_1.csv"
#filepath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyBank\\raw_data\\budget_data_1.csv"
#IF YOU UNCOMMENT THE LINE ABOVE THE DATA BELOW WILL RUN THROUGH BOTH THE CSV FILES AND RETURN NUMBERS BASED ON BOTH THE CSV FILES.
#txtpath = os.path.join("Zip","PyParagraph","raw_data","paragraph_1.txt")
#filepath = os.path.join("Zip","PyBank","raw_data","budget_data_1.csv")
txtpaths = os.path.join("Zip","PyParagraph","raw_data","paragraph_2.txt")
num_words1 = 0
num_sentences1 = 0
num_chars1 = 0
words1 = 0
avg = 0
lines1 = 0
sentences1 = 0
num_words1 = 0
blanklines1 = 0

with open(txtpaths) as paragraph:
    #Find out word count
    #print (paragraph.read())
    for line in paragraph:
        words1 = line.split()
        num_words1 += len(words1)
        num_chars1 += len(line)


        lines1 += 1

        if line.startswith('\n'):
            blanklines1 += 1
        else:
    # assume that each sentence ends with . or ! or ?
    # so simply count these characters
            sentences1 += line.count('.') + line.count('!') + line.count('?')
         #avg word lenght
    avg_chars = num_chars1/num_words1

        #avg sentence lenght
    avg_sentence = num_words1/sentences1

    # create a list of words
    # use None to split at any whitespace regardless of length
    # so for instance double space counts as one space


print("Number of words: " + str(num_words1))
print("Number of sentences: " + str(sentences1))
print("avg letter count: " + str(avg_chars))
print("avg sentence lenght: "+str(avg_sentence))

file_output = "mainParagraph1.txt"
with open(file_output, "w") as txt_file:
    txt_file.write("Number of words: ")
    txt_file.write(str(num_words1))
    txt_file.write("\n")
    txt_file.write("Number of Sentences: ")
    txt_file.write(str(sentences1))
    txt_file.write("\n")
    txt_file.write("avg Letter Count: ")
    txt_file.write(str(avg_chars))
    txt_file.write("\n")
    txt_file.write("avg Sentence Count: ")
    txt_file.write(str(avg_sentence))
