import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
    There are 3 interval to calculate, 
    [60,91): liner increase with higher increasing rate
    [90,95): liner increase with lower increasing rate
    [95,101): constent, 4.3
"""

def main():
    input_score = [ 61, 67, 69, 71, 78, 79, 81, 82, 83, 84, 85, 85, 86, 87, 87, 88, 89, 89, 90, 93, 95, 95, 96, 98]
    output_score = []
    normalize_score = []
    k_69 = (4.0 - 1.0) / (90-60)
    b_69 = 4-k_69*90
    
    k_90_94 = (4.3-4.0) / (94-90)
    b_90_94 = 4.3-k_90_94*94
    
    for score in input_score:
        if (score in range (60,91)):
            convert_score = k_69*score + b_69
        elif (score in range (91,95)):
            convert_score = k_90_94*score + b_90_94
        elif (score >= 95):
            convert_score = 4.3
        # create the general transformation
        output_score.append(round(convert_score,1))
        # create the data after normalization
        normalize_score.append(score/100)

    print ("Score after transformation: ",output_score)
    print ("lenth of array: ",len(output_score))
    print()  

    #-------------- end of data transformation
    # Clustering, Using Quartiles to remove outliers 
    q1 = int(len(input_score)*0.25)
    q3 = int(len(input_score)*0.75)

    IQR = output_score[q3] - output_score[q1]
    outlier_bar = 1.5*IQR

    
    cluster_clean = []
    for out_score in output_score:
        if out_score>outlier_bar:
            cluster_clean.append(out_score)

    print ("Transformation Score after remove outlier: ",cluster_clean)
    print ("lenth of array: ",len(cluster_clean))
    print()

    print ("Q1=",output_score[q1])
    print ("Q3=",output_score[q3])
    print ("IQR=",IQR)
    print ("Outlier_bar=",outlier_bar)

    
    

    # data boxplot credit: http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    
    # plotbox to compare remove the outlier 3-(c)
    data_to_plot3 = [output_score,cluster_clean]

    fig3 = plt.figure(figsize = (6,4))
    ax3 = fig3.add_subplot(111)
    bp3 = ax3.boxplot(data_to_plot3)
    fig3.savefig("Remove outlier.png",bbox_inches='tight')
    
    
    """
    # plotbox to compare the with/without decimal scaling 3-(b)
    data_to_plot1 = [input_score,output_score]
    data_to_plot2 = [normalize_score,output_score]

    # create a figure instance
    fig1 = plt.figure(figsize = (6,4))
    ax1 = fig1.add_subplot(111)
    bp1 = ax1.boxplot(data_to_plot1)
    fig1.savefig("without scaling.png",bbox_inches='tight')

    fig2 = plt.figure(figsize = (6,4))
    ax2 = fig2.add_subplot(111)
    bp2 = ax2.boxplot(data_to_plot2)
    fig2.savefig("decimal scaling.png",bbox_inches='tight')

    """


main()
    