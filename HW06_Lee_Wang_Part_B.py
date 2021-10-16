#Creator: Vicky Wang, Anthony Lee
#CSCI 420: HW06

import numpy as np
from math import dist
import matplotlib.pyplot as plt

#used to find distance between two centers of clusters
def euclid_dist(centerA,centerB):
    return dist(centerA,centerB)

class cluster:
    def __init__(self, center, records, id_members):
        #coordinate to be the center of cluster.
        self.center = center

        #Keeps track of all points in cluster
        self.records = records

        #Keeps track of guest id joined in the cluster.
        self.id_members = id_members

        #Keeps track of what clusters are merged into the cluster
        self.merged_clusters = []

    def merge(new_cluster):
        self.merged_clusters.append(new_cluster)
