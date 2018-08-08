
if __name__ == "__main__":
    x,y = get_data()
    
    # Divide the data into Train, dev and test    
    x_train,x_test_all,y_train,y_test_all = train_test_split(x,y,test_size = 0.3,random_state=9)
    x_dev,x_test,y_dev,y_test = train_test_split(x_test_all,y_test_all,test_size=0.3,random_state=9)
    
    model = build_model(x_train,y_train)

    inspect_model(model)

    print "Model worth on train data"
    model_worth(model,x_train,y_train)
    print "Model worth on dev data"
    model_worth(model,x_dev,y_dev)
    
    # Building model with l2 regularization
    model = build_model_regularized(x_train,y_train)
    inspect_model(model)
