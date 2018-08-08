if __name__ == "__main__":
    
    # Load data
    input_dataset, y_labels = get_data()
    # Train data    
    train_data,all_test_data,train_y,all_test_y = get_train_test(input_dataset,y_labels)
    # Dev data
    dev_data,test_data,dev_y,test_y = get_train_test(all_test_data,all_test_y)

    # Let us look at the data size in our different 
    # datasets
    print "\nOriginal  Data Size   =", len(input_dataset)
    print "\nTraining  Data Size   =", len(train_data)
    print "\nDev       Data Size   =", len(dev_data)
    print "\nTesting   Data Size   =", len(test_data)    

    # Different passes of our model building exercise    
    model_cycle_1 =  build_model_cycle_1(train_data,dev_data)
    # Print informative features
    show_features(model_cycle_1)    
    model_cycle_2 = build_model_cycle_2(train_data,dev_data)
    show_features(model_cycle_2)
    model_cycle_3 = build_model_cycle_3(train_data,dev_data)
    show_features(model_cycle_3)