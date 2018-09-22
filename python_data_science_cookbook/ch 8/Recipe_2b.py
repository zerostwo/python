def build_single_model(x,y):
    model = DecisionTreeClassifier()
    model.fit(x,y)
    return model
    
def build_boosting_model(x,y,no_estimators=20):
    boosting = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1,min_samples_leaf=1),random_state=9 \
    ,n_estimators=no_estimators,algorithm="SAMME")
    boosting.fit(x,y)
    return boosting

def view_model(model):
    print "\n Estimator Weights and Error\n"
    for i,weight in  enumerate(model.estimator_weights_):
        print "estimator %d weight = %0.4f error = %0.4f"%(i+1,weight,model.estimator_errors_[i])
        
    plt.figure(1)
    plt.title("Model weight vs error")
    plt.xlabel("Weight")
    plt.ylabel("Error")
    plt.plot(model.estimator_weights_,model.estimator_errors_)
