#Local reachable density
local_reach_density = defaultdict(float)
for i in range(instances.shape[0]):
    # LRDs numerator, number of K distance neighbourhood
    no_neighbours = len(k_distance_neig[i])
    denom_sum = 0
    # Reachability distance sum
    for neigh in k_distance_neig[i]:
        # maximum(K-Distance(P), Distance(P,Q))
        denom_sum+=max(k_distance[neigh[1]][0],neigh[0])
    local_reach_density[i] = no_neighbours/(1.0*denom_sum)
    
