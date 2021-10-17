#Creator: Vicky Wang, Anthony Lee
#CSCI 420: HW06

import math as m
import matplotlib.pyplot as plt
import csv

#Attribute names
attr_names = ['ID', 'Milk:0', 'ChdBby:1', 'Vegges:2', 'Cerel:3', 'Bread:4', 'Rice:5', 'Meat:6', 
'Eggs:7', 'YogChs:8', 'Chips:9', 'Soda:10', 'Fruit:11', 'Corn:12', 'Fish:13', 'Sauce:14', 'Beans:15', 'Tortya:16', 
'Salt:17', 'Scented:18', 'Salza:19'] 

#Typifying based on attribute indexes, putting the indexes to exclude
#the attribute, not include
#excluding: meats and fish
vegetarian = [6,13]
#excluding: milk,meat,yogurt/cheese, fish
vegan = [0,6,7,8,13]

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

#Given the new center attaches all the other clusters to it
#Any of the given cluster lists are also reset in this scenario.
def new_center(center,clusters):
    for x in clusters:
        if center != x:
            center.merge(x)
            if x.merged_clusters != []:
                x.merged_clusters = []
    return center

#Used to find the shortest distance between 2 centers of clusters
#Expects an array of clusters
#returns the two points that give the shortest distance and the distance
def shortest_dist(clusters):
    shortest = []
    distance = 99999999999999999
    for x in range(0,len(clusters)):
        for y in range(x+1,len(clusters)):
            cluA = clusters[x]
            cluB = clusters[y]
            if euclid_dist(cluA,cluB) < distance:
                shortest = [cluA,cluB]
                distance = euclid_dist(cluA, cluB)
    return shortest,distance


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
        #Keeps track of what is the center of the cluster
        self.center = self

    #appends a cluster to the list
    def merge(self,cluster):
        self.merged_clusters.append(cluster)
        cluster.center = self
        self.center = self
        return
    
    #re-centers the cluster based on the clusters inside it
    def reCenter(self):
        clusters = self.merged_clusters
        clusters.append(self)
        avg_dist = []
        for x in clusters:
            avg_dist.append(avg_distance(x, clusters))
        idx = avg_dist.index(min(avg_dist))
        center = clusters[idx]
        return new_center(center,clusters)

    #formats print statement
    def __str__(self):
        Id = []
        for x in self.merged_clusters:
            Id.append(x.id)
        return ("Id: "+ str(self.id) + 
        '\nattributes: ' + str(self.records) +
        '\nmerged_clusters: '+ str(Id)
        )


def main():
    data = retrieve_data('HW_CLUSTERING_SHOPPING_CART_v2211.csv')
    clusters = data_to_cluster(data)
    short, dist = shortest_dist(clusters)
    for x in range(1,5):
        clusters[0].merge(clusters[x])
    centered_cluster = clusters[0].reCenter()
    for x in range(0,5):
        print(clusters[x])
    return
if __name__ == '__main__':
    main()
