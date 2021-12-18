import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score

df1 = pd.read_csv("OC_DF.csv")
df2 = pd.read_csv("OC_user_rating_DF.csv")
df = pd.merge(df1, df2, on="title")
df.dropna(subset = ["rating"], inplace=True)
df.dropna(subset = ["year"], inplace=True)

df_train = df.iloc[:518,:]
df_test = df.iloc[519:,:]

x_train = df_train['year']
y_train = df_train['rating']
x_test = df_test['year']
y_test = df_test['rating']

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)

clf = LinearRegression(normalize=True)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(r2_score(y_test,y_pred))