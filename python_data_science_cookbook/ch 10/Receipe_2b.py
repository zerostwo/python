def build_model(x,y):
    estimator = SGDRegressor(n_iter = 10, shuffle=True,loss = "squared_loss", \
            learning_rate='constant',eta0=0.01,fit_intercept=True, \
            penalty='none')
    estimator.fit(x,y)
    
    return estimator
    
    
def model_worth(model,x,y):
    predicted_y = model.predict(x)
    print "\nMean absolute error = %0.2f"%mean_absolute_error(y,predicted_y)
    print "Mean squared error = %0.2f"%mean_squared_error(y,predicted_y)
    
def inspect_model(model):
    print "\nModel Itercept {0}".format(model.intercept_)
    print
    for i,coef in enumerate(model.coef_):
        print "Coefficient {0} = {1:.3f}".format(i+1,coef)
