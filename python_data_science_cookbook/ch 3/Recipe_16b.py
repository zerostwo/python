# 2.	Let us extract the sentences.
sentences = sent_tokenize(text)

# 3.	Create a matrix of term document frequency.
stop_words = stopwords.words('english')

count_v = CountVectorizer(stop_words=stop_words)
tdm = count_v.fit_transform(sentences)

#4.	Calcuate the TFIDF score.
tfidf = TfidfTransformer()
tdm_tfidf = tfidf.fit_transform(tdm)
