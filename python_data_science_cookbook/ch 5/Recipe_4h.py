predicted_y = [find_class_id(instance,p_vectors) for instance in x ]

from sklearn.metrics import classification_report

print
print classification_report(y,predicted_y,target_names=['Iris-Setosa','Iris-Versicolour', 'Iris-Virginica'])
