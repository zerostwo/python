if __name__ == "__main__":
    
    x,y = get_data()
    
    # Divide the data into Train, dev and test    
    x_train,x_test_all,y_train,y_test_all = train_test_split(x,y,test_size = 0.3,random_state=9)
    x_dev,x_test,y_dev,y_test = train_test_split(x_test_all,y_test_all,test_size=0.3,random_state=9)
    
    # Build the model
    model = build_model(x_train,y_train)
    predicted_y = model.predict(x_train)
    
    # Plot the residual
    plot_residual(y_train,predicted_y)
    # View model coeffiecients    
    view_model(model)
    
    print "\n Model Performance in Training set\n"
    model_worth(y_train,predicted_y)  
    
    # Apply the model on dev set
    predicted_y = model.predict(x_dev)
    print "\n Model Performance in Dev set\n"
    model_worth(y_dev,predicted_y)  
    
    #Prepare some polynomial features
    poly_features = PolynomialFeatures(2)
    poly_features.fit(x_train)
    x_train_poly = poly_features.transform(x_train)
    x_dev_poly   = poly_features.transform(x_dev)
    
    # Build model with polynomial features
    model_poly = build_model(x_train_poly,y_train)
    predicted_y = model_poly.predict(x_train_poly)
    print "\n Model Performance in Training set (Polynomial features)\n"
    model_worth(y_train,predicted_y)  
    
    # Apply the model on dev set
    predicted_y = model_poly.predict(x_dev_poly)
    print "\n Model Performance in Dev set  (Polynomial features)\n"
    model_worth(y_dev,predicted_y)  
    
    # Apply the model on Test set
    x_test_poly = poly_features.transform(x_test)
    predicted_y = model_poly.predict(x_test_poly)

    print "\n Model Performance in Test set  (Polynomial features)\n"
    model_worth(y_test,predicted_y)  

    predicted_y = model.predict(x_test)
    print "\n Model Performance in Test set  (Regular features)\n"
    model_worth(y_test,predicted_y)  
