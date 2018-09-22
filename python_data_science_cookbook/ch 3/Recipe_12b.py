words = word_tokenize(text)
# 2.Let us get the list of stopwords from nltk stopwords english corpus.
stop_words = stopwords.words('english')


print "Number of words = %d"%(len(words)) 
# 3.	Filter out the stop words.
words = [w for w in words if w not in stop_words]
print "Number of words,without stop words = %d"%(len(words)) 


words = [w for w in words if w not in string.punctuation]
print "Number of words,without stop words and punctuations = %d"%(len(words)) 
