import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

veri=pd.read_csv("C:/Users/smyyy/OneDrive\Masaüstü/train.csv")

label_encoder=LabelEncoder().fit(veri.price_range)
labels=label_encoder.transform(veri.price_range)
classes=list(label_encoder.classes_)

x=veri.drop(["price_range"],axis=1)
y=labels

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from tensorflow.keras.utils import to_categorical
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)


from.tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model=Sequential()
model.add(Dense(16,input_dim=20,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(4,activation="softmax"))
model.summary()

model.compile(lost="categorical_crossentropy",optimizer="adam",metrics="accuracy")
model.fit(x_train,y_train,validation_data=(x_test,y_test),epoch=50)
print("ortalama eğitim kaybı",np.mean(model.history.history["loss"]))
print("ortalama eğitim başarımı",np.mean(model.history.history["accuracy"]))
print("ortalama eğitim kaybı",np.mean(model.history.history["val_loss"]))
print("ortalama doğrulama başarımı ",np.mean(model.history.history["val_accuracy"]))

import matplotlib.pyplot as plt
plt.plot(model.history.history["loss"])
plt.plot(model.history.history["val_loss"])
plt.title("model kaybı")
plt.ylabel("kayıp")
plt.xlabel("epok")
plt.legend(["eğitim","test"],loc="upper left")
plt.show()

