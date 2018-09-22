def build_model(x,y):
    """
    Build a Ridge regression model
    """
    kfold = KFold(y.shape[0],5)
    model = Ridge(normalize=True)

    alpha_range = np.linspace(0.0015,0.0017,30)
    grid_param = {"alpha":alpha_range}
    grid = GridSearchCV(estimator=model,param_grid=grid_param,cv=kfold,scoring='mean_squared_error')
    grid.fit(x,y)
    display_param_results(grid.grid_scores_)
    print grid.best_params_
    # Track the scores- Mean squared residual for plot
    return grid.best_estimator_

def view_model(model):
    """
    Look at model coeffiecients
    """
    #print "\n Estimated Alpha = %0.3f"%model.alpha_
    print "\n Model coeffiecients"
    print "======================\n"
    for i,coef in enumerate(model.coef_):
        print "\tCoefficient %d  %0.3f"%(i+1,coef)
            
    print "\n\tIntercept %0.3f"%(model.intercept_)

def model_worth(true_y,predicted_y):
    """
    Evaluate the model
    """
    print "\tMean squared error = %0.2f"%(mean_squared_error(true_y,predicted_y))
    return mean_squared_error(true_y,predicted_y)

def display_param_results(param_results):
    fold = 1
    for param_result in param_results:
        print "Fold %d Mean squared error %0.2f"%(fold,abs(param_result[1])),param_result[0]
        fold+=1
