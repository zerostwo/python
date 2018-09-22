def find_closest(in_vector,proto_vectors):
    closest = None
    closest_distance = 99999
    for p_v in proto_vectors:
        distance = euclidean_distances(in_vector,p_v.p_vector)
        if distance < closest_distance:
            closest_distance = distance
            closest = p_v
    return closest
