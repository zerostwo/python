from sklearn.datasets import make_classification
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report,zero_one_loss
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt
import itertools

def get_data():
    """
    Make a sample classification dataset
    Returns : Independent variable y, dependent variable x
    """
    no_features = 30
    redundant_features = int(0.1*no_features)
    informative_features = int(0.6*no_features)
    repeated_features = int(0.1*no_features)
    print no_features,redundant_features,informative_features,repeated_features
    x,y = make_classification(n_samples=500,n_features=no_features,flip_y=0.03,\
            n_informative = informative_features, n_redundant = redundant_features \
            ,n_repeated = repeated_features,random_state=7)
    return x,y
    
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
    

def number_estimators_vs_err_rate(x,y,x_dev,y_dev):
    no_estimators = range(20,120,10)
    misclassy_rate = []
    misclassy_rate_dev = []
    
    for no_estimator in no_estimators:
        boosting = build_boosting_model(x,y,no_estimators=no_estimator)
        predicted_y = boosting.predict(x)
        predicted_y_dev = boosting.predict(x_dev)        
        misclassy_rate.append(zero_one_loss(y,predicted_y))
        misclassy_rate_dev.append(zero_one_loss(y_dev,predicted_y_dev))
    
    plt.figure(2)
    plt.title("No estimators vs Mis-classification rate")
    plt.xlabel("No of estimators")
    plt.ylabel("Mis-classification rate")
    plt.plot(no_estimators,misclassy_rate,label='Train')
    plt.plot(no_estimators,misclassy_rate_dev,label='Dev')
        
    plt.show() 

    
    
if __name__ == "__main__":
    x,y = get_data()    
    plot_data(x,y)

    # Divide the data into Train, dev and test    
    x_train,x_test_all,y_train,y_test_all = train_test_split(x,y,test_size = 0.3,random_state=9)
    x_dev,x_test,y_dev,y_test = train_test_split(x_test_all,y_test_all,test_size=0.3,random_state=9)
        
    # Build a single model    
    model = build_single_model(x_train,y_train)
    predicted_y = model.predict(x_train)
    print "\n Single Model Accuracy on training data\n"
    print classification_report(y_train,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_train,predicted_y)*100),"%"


    # Build a bag of models
    boosting = build_boosting_model(x_train,y_train, no_estimators=85)
    predicted_y = boosting.predict(x_train)
    print "\n Boosting Model Accuracy on training data\n"
    print classification_report(y_train,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_train,predicted_y)*100),"%"
    
    view_model(boosting)
    
    # Look at the dev set
    predicted_y = model.predict(x_dev)
    print "\n Single Model Accuracy on Dev data\n"
    print classification_report(y_dev,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_dev,predicted_y)*100),"%"

    print "\n Boosting Model Accuracy on Dev data\n"
    predicted_y = boosting.predict(x_dev)
    print classification_report(y_dev,predicted_y)
    print "Fraction of misclassfication = %0.2f"%(zero_one_loss(y_dev,predicted_y)*100),"%"

    number_estimators_vs_err_rate(x_train,y_train,x_dev,y_dev)
