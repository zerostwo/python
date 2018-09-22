def all_indices(value, inlist):
    out_indices = []
    idx = -1
    while True:
        try:
            idx = inlist.index(value, idx+1)
            out_indices.append(idx)
        except ValueError:
            break
    return out_indices

# Calculate K distance neighbourhood
import heapq
k_distance_neig = defaultdict(list)
# For each data point
for i in range(instances.shape[0]):
    # Get the points distances to its neighbours
    distances = dist[i].tolist()
    print "k distance neighbourhood",i
    print distances
    # Get the 1 to K nearest neighbours
    ksmallest = heapq.nsmallest(k+1,distances)[1:]
    print ksmallest
    ksmallest_set = set(ksmallest)
    print ksmallest_set
    ksmallest_idx = []
    # Get the indices of the K smallest elements
    for x in ksmallest_set:
            ksmallest_idx.append(all_indices(x,distances))
    # Change a list of list to list
    ksmallest_idx = [item for sublist in ksmallest_idx for item in sublist]
    # For each data pont store the K distance neighbourhood
    k_distance_neig[i].extend(zip(ksmallest,ksmallest_idx))
