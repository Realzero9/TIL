# 시험환경 세팅 (코드 변경 X)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def exam_data_load(df, target, id_name="", null_name=""):
    if id_name == "":
        df = df.reset_index().rename(columns={"index": "id"})
        id_name = 'id'
    else:
        id_name = id_name
    
    if null_name != "":
        df[df == null_name] = np.nan
    
    X_train, X_test = train_test_split(df, test_size=0.2, random_state=2021)
    
    y_train = X_train[[id_name, target]]
    X_train = X_train.drop(columns=[target])

    
    y_test = X_test[[id_name, target]]
    X_test = X_test.drop(columns=[target])
    return X_train, X_test, y_train, y_test 
    
df = pd.read_csv("3.train_titanic.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Survived', id_name='PassengerId')

# X_train.shape, X_test.shape, y_train.shape, y_test.shape

X_train.isnull().sum()
X_train.info()
y_train.head()

y_train['Survived'].value_counts()

y = y_train['Survived']
cols = ['Pclass', 'Sex', 'SibSp', 'Parch']
X = pd.get_dummies(X_train[cols])
test = pd.get_dummies(X_test[cols])

# X.shape, test.shape

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=10)
model.fit(X, y)
predictions = model.predict(test)

model.score(X, y)

output = pd.DataFrame({'PassengerId' : X_test.PassengerId, 'Survived':predictions})
output.head()

output.to_csv('3.result_0000.csv', index=False)
model.score(test, y_test['Survived'])