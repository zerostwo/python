if __name__ == "__main__":
    x,y = get_data()    
    plot_data(x,y)

    # Divide the data into Train, dev and test    
    x_train,x_test_all,y_train,y_test_all = train_test_split(x,y,test_size = 0.3,random_state=9)
    x_dev,x_test,y_dev,y_test = train_test_split(x_test_all,y_test_all,test_size=0.3,random_state=9)
        
    # Build a single model    
    model = build_single_model(x_train,y_train)
    predicted_y = model.predict(x_train)
    print "\n Single Model Accuracy on training data\n"
    print classification_report(y_train,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_train,predicted_y)*100),"%"


    # Build a bag of models
    boosting = build_boosting_model(x_train,y_train, no_estimators=85)
    predicted_y = boosting.predict(x_train)
    print "\n Boosting Model Accuracy on training data\n"
    print classification_report(y_train,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_train,predicted_y)*100),"%"
    
    view_model(boosting)
    
    # Look at the dev set
    predicted_y = model.predict(x_dev)
    print "\n Single Model Accuracy on Dev data\n"
    print classification_report(y_dev,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_dev,predicted_y)*100),"%"

    print "\n Boosting Model Accuracy on Dev data\n"
    predicted_y = boosting.predict(x_dev)
    print classification_report(y_dev,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_dev,predicted_y)*100),"%"

    number_estimators_vs_err_rate(x_train,y_train,x_dev,y_dev)
