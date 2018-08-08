# Load libraries
from sklearn.metrics import jaccard_similarity_score

# 1.Initialize two sentences.
st_1 = "dogs chase cats"
st_2 = "dogs hate cats"

# 2.Create set of words from strings
st_1_wrds = set(st_1.split())
st_2_wrds = set(st_2.split())

unq_wrds = st_1_wrds.union(st_2_wrds)

a  =[ 1 if w in st_1_wrds else 0 for w in unq_wrds ]
b  =[ 1 if w in st_2_wrds else 0 for w in unq_wrds]

print a
print b
print jaccard_similarity_score(a,b)