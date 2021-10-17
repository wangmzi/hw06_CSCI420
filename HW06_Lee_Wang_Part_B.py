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

#The first iteration should be all data_points as individual clusters
#There are 880 entries and therefore a maximum of 880 clusters
max_clusters = 880



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
    def merge(cluster):
        self.merged_clusters.append(cluster)
    
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
#array A and B
def euclid_dist(centerA,centerB):
    return m.dist(centerA,centerB)


def main():
    data = retrieve_data('HW_CLUSTERING_SHOPPING_CART_v2211.csv')
    clusters = data_to_cluster(data)
    print(len(clusters))

    return
if __name__ == '__main__':
    main()
