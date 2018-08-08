def build_models(x,y):
    """
    Build a Lasso regression model
    """
    # Alpha values uniformly
    # spaced between 0.01 and 0.02
    alpha_range = np.linspace(0,0.5,200)
    model = Lasso(normalize=True)
    coeffiecients = []
    # Fit a model for each alpha value
    for alpha in alpha_range:
        model.set_params(alpha=alpha)
        model.fit(x,y)
        # Track the coeffiecients for plot
        coeffiecients.append(model.coef_)
    # Plot coeffients weight decay vs alpha value
    # Plot model RMSE vs alpha value
    coeff_path(alpha_range,coeffiecients)
    # View coeffiecient value
    #view_model(model)

def view_model(model):
    """
    Look at model coeffiecients
    """
    print "\n Model coeffiecients"
    print "======================\n"
    for i,coef in enumerate(model.coef_):
        print "\tCoefficient %d  %0.3f"%(i+1,coef)
            
    print "\n\tIntercept %0.3f"%(model.intercept_)

def model_worth(true_y,predicted_y):
    """
    Evaluate the model
    """
    print "\t Mean squared error = %0.2f\n"%(mean_squared_error(true_y,predicted_y))
