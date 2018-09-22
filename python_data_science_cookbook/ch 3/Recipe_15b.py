#2.Let us divide the given text into sentences
sentences = sent_tokenize(text)

#3.Let us write the code to generate feature vectors.
count_v = CountVectorizer()
tdm = count_v.fit_transform(sentences)


# While creating a mapping from words to feature indices, we can ignore
# some words by providing a stop word list.
stop_words = stopwords.words('english')
count_v_sw = CountVectorizer(stop_words=stop_words)
sw_tdm = count_v.fit_transform(sentences)


# Use ngrams
count_v_ngram = CountVectorizer(stop_words=stop_words,ngram_range=(1,2))
ngram_tdm = count_v.fit_transform(sentences)
