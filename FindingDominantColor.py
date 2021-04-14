import cv2 as cv
from sklearn.cluster import KMeans


def findDominantColor(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # sklearn uses RGB color
    img = img.reshape((img.shape[0] * img.shape[1], 3))
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(img)
    colors = kmeans.cluster_centers_
    # to return all dominants change return part to colors instead of tuple(....)
    return tuple(reversed(colors[0]))
