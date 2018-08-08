def build_model_cycle_1(train_data,dev_data):
    """
    First pass at trying out our model
    """
    # Build features for training set
    train_features =map(build_word_features,train_data)
    # Build features for test set
    dev_features = map(build_word_features,dev_data)
    # Build model
    model = build_model(train_features)    
    # Look at the model
    probe_model(model,train_features)
    probe_model(model,dev_features,'Dev')
    
    return model
    
def build_model_cycle_2(train_data,dev_data):
    """
    Second pass at trying out our model
    """

    # Build features for training set
    train_features =map(build_negate_features,train_data)
    # Build features for test set
    dev_features = map(build_negate_features,dev_data)
    # Build model
    model = build_model(train_features)    
    # Look at the model
    probe_model(model,train_features)
    probe_model(model,dev_features,'Dev')
    
    return model

    
def build_model_cycle_3(train_data,dev_data):
    """
    Third pass at trying out our model
    """
    
    # Build features for training set
    train_features =map(build_keyphrase_features,train_data)
    # Build features for test set
    dev_features = map(build_keyphrase_features,dev_data)
    # Build model
    model = build_model(train_features)    
    # Look at the model
    probe_model(model,train_features)
    probe_model(model,dev_features,'Dev')
    test_features = map(build_keyphrase_features,test_data)
    probe_model(model,test_features,'Test')
    
    return model
