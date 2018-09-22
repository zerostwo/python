def build_forest(x,y,x_dev,y_dev):
    """
    Build a random forest of fully grown trees
    and evaluate peformance
    """
    no_trees = 100
    estimator = RandomForestClassifier(n_estimators=no_trees)
    estimator.fit(x,y)
    
    train_predcited = estimator.predict(x)
    train_score = accuracy_score(y,train_predcited)
    dev_predicted = estimator.predict(x_dev)
    dev_score = accuracy_score(y_dev,dev_predicted)
    
    print "Training Accuracy = %0.2f Dev Accuracy = %0.2f"%(train_score,dev_score)
    
     
def search_parameters(x,y,x_dev,y_dev):
    """
    Search the parameters of random forest algorithm
    """
    estimator = RandomForestClassifier()
    no_features = x.shape[1]
    no_iterations = 20
    sqr_no_features = int(np.sqrt(no_features))

    parameters = {"n_estimators"      : np.random.randint(75,200,no_iterations),
                 "criterion"         : ["gini", "entropy"],
                 "max_features"      : [sqr_no_features,sqr_no_features*2,sqr_no_features*3,sqr_no_features+10]
                 }

    grid = RandomizedSearchCV(estimator=estimator,param_distributions=parameters,\
    verbose=1, n_iter=no_iterations,random_state=77,n_jobs=-1,cv=5)
    grid.fit(x,y)
    print_model_worth(grid,x_dev,y_dev)

    return grid.best_estimator_

   

def print_model_worth(grid,x_dev,y_dev):    
    # Print the goodness of the models
    # We take the top 5 models
    scores = sorted(grid.grid_scores_, key=itemgetter(1), reverse=True) [0:5]
    
    for model_no,score in enumerate(scores):
        print "Model %d, Score = %0.3f"%(model_no+1,score.mean_validation_score)
        print "Parameters = {0}".format(score.parameters)
    print
    dev_predicted = grid.predict(x_dev)
    
    print classification_report(y_dev,dev_predicted)
