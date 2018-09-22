def get_class_distribution(y):
	"""
	Given an array of class labels
	Return the class distribution
	"""
    distribution = {}
    set_y = set(y)
    for y_label in set_y:
        no_elements = len(np.where(y == y_label)[0])
        distribution[y_label] = no_elements
    dist_percentage = {class_label: count/(1.0*sum(distribution.values())) for class_label,count in distribution.items()}
    return dist_percentage
        
    

def print_class_label_split(train,test):
  	"""
  	Print the class distribution
  	in test and train dataset
  	"""  
    y_train = train[:,-1]
    
    train_distribution = get_class_distribution(y_train)
    print "\nTrain data set class label distribution"
    print "=========================================\n"
    for k,v in train_distribution.items():
        print "Class label =%d, percentage records =%.2f"%(k,v)
    
    y_test = test[:,-1]    
    
    test_distribution = get_class_distribution(y_test)
    
    print "\nTest data set class label distribution"
    print "=========================================\n"
    
    for k,v in test_distribution.items():
        print "Class label =%d, percentage records =%.2f"%(k,v)


print_class_label_split(train,test)
