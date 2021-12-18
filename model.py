import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("OC_DF.csv")
df.dropna(subset = ["rating"], inplace=True)
df.dropna(subset = ["year"], inplace=True)

Y = df.rating
X = df.drop(['title','genre','actor','imdb_id','kind','matched_by','rating','votes'], axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

X_train.shape, Y_train.shape
#(532,1) (532,1)
X_test.shape, Y_test.shape
#(134,1) (134,1)

model = linear_model.LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

# print('Coefficients:', model.coef_)
# print('Intercept:', model.intercept_)
# print('Mean squared error (MSE): %.2f'
#       % mean_squared_error(Y_test, Y_pred))
# print('Coefficient of determination (R^2): %.2f'
#       % r2_score(Y_test, Y_pred))
#Y=-0.11188241(year) + 232.81646130373971
