def build_model(x,y):
    """
    Fit the model for the given attribute 
    class label pairs
    """
    model = tree.DecisionTreeClassifier(criterion="entropy")
    model = model.fit(x,y)
    return model


def test_model(x,y,model,label_names):
    """
    Inspect the model for accuracy
    """
    y_predicted = model.predict(x)
    print "Model accuracy = %0.2f"%(accuracy_score(y,y_predicted) * 100) + "%\n"
    print "\nConfusion Matrix"
    print "================="
    print pprint.pprint(confusion_matrix(y,y_predicted))
    
    print "\nClassification Report"
    print "================="
    
    print classification_report(y,y_predicted,target_names=label_names)
    
