def build_word_features(instance):
    """
    Build feature dictionary
    Features are binary, name of the feature is word iteslf
    and value is 1. Features are stored in a dictionary
    called feature_set
    """
    # Dictionary to store the features
    feature_set = {}
    # The first item in instance tuple the word list
    words = instance[0]
    # Populate feature dicitonary
    for word in words:
        feature_set[word] = 1
    # Second item in instance tuple is class label
    return (feature_set,instance[1])

def build_negate_features(instance):
    """
    If a word is preceeded by either 'not' or 'no'
    this function adds a prefix 'Not_' to that word
    It will also not insert the previous negation word
    'not' or 'no' in feature dictionary
    """
    # Retreive words, first item in instance tuple
    words = instance[0]
    final_words = []
    # A boolean variable to track if the 
    # previous word is a negation word
    negate = False
    # List of negation words
    negate_words = ['no','not']
    # On looping throught the words, on encountering
    # a negation word, variable negate is set to True
    # negation word is not added to feature dictionary
    # if negate variable is set to true
    # 'Not_' prefix is added to the word
    for word in words:
        if negate:
            word = 'Not_' + word
            negate = False
        if word not in negate_words:
            final_words.append(word)
        else:
            negate = True
    # Feature dictionary
    feature_set = {}
    for word in final_words:
        feature_set[word] = 1
    return (feature_set,instance[1])

def remove_stop_words(in_data):
    """
    Utility function to remove stop words
    from the given list of words
    """
    stopword_list = stopwords.words('english')
    negate_words = ['no','not']
    # We dont want to remove the negate words
    # Hence we create a new stop word list excluding
    # the negate words
    new_stopwords = [word for word in stopword_list if word not in negate_words]
    label = in_data[1]
    # Remove stopw words
    words = [word for word in in_data[0] if word not in new_stopwords]
    return (words,label)


def build_keyphrase_features(instance):
    """
    A function to extract key phrases
    from the given text.
    Key Phrases are words of importance according to a measure
    In this key our phrase of is our length 2, i.e two words or bigrams
    """
    feature_set = {}
    instance = remove_stop_words(instance)
    words = instance[0]
   
    bigram_finder  = BigramCollocationFinder.from_words(words)
    # We use the raw frequency count of bigrams, i.e. bigrams are
    # ordered by their frequency of occurence in descending order
    # and top 400 bigrams are selected.
    bigrams        = bigram_finder.nbest(BigramAssocMeasures.raw_freq,400)
    for bigram in bigrams:
        feature_set[bigram] = 1
    return (feature_set,instance[1])
