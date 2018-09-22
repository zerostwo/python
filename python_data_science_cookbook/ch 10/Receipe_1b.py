def build_model(x,y,weights,epochs,alpha=0.5):
    """
    Simple Perceptron
    """
  
    for i in range(epochs):
        
        # Shuffle the dataset
        shuff_index = np.random.shuffle(range(len(y)))
        x_train = x[shuff_index,:].reshape(x.shape)
        y_train = np.ravel(y[shuff_index,:])
        
        # Build weights one instance at a time
        for index in range(len(y)):
            prediction = np.sign( np.sum(x_train[index,:] * weights) ) 
            if prediction != y_train[index]:
                weights = weights + alpha * (y_train[index] * x_train[index,:])
            
    return weights
    

                    
def model_worth(x,y,weights):
    prediction = np.sign(np.sum(x * weights,axis=1))
    print classification_report(y,prediction)
