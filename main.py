from nltk import word_tokenize, sent_tokenize
import os

path_file = os.getcwd()
path_file = path_file + '/Files/text.txt'
text=open(path_file).read()
filepath = './Files/tokenized_sentences.txt'
 
sentences = sent_tokenize(text)
for s in sentences:
    print (word_tokenize(s))    


with open(filepath, 'w') as file_handler:
    for s in sentences:
        file_handler.write("{}\n".format(word_tokenize(s)))
