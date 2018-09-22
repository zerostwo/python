# 1.Load a variable with sentences
sentence = "Peter Piper picked a peck of pickled peppers A peck of pickled \
peppers Peter Piper picked If Peter Piper picked a peck of pickled \
peppers Wheres the peck of pickled peppers Peter Piper picked"


# 2.Initialize a dictionary object
word_dict = {}

# 3.Perform the word count
for word in sentence.split():
    if word not in word_dict:
        word_dict[word] =1
    else:  
        word_dict[word]+=1

# 4.print the output
print word_dict

