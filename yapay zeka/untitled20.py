import pandas as pd
import SimpSOM  as sps 
from sklearn.cluster import KMeans
import numpy as np

veri=pd.read_csv("C:/Users/smyyy/OneDrive/Masaüstü/airline-safety.csv")
x=veri.drop(["airline","avail_seat_km_per_week"], axis=1)


net=sps.somNet(20,20, x.values,PBC=True)
net.train(0.01,1000)

hrt=np.array(net.project(x.values))
kort=KMeans(n_cluster=3, max_iter=300,random_state=0)

y_ort=kort.fit_predict(hrt)


veri["kümeler"]=kort.labels_

print(veri[veri["kümeler"]==0].head(5))
print(veri[veri["kümeler"]==1].head(5))
print(veri[veri["kümeler"]==2].head(5))

pd.set_option('display.max_columns',None)
