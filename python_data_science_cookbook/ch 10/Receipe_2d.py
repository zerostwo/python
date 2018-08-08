def build_model_regularized(x,y):
    estimator = SGDRegressor(n_iter = 10,shuffle=True,loss = "squared_loss", \
            learning_rate='constant',eta0=0.01,fit_intercept=True, \
            penalty='l2',alpha=0.01)
    estimator.fit(x,y)
    
    return estimator
