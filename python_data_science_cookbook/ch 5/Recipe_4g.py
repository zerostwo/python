while epsilon >= 0.01:
    # Sample a training instance randonly
    rnd_i = np.random.randint(0,149)
    rnd_s = x[rnd_i]
    target_y = y[rnd_i]

    # Decrement epsilon value for next iteration
    epsilon = epsilon - epsilon_dec_factor    
    # Find closes prototype vector to given point
    closest_pvector = find_closest(rnd_s,p_vectors)
    
    # Update closes prototype vector
    if target_y == closest_pvector.class_id:
        closest_pvector.update(rnd_s)
    else:
        closest_pvector.update(rnd_s,False)
    closest_pvector.epsilon = epsilon
        
print "class id \t Final Prototype Vector\n"
for p_vector in p_vectors:
    print p_vector.class_id,'\t',p_vector.p_vector

