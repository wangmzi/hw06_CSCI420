#Creator: Vicky Wang, Anthony Lee
#CSCI 420: HW06

import math as m
import matplotlib.pyplot as plt
import csv


attr_names = ['ID', 'Milk', 'ChdBby', 'Vegges', 'Cerel', 'Bread', 'Rice', 'Meat', 
'Eggs', 'YogChs', 'Chips', 'Soda', 'Fruit', 'Corn', 'Fish', 'Sauce', 'Beans', 'Tortya', 
'Salt', 'Scented', 'Salza']  
#Takes a guest entry and converts it to a cluster format.
class cluster:
    def __init__(self, guest_id, records):
        #cluster guest Id
        self.id = guest_id
        #Keeps track of all attributes in cluster
        self.records = records
        #Keeps track of what clusters are merged into the cluster
        self.merged_clusters = []

    def merge(cluster):
        self.merged_clusters.append(cluster)
    
    def __str__(self):
        Id = []
        for x in self.merged_clusters:
            Id.append(x.id)
        return "Id: "+ str(self.id) + '\nmerged_clusters: '+ str(Id)


#used to find distance between two centers of clusters
def euclid_dist(centerA,centerB):
    return m.dist(centerA,centerB)

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

def data_to_cluster(data):
    clusters = []
    for x in data:
        clusters.append(cluster(x[0], x[1:]))
    return clusters

def main():
    data = retrieve_data('HW_CLUSTERING_SHOPPING_CART_v2211.csv')
    clusters = data_to_cluster(data)
    print(clusters[0])
    print(clusters[0].records)
    return
if __name__ == '__main__':
    main()
