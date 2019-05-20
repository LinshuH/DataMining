import numpy as np
from math import sqrt


def E_distance(point,center):
    """
    This function calculate the Euclidean distance between a point and the center
    """
    distance = sqrt(pow((center[0]-point[0]),2)+pow((center[1]-point[1]),2))
    #print ("distance is: ",distance)
    return distance   
    


def one_k_mean (center,data,k):
    """
    center: [] center of cluster
    data: input array of point: [[]]
    k: int, number of cluster for the goal

    final_cluster: [[]]   [[total_square_error],[cluster1] , [cluster2],...] 
                          # cluster: [cluster_center, point1_in_this_cluster, point2, etc]
    center: []
    """
    
    final_cluster = [[],[],[]]
    new_center = []
    for cluster in data:
        for point in cluster:
            # find the minimal distance among all the cluster
            cluster_index = 0  # index, 0-2 which index
            #print ("point is: ",point)
            #print ("center is: ",center)
            min_distance = E_distance(point,center[0]) 
            for i in range (1,k):
                distance = E_distance(point,center[i])
                if (distance<min_distance):
                    min_distance=distance
                    cluster_index = i
            final_cluster[cluster_index].append(point)

    for j in range (len(final_cluster)):
        sum_x = 0
        sum_y = 0
        for po in range (len(final_cluster[j])):
            sum_x += final_cluster[j][po][0]
            sum_y += final_cluster[j][po][1]
        ave_x = sum_x / len(final_cluster[j])
        ave_y = sum_y / len(final_cluster[j])

        center_point = (ave_x,ave_y)

        new_center.append(center_point)

    return new_center,final_cluster
    

def main():
    init_data = [[(3,10), (5,6), (9,5)], [(2,8), (8,5), (4,6)], [(3,3), (5,7), (6,9)]]
    center = [init_data[0][0],init_data[1][0],init_data[2][0]]
    result_cluster = [[],[],[]]
    equal = False
    count = 0
    while (equal==False):
        count += 1
        print ("Iteration: ",count)
        equal = True
        print ("Last stage center is: ",center)
        print ("Last stage cluster: ",init_data)
        center,result_cluster = one_k_mean (center,init_data,3)
        print ("New center is: ",center)
        print ("New cluster: ",result_cluster)
        print ()
        for i in range (len(result_cluster)):
            if (set(result_cluster[i]) != set(init_data[i])):
                equal = False
                init_data = result_cluster

    # if the new and the old are same, print the final cluster
    print ("---------------")
    print ("Final center is: ",center)
    print ("Final cluster: ",result_cluster)


main()
