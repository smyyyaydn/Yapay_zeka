import pandas as pd
import numpy as np
import simpsom as sps
from sklearn.cluster import KMeans

#Verisetinin yüklenmesi
veri=pd.read_csv("C:/Users/smyyy/OneDrive/Masaüstü/cc.csv")

#Null değerlerin doldurlması
veri=veri.fillna(veri.mean())

#verileri düzenleme eklem çıkarma

#X=veri.drop(["CUST_ID","BALANCE","PURCHASES","ONEOFF_PURCHASES","INSTALLMENTS_PURCHASES","CASH_ADVANCE","PURCHASES_FREQUENCY","ONEOFF_PURCHASES_FREQUENCY","PURCHASES_INSTALLMENTS_FREQUENCY","CASH_ADVANCE_FREQUENCY","CASH_ADVANCE_TRX","PURCHASES_TRX","TENURE"],axis=1)
X=veri.drop(["CUST_ID"],axis=1)

#Ağın oluşturması
net=sps.SOMNet(20, 20, X.values, PBC=True)

#ağın eğitilmesi
net.train("batch",10)

#Veri noktalarının iki boyutlu bir haritaya gömülemsi ve kümelemenin yapılması
hrt=np.array((net.project(X.values)))
kort=KMeans(n_clusters=3, max_iter=8951, random_state=0)


#Örneklerin hangi kümeye ait olduğu belirlenir
y_ort=kort.fit_predict(hrt)

#kümelerin etiketlenmesi
veri["kümeler"]=kort.labels_

#1 numaralı kümelerin değerlierinin bulunması
print(veri[veri["kümeler"]==0].head(5))

#2 numaralı kümelerin değerlierinin bulunması
print(veri[veri["kümeler"]==1].head(5))

#3 numaralı kümelerin değerlierinin bulunması
print(veri[veri["kümeler"]==2].head(5))


pd.set_option('display.max_columns',None)