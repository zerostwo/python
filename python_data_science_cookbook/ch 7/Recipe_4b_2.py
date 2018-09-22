if __name__ == "__main__":
    
    x,y = get_data()
    
    # Divide the data into Train and test    
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state=9)

    #Prepare some polynomial features
    poly_features = PolynomialFeatures(interaction_only=True)
    poly_features.fit(x_train)
    x_train_poly = poly_features.transform(x_train)
    x_test_poly  = poly_features.transform(x_test)
    
    choosen_model = build_model(x_train_poly,y_train)
    predicted_y = choosen_model.predict(x_train_poly)
    model_worth(y_train,predicted_y)
    
    view_model(choosen_model)
    
    predicted_y = choosen_model.predict(x_test_poly)
    model_worth(y_test,predicted_y)
    

