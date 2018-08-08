def build_model(x,y,n_estimators=500):
    """
    Build a Gradient Boost regression model
    """
    model = GradientBoostingRegressor(n_estimators=n_estimators,verbose=10,\
            subsample=0.7, learning_rate= 0.15,max_depth=3,random_state=77)
    model.fit(x,y)
    return model    

def view_model(model):
    """
    """
    print "\n Training scores"
    print "======================\n"
    for i,score in enumerate(model.train_score_):
        print "\tEstimator %d score %0.3f"%(i+1,score)

    plt.cla()
    plt.figure(1)
    plt.plot(range(1,model.estimators_.shape[0]+1),model.train_score_)
    plt.xlabel("Model Sequence")
    plt.ylabel("Model Score")
    plt.show()

    print "\n Feature Importance"
    print "======================\n"
    for i,score in enumerate(model.feature_importances_):
        print "\tFeature %d Importance %0.3f"%(i+1,score)
    
            

def model_worth(true_y,predicted_y):
    """
    Evaluate the model
    """
    print "\tMean squared error = %0.2f"%(mean_squared_error(true_y,predicted_y))
