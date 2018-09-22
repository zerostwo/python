def build_model(x,y,x_dev,y_dev):
    estimator = SGDClassifier(n_iter=50,shuffle=True,loss="log", \
                learning_rate = "constant",eta0=0.0001,fit_intercept=True, penalty="none")
    estimator.fit(x,y)
    train_predcited = estimator.predict(x)
    train_score = accuracy_score(y,train_predcited)
    dev_predicted = estimator.predict(x_dev)
    dev_score = accuracy_score(y_dev,dev_predicted)
    
    print 
    print "Training Accuracy = %0.2f Dev Accuracy = %0.2f"%(train_score,dev_score)