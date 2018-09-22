# Perform Split the data
stratified_split = StratifiedShuffleSplit(input_dataset[:,-1],test_size=test_size,n_iter=1)

for train_indx,test_indx in stratified_split:
    train = input_dataset[train_indx]
    test =  input_dataset[test_indx]
    print_class_label_split(train,test)
