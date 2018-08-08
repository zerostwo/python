# Calculate K distance
import heapq
k_distance = defaultdict(tuple)
# For each data point
for i in range(instances.shape[0]):
    # Get its distance to all the other points.
    # Convert array into list for convienience
    distances = dist[i].tolist()
    # Get the K nearest neighbours
    ksmallest = heapq.nsmallest(k+1,distances)[1:][k-1]
    # Get their indices
    ksmallest_idx = distances.index(ksmallest)
    # For each data point store the K th nearest neighbour and its distance
    k_distance[i]=(ksmallest,ksmallest_idx)
