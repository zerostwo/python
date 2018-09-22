if __name__ == "__main__":
    # Load the data
    x,y,label_names = get_data()
    # Split the data into train and test    
    train_x,train_y,test_x,test_y = get_train_test(x,y)
    # Build model    
    model = build_model(train_x,train_y)
    # Evaluate the model on train dataset    
    test_model(train_x,train_y,model,label_names)    
    # Evaluate the model on test dataset
    test_model(test_x,test_y,model,label_names)
