import numpy as np
import pandas as pd
import matplotlib.pyplot as pp
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn import tree, preprocessing
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder, LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import joblib

tab = pd.read_csv('https://raw.githubusercontent.com/quentingourier/c478_dnq/main/MatchTimelinesFirst15.csv')
# print(tab)

X = tab.drop(columns = ['matchId', 'blue_win', 'blueDragonKills', 'redDragonKills','blueJungleMinionsKilled','blueAvgLevel','redJungleMinionsKilled','redAvgLevel','blueHeraldKills','redHeraldKills'])
y = tab['blue_win']

print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, stratify = y)

model = GradientBoostingClassifier(loss='deviance', max_depth = 8, n_estimators= 200,
                                   learning_rate=0.1)
model.fit(X_train, y_train) #train the model
joblib.dump(model, "lol15.pkl")

prediction = model.predict(X_test)

score = accuracy_score(y_test, prediction)
print(score)

# print(prediction)

predictions = model.predict(X_test)
cm = confusion_matrix(y_test, predictions, labels=model.classes_)
# print(cm)

# print(predictions)

print(classification_report(y_test, predictions, labels=model.classes_))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot()
pp.show()

from joblib import dump, load
dump(model, 'GBC_DNQ_15.joblib')