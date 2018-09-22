k = 2
distance = 'manhattan'


from sklearn.metrics import pairwise_distances
dist = pairwise_distances(instances,metric=distance)
