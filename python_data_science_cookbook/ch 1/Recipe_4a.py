# 1.Initialize two sentences.
st_1 = "dogs chase cats"
st_2 = "dogs hate cats"

# 2.Create set of words from strings
st_1_wrds = set(st_1.split())
st_2_wrds = set(st_2.split())

# 3.Find out the number of unique words in each set, vocabulary size.
no_wrds_st_1 = len(st_1_wrds)
no_wrds_st_2 = len(st_2_wrds)

# 4.Find out the list of common words between the two sets.
# Also find out the count of common words.
cmn_wrds = st_1_wrds.intersection(st_2_wrds)
no_cmn_wrds = len(st_1_wrds.intersection(st_2_wrds))

# 5.Get a list of unique words between the two sets.
# Also find out the count of unique words.
unq_wrds = st_1_wrds.union(st_2_wrds)
no_unq_wrds = len(st_1_wrds.union(st_2_wrds))

# 6.Calculate Jaccard similarity 
similarity = no_cmn_wrds / (1.0 * no_unq_wrds)

# 7.Let us now print to grasp our output.
print "No words in sent_1 = %d"%(no_wrds_st_1)
print "Sentence 1 words =", st_1_wrds
print "No words in sent_2 = %d"%(no_wrds_st_2)
print "Sentence 2 words =", st_2_wrds
print "No words in common = %d"%(no_cmn_wrds)
print "Common words =", cmn_wrds
print "Total unique words = %d"%(no_unq_wrds)
print "Unique words=",unq_wrds
print "Similarity = No words in common/No unique words, %d/%d = %.2f"%(no_cmn_wrds,no_unq_wrds,similarity)


