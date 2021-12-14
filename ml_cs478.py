# Topic: Final Project CS478
# Machine learning code created by Quentin using: 
#    - sklearn (model, training, testing, metrics)
#    - pandas (data management)
#    - matplotlib (displaying, graphs)
#    - joblib (saving the model)
# Last version: 12/07/21



#IMPORTS
#-----------------------------------------------------------------------------------------------------------
import joblib
import pandas as pd
import matplotlib.pyplot as pp
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn import tree, preprocessing
from sklearn.ensemble import GradientBoostingClassifier
from joblib import dump, load
#-----------------------------------------------------------------------------------------------------------



#DATA READING & INITIALIZATION
#-----------------------------------------------------------------------------------------------------------
tab = pd.read_csv('https://raw.githubusercontent.com/quentingourier/c478_dnq/main/MatchTimelinesFirst15.csv') #read data from url
# print(tab)

X = tab.drop(columns = ['matchId', 'blue_win', 'blueDragonKills', 'redDragonKills', 'blueJungleMinionsKilled','blueAvgLevel',
                        'redJungleMinionsKilled','redAvgLevel','blueHeraldKills','redHeraldKills']) #droping useless columns
y = tab['blue_win'] #blue win is used as an output (binary output : 0 red win and 1 blue win)
# print(X)
#-----------------------------------------------------------------------------------------------------------



#MACHINE LEARNING PROCESS & MODELING
#-----------------------------------------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, stratify = y) #training 90% and testing 10%

model = GradientBoostingClassifier(loss='deviance', max_depth = 8, n_estimators= 200,
                                   learning_rate=0.1) #GBC is using Decision Tree and try to minimize the error value
model.fit(X_train, y_train) #training process (longest part)
#-----------------------------------------------------------------------------------------------------------



#PREDICTION & RESULTS
#-----------------------------------------------------------------------------------------------------------
prediction = model.predict(X_test) #run a prediction test on the testing inputs left to test the model

score = accuracy_score(y_test, prediction) #display the accuracy rate of the trained model ([0.0 -> 1.0])
# print(score)
# print(prediction) #display the output prediction of the inputs parameters

cm = confusion_matrix(y_test, prediction, labels=model.classes_)
# print(cm)

print(classification_report(y_test, prediction, labels=model.classes_)) #classification report tab (precision, recall, etc)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_) #confusion matrix made from classification report
disp.plot()
pp.show()
#-----------------------------------------------------------------------------------------------------------



#SAVING
#-----------------------------------------------------------------------------------------------------------
dump(model, 'GBC_DNQ_15.joblib') #dumps the model -> saving it as a joblib file to be loaded afterward
#-----------------------------------------------------------------------------------------------------------



#This is the code implemented in the user interface
#Version 1.2
