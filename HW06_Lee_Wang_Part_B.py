#Creator: Vicky Wang, Anthony Lee
#CSCI 420: HW06

import math as m
import matplotlib.pyplot as plt
import csv

#Takes a guest entry and converts it to a cluster format.
class cluster:
    #Constructor
    def __init__(self, guest_id, records):
        #cluster guest Id
        self.id = guest_id
        #Keeps track of all attributes in cluster
        self.records = records
        #Keeps track of what clusters are merged into the cluster
        self.merged_clusters = []


    #appends a cluster to the list
    def merge(self,cluster):
        self.merged_clusters.append(cluster)
        return

    #returns the average distance of the clusters from center
    def average_dist(self):
        return avg_distance(self, self.merged_clusters)
    
    #returns the size of the cluster including itself
    def size(self):
        return len(self.merged_clusters) + 1

    #formats print statement
    def __str__(self):
        Id = []
        for x in self.merged_clusters:
            Id.append(x.id)
        return ("Id: "+ str(self.id) + 
        '\nattributes: ' + str(self.records) +
        '\nmerged_clusters: '+ str(Id)
        )


#Gets data from the csv file and organizes it into an array
#returns an array of entries
def retrieve_data(csv_filename):
    file = open(csv_filename)
    reader = csv.reader(file)
    next(reader)
    data = []
    for x in reader:
        curr_entry = []
        for val in x:
            try:
                curr_entry.append(int(val))
            except:
                pass
        data.append(curr_entry)
    file.close()
    return data

#Takes the array of data and converts each entry into a cluster
#returns an array of clusters
def data_to_cluster(data):
    clusters = []
    for x in data:
        clusters.append(cluster(x[0], x[1:]))
    return clusters


#Used to find distance between two centers of clusters
#returns the distance between tuple A and B OR
#expects centerA and centerB to be clusters
def euclid_dist(centerA,centerB):
    return m.dist(centerA.records,centerB.records)

#Given an array of clusters find the average distance from the given
#center. Expects a cluster for center and an array of clusters for
#clusters where the center is also in the array
def avg_distance(center, clusters):
    sum = 0
    for x in clusters:
        if center != x:
            sum += euclid_dist(center, x)
    return sum/len(clusters)-1


#Used to find the shortest distance between 2 centers of clusters
#Expects an array of clusters
#returns the two points that give the shortest distance and the distance
def shortest_dist(clusters):
    shortest = []
    distance = 99999999999999999
    shortA, shortB = None, None
    for x in range(0,len(clusters)):
        for y in range(x+1,len(clusters)):
            cluA = clusters[x]
            cluB = clusters[y]
            if euclid_dist(cluA,cluB) < distance:
                shortA = cluA
                shortB = cluB
                distance = euclid_dist(cluA, cluB)
    return [shortA, shortB]

#removes cluster from the array
def remove_cluster(clu,clusters):
    return (clusters.pop(clusters.index(clu)))

#returns the smallest clusters size.
def smallest_cluster(clusters):
    small = clusters[0].size()
    for x in clusters:
        if x.size() < small:
            small = x.size()
    return small

#Given the new center attaches all the other clusters to it
#Any of the given cluster lists are also reset in this scenario.
def new_center(center,clusters):
    for x in clusters:
        center.merge(x)
        if x.merged_clusters != []:
            x.merged_clusters = []
    return center

#Given a cluster recenter it based on the merged clusters
def recenter(cluster):
    clusters = cluster.merged_clusters
    clusters.append(cluster.center)
    avg_dist = []
    for x in clusters:
        avg_dist.append(avg_distance(x, clusters))
    idx = avg_dist.index(min(avg_dist))
    center = clusters.pop(idx)
    return new_center(center,clusters)

#Given an array of clusters, recenters all of them.
def recenter_grouped_clusters(clusters):
    for x in range(0,len(clusters)):
        print(x)
        clusters[x] = recenter(clusters[x])
    return

#grouping the clusters and retruns smallest cluster merged
#This is based off cluster distances
#this also limits the clusters to certain sizes
#TODO: some clusters are lost here
def group_clusters(cluster_dist, clusters, cluster_size):
    smallest_size = smallest_cluster(clusters)
    grouped_clusters = []
    points = shortest_dist(clusters)
    while clusters != []:
        grouped_clusters.append(remove_cluster(clusters[0], clusters))
        curr_cluster = grouped_clusters[len(grouped_clusters)-1]
        for x in clusters:
            if euclid_dist(curr_cluster, x) < cluster_dist and curr_cluster.size() < cluster_size:
                curr_cluster.merge(remove_cluster(x,clusters))

    #TODO: Needs to be fixed
    # recenter_grouped_clusters(grouped_clusters)
    
    if smallest_cluster(grouped_clusters) == smallest_size:
        remaining_clusters = []
        for x in grouped_clusters:
            if x.size() == smallest_size:
                remaining_clusters.append(remove_cluster(x, grouped_clusters))

        for x in remaining_clusters:
            possible_cluster = grouped_clusters[0]
            distance = euclid_dist(x, possible_cluster)
            for y in range(0,len(grouped_clusters)):
                if euclid_dist(x,grouped_clusters[y]) < distance:
                    possible_cluster = grouped_clusters[y]
            possible_cluster.merge(x)

    return grouped_clusters, smallest_size 

def group_iteration(cluster_dist,clusters,cluster_size, cycles):
    grouped_clusters = clusters
    merge_record = []
    for x in range(0, cycles):
        grouped_clusters, smallest_size = group_clusters(cluster_dist, grouped_clusters, cluster_size)
        merge_record.append(smallest_size)
    return grouped_clusters, merge_record

def main():
    data = retrieve_data('HW_CLUSTERING_SHOPPING_CART_v2211.csv')
    clusters = data_to_cluster(data)

    max_cluster_dist = 8 #arbitrary number 
    cluster_size = 90 #arbitrary number
    cycles = 15 #iterations of grouping

    #grouped clusters are the clusters after being merged together based on distance
    #merge_record is to record the smallest group merged of each iteration
    #The following TODO: are in the function call below group_iteration
    #TODO: fix recentering function (it is commented out)
    #TODO: some clusters are lost, must figure out where they are being lost
    grouped_clusters, merge_record= group_iteration(max_cluster_dist, clusters, cluster_size, cycles)
    sizes = []
    avg_distance = []
    for x in grouped_clusters:
        sizes.append(x.size())
        avg_distance.append(x.average_dist())
    sizes.sort()
    print("The following numbers are based on the following chateristics:")
    print("Max distance a cluster(data point is from the center): ", max_cluster_dist)
    print("Max cluster size: ", cluster_size)
    print("# of cycles to merge: ", cycles)
    print("\nnumber of clusters: ", len(grouped_clusters))
    print("sizes of clusters (smallest to largest): ", sizes)
    print("average prototype : ", sum(avg_distance)/len(avg_distance))

    return

if __name__ == '__main__':
    main()
