import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('POO\Reconocimiento\data.csv')

df = df.rename({'concave points_mean': 'concave_points_mean','concave points_worst': 'concave_points_worst'}, axis=1) 
pd.set_option("display.max_columns", None)

print(df.isnull().sum()) 

df=df.drop(['id','Unnamed: 32'],axis=1)
df=pd.get_dummies(df,drop_first=True)

plt.figure(figsize=(20,20))
cor=df.corr()
sns.heatmap(cor,annot=True)
plt.show()

max_thresold1 = df['perimeter_mean'].quantile(0.99)
print(max_thresold1)
print(df[df['perimeter_mean']>max_thresold1])

max_thresold2 = df['perimeter_worst'].quantile(0.99)
max_thresold2
df[df['perimeter_worst']>max_thresold2]

max_thresold3 = df['area_worst'].quantile(0.99)
max_thresold3
df[df['area_worst']>max_thresold3]

df = df.drop(df.index[[46,82,101,151,180,352,461,538,539,568]])

X=df[['radius_worst','concave_points_mean','perimeter_worst','concave_points_worst']]
y=pd.DataFrame(df['diagnosis_M'])
y=pd.get_dummies(y,drop_first=True)

plt.figure(figsize=(20,20))
corr=X.corr()
sns.heatmap(corr,annot=True)

plt.show()

param_grid = [    
    {'penalty' : ['l1', 'l2', 'elasticnet', 'none'],
    'C' : np.logspace(-4, 4, 20),
    'solver' : ['lbfgs','newton-cg','liblinear','sag','saga'],
    'max_iter' : [100, 1000,2500, 5000]
    }
]

logReg = LogisticRegression(solver='liblinear')

clf = GridSearchCV(logReg, param_grid = param_grid, cv = 3, verbose=True, n_jobs=-1)

X2 = df[['radius_mean','perimeter_mean','area_mean','concavity_mean','concave_points_mean','radius_worst','perimeter_worst','area_worst','concavity_worst','concave_points_worst']]

X_train,X_test,y_train,y_test=train_test_split(X2,y,test_size=0.23)

best_clf = clf.fit(X2,y)

best_clf.best_estimator_
print (f'Accuracy - : {best_clf.score(X2,y):.3f}')