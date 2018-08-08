from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score



def form_clusters(x,k):
    """
    Build clusters
    """
    # k = required number of clusters
    no_clusters = k
    model = KMeans(n_clusters=no_clusters,init='random')
    model.fit(x)
    labels = model.labels_
    print labels
    # Cacluate the silhouette score
    sh_score = silhouette_score(x,labels)
    return sh_score