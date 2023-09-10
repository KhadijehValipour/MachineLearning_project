import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


# load data
data = pd.read_csv('dataset.csv' , header=None) 
data = data.dropna()
data = data.iloc[1:]

X = data.iloc[:,:-1].values  # همه ردیف ها تا ستون اخر
Y = data.iloc[: , -1].values # همه ردیف ها فقط ستون اخرشون

enc = OneHotEncoder()
enc.fit(Y)
onehotlabels = enc.transform(Y).toarray()
labels = pd.DataFrame(onehotlabels)



X_train , X_test ,Y_train ,Y_test = train_test_split(X,Y,test_size=0.2,shuffle=True)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(12 , activation='sigmoid') , 
    tf.keras.layers.Dense(30,activation='relu') , 
    tf.keras.layers.Dense(16,activation='relu') , 
    tf.keras.layers.Dense(4 , activation='softmax')
])

model.compile(optimizer='adam' ,
              loss='sparse_categorical_crossentropy' , 
              metrics=['accuracy']
)

output = model.fit(X_train,Y_train,epochs=100)

model.evaluate(X_test ,Y_test)

loss , accuracy = model.evaluate(X_test,Y_test)

model.save('snake_game_model.h5')