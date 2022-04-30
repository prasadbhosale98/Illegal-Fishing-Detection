import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

df = pd.read_csv("D:/illegalfishing/dashboard/trollers.csv")
df.head(-5)

df.isnull().sum()

df1 = df.fillna(df.mean())
df1.head(-5)

df1.isnull().sum()

X = df1.drop('is_fishing', axis=1)
Y = df1.is_fishing
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=10)
model = LGBMClassifier()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print('Prediction' + str(pred))
print('Accurancy score :'+ str(model.score(X_test, y_test)))
print('Recall score' + str(recall_score(y_test, pred)))
print('f1 score' + str(f1_score(y_test, pred)))
print('Confusion matrix' + str(confusion_matrix(y_test, pred)))


