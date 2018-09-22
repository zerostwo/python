from collections import defaultdict

sentence = "Peter Piper picked a peck of pickled peppers  A peck of pickled \
            peppers Peter Piper picked If Peter Piper picked a peck of pickled \
            peppers Wheres the peck of pickled peppers Peter Piper picked"

word_dict = defaultdict(int)

for word in sentence.split():
    word_dict[word]+=1

print word_dict    