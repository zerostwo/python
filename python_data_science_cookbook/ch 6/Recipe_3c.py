def build_model(features):
    """
    Build a naive bayes model
    with the gvien feature set.
    """
    model = nltk.NaiveBayesClassifier.train(features)
    return model    
    
def probe_model(model,features,dataset_type = 'Train'):
    """
    A utility function to check the goodness
    of our model.
    """
    accuracy = nltk.classify.accuracy(model,features)
    print "\n" + dataset_type + " Accuracy = %0.2f"%(accuracy*100) + "%" 
    
def show_features(model,no_features=5):
    """
    A utility function to see how important
    various features are for our model.
    """
    print "\nFeature Importance"
    print "===================\n"
    print model.show_most_informative_features(no_features)        
