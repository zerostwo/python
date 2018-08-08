if __name__ == "__main__":
    
    x,y = get_data()
    # Build multiple models for different alpha values
    # and plot them    
    build_models(x,y)
    print "\nPredicting using all the variables"
    full_model = LinearRegression(normalize=True)
    full_model.fit(x,y)
    predicted_y = full_model.predict(x)
    model_worth(y,predicted_y)    
           
    print "\nModels at different alpha values\n"
    alpa_values = [0.22,0.08,0.01]
    for alpha in alpa_values:
        
        indices = get_coeff(x,y,alpha)   
        print "\t alpah =%0.2f Number of variables selected = %d "%(alpha,len(indices))
        print "\t attributes include ", indices
        x_new = x[:,indices]
        model = LinearRegression(normalize=True)
        model.fit(x_new,y)
        predicted_y = model.predict(x_new)
        model_worth(y,predicted_y)


