if __name__ == "__main__":

    # Sample data, 2 vectors of dimension 3
    x = np.asarray([1,2,3])
    y = np.asarray([1,2,3])
    # print euclidean distance    
    print euclidean_distance(x,y)
    # Print euclidean by invoking lr norm with
    # r value of 2    
    print lrNorm_distance(x,y,2)
    # Manhattan or citi block Distance
    print lrNorm_distance(x,y,1)
    
    # Sample data for cosine distance
    x =[1,1]
    y =[1,0]
    print 'cosine distance'
    print cosine_distance(x,y)
    
    # Sample data for jaccard distance    
    x = [1,2,3]
    y = [1,2,3]
    print jaccard_distance(x,y)
    
    # Sample data for hamming distance    
    x =[11001]
    y =[11011]
    print hamming_distance(x,y)
    
