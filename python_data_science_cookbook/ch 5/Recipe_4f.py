# Choose R initial prototypes for each class        
p_vectors = []
for i in range(n_classes):
    # Select a class
    y_subset = np.where(y == i)
    # Select tuples for choosen class
    x_subset  = x[y_subset]
    # Get R random indices between 0 and 50
    samples = np.random.randint(0,len(x_subset),R)
    # Select p_vectors
    for sample in samples:
        s = x_subset[sample]
        p = prototype(i,s,epsilon)
        p_vectors.append(p)

print "class id \t Initial protype vector\n"
for p_v in p_vectors:
    print p_v.class_id,'\t',p_v.p_vector
       
print
