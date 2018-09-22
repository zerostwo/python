def get_feature_names():
    data = load_iris()
    return data['feature_names']


def probe_model(x,y,model,label_names):

    feature_names = get_feature_names()
    feature_importance = model.feature_importances_
    print "\nFeature Importance\n"
    print "=====================\n"
    for i,feature_name in enumerate(feature_names):
        print "%s = %0.3f"%(feature_name,feature_importance[i])

    # Export the decison tree as a graph
    tree.export_graphviz(model,out_file='tree.dot')
