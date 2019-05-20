from sklearn.cluster import DBSCAN
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt


# method 1
def dbscan_build_in_module():
    input_data = np.array([(3,10), (5,6), (9,5), (2,8), (8,5), (4,6), (3,3), (5,7), (6,9)])
    clustering = DBSCAN (eps=3,min_samples=3).fit(input_data)
    print (clustering.labels_)


def E_distance(point,center):
    """
    This function calculate the Euclidean distance between a point and the center
    """
    distance = sqrt(pow((center[0]-point[0]),2)+pow((center[1]-point[1]),2))
    #print ("distance is: ",distance)
    return distance 

def dbscan(data,radius,MinPts):
    final_cluster = []
    # goes over each point
    for i in range (len(data)):
        #print ("point is: ",data[i])
        one_point_neighbor = [data[i]]
        # establish the neighbor for each point (including itself)
        for point in data:
            if (data[i] != point):
                distance = E_distance(data[i],point)
                #print ("\tcomparint point is: ",point)
                #print ("\tdistance between is: ",distance)

                if (distance<=radius):
                    one_point_neighbor.append(point)
        #print ("\tthis point's neighbor {}, length: {}".format(one_point_neighbor,len(one_point_neighbor)))
        final_cluster.append(one_point_neighbor)
        one_point_neighbor = []

    core = []
    border = []
    noise = []
    
    non_core_points = []
    for clu in final_cluster:
        non_core_points.append(clu)
    # check the core point
    for neighbor in range(len(final_cluster)):
        nei_length = len(final_cluster[neighbor])
        if (nei_length>=MinPts):
            core_info = (final_cluster[neighbor][0],neighbor) # pair (point, index)
            core.append(core_info)
            non_core_points[neighbor] = []

    core_border = []
    #print ("final claster: ",final_cluster)
    for core_pair in core:
        nei = final_cluster[core_pair[1]]
        #print ("core_pair[1]: ",core_pair[1])
        #print ("the neighborhood for core: ")
        #print (nei)

        for p in (nei[1:]):
            if (p not in core_border):
                core_border.append(p)
    print ("core_border is: ",core_border)
                #if (check_point in final_cluster[core_pair[1]]):
    # if a point is not core, could be "border" or "noise"
    for non_core in non_core_points:
        if (non_core !=[]):
            check_point = non_core[0]
            #isborder = False
            if (check_point in core_border):
                border.append(check_point)
            else:
                noise.append(check_point)
   
    print ("core is: ",core)
    print ("border is: ",border)
    print ("noise is: ",noise)
    

def main():
    data = [(3,10), (5,6), (9,5), (2,8), (8,5), (4,6), (3,3), (5,7), (6,9)]
    radius = 3
    MinPts = 3
    dbscan(data,radius,MinPts)
    print ("--------")
    print ("standard: ")
    dbscan_build_in_module() # -1 represent noise
    


main()