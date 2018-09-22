if __name__ == "__main__":
    data = get_data(10)    
    x,y = data.next()
    weights = np.zeros(x.shape[1])    
    for i in range(10):
        epochs = 100
        weights = build_model(x,y,weights,epochs)
        print
        print "Model worth after receiving dataset batch %d"%(i+1)    
        model_worth(x,y,weights)
        print
        if i < 9:
            x,y = data.next()


