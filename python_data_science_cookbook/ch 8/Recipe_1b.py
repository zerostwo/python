
def build_single_model(x,y):
    model = KNeighborsClassifier()
    model.fit(x,y)
    return model


def build_bagging_model(x,y):
	bagging = BaggingClassifier(KNeighborsClassifier(),n_estimators=100,random_state=9 \
             ,max_samples=1.0,max_features=0.7,bootstrap=True,bootstrap_features=True)
	bagging.fit(x,y)
	return bagging

def view_model(model):
    print "\n Sampled attributes in top 10 estimators\n"
    for i,feature_set in  enumerate(model.estimators_features_[0:10]):
        print "estimator %d"%(i+1),feature_set
