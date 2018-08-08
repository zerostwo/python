from sklearn.datasets import load_iris
from sklearn.cross_validation import KFold,StratifiedKFold

def get_data():
    data = load_iris()
    x = data['data']
    y = data['target']
    return x,y

def class_distribution(y):
        class_dist = {}
        total = 0
        for entry in y:
            try:
                class_dist[entry]+=1
            except KeyError:
                class_dist[entry]=1
            total+=1
        
        for k,v in class_dist.items():
            print "\tclass %d percentage =%0.2f"%(k,v/(1.0*total))
    
if __name__ == "__main__":
    x,y = get_data()
    # K Fold
    # 3 folds
    kfolds = KFold(n=y.shape[0],n_folds=3)
    fold_count  =1
    print
    for train,test in kfolds:
        print "Fold %d x train shape"%(fold_count),x[train].shape,\
        " x test shape",x[test].shape
        fold_count==1
    print
    #Stratified KFold
    skfolds = StratifiedKFold(y,n_folds=3)
    fold_count  =1
    for train,test in skfolds:
        print "\nFold %d x train shape"%(fold_count),x[train].shape,\
        " x test shape",x[test].shape
        y_train = y[train]
        y_test  = y[test]
        print "Train Class Distribution"
        class_distribution(y_train)
        print "Test Class Distribution"
        class_distribution(y_test)

        fold_count+=1

    print

    
    
    