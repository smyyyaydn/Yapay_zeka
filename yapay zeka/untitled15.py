import pandas as pd
import numpy as np
import simpsom as sps
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import csv


#Verisetinin yüklenmesi
veri=pd.read_csv("C:/Users/smyyy/OneDrive/Masaüstü/Mall_Customers.csv")

#verileri düzenleme eklem çıkarma
X=veri.drop(["CustomerID","Genre"],axis=1)

#Ağın oluşturması
net=sps.SOMNet(20, 20, X.values, PBC=True)

#ağın eğitilmesi
net.train("batch",1000)

#Veri noktalarının iki boyutlu bir haritaya gömülemsi ve kümelemenin yapılması
hrt=np.array((net.project(X.values)))
kort=KMeans(n_clusters=3, max_iter=200, random_state=0)


#Örneklerin hangi kümeye ait olduğu belirlenir
y_ort=kort.fit_predict(hrt)

#kümelerin etiketlenmesi
veri["kümeler"]=kort.labels_


print(veri[veri["kümeler"]==0].head(5))

#2 numaralı kümelerin değerlierinin bulunması
print(veri[veri["kümeler"]==1].head(5))

#3 numaralı kümelerin değerlierinin bulunması
print(veri[veri["kümeler"]==2].head(5))


pd.set_option('display.max_columns',None)

