#import libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from taipy import Gui

#load data about past eruptions from Yellowstone National Park USA
df= pd.read_csv("/home/kami/Desktop/GHW/taipy_project/faithful.csv")


#format the data to be useful for the KMeans algorithm- It does not take in Dataframes but .values converts them to Numpy arrays
#we use Capital X because it is a matrix
X= df.values 

#building the KMeans model
kmeans= KMeans(n_clusters=2,    #specifies the number of clusters
               init= 'random',  #specifies how we want to initialize the centroids
               max_iter=300     #specifies the maximum number of iterations
               )

#fit the model
kmeans.fit(X)

print('Cluster centers:', kmeans.cluster_centers_[0], kmeans.cluster_centers_[1])
print('SSE:', kmeans.inertia_)             #standard square errors
print('# of iterations:', kmeans.n_iter_)

#show the classifications that resulted from the model fit
flags= kmeans.labels_
print(flags)