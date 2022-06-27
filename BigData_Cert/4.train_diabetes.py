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
    
df = pd.read_csv("4.train_diabetes.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Outcome')

# X_train.shape, X_test.shape, y_train.shape, y_test.shape

X_train.head()
X_train.info()
y_train.head()
y_train.value_counts()
y_train.nunique()
X_train.describe()

len(X_train[(X_train.Glucose == 0)])
len(X_train[(X_train.BloodPressure == 0)])
len(X_train[(X_train.SkinThickness == 0)])
len(X_train[(X_train.Insulin == 0)])
len(X_train[(X_train.BMI == 0)])

len(X_test[(X_test.Glucose == 0)])
len(X_test[(X_test.BloodPressure == 0)])
len(X_test[(X_test.SkinThickness == 0)])
len(X_test[(X_test.Insulin == 0)])
len(X_test[(X_test.BMI == 0)])

del_idx = X_train[(X_train.Glucose == 0)].index
X_train.shape
y_train.shape
X_train = X_train.drop(index=del_idx, axis=0)
y_train = y_train.drop(index=del_idx, axis=0)

cols = ['BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
cols_mean = X_train[cols].mean()
X_train[cols].replace(0, cols_mean)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X_train[cols] = scaler.fit_transform(X_train[cols])
X_test[cols] = scaler.fit_transform(X_test[cols])

X = X_train.drop('id', axis=1)
test = X_test.drop('id', axis=1)

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
model = SVC(random_state=10)
model.fit(X, y_train['Outcome'])
pred = model.predict(test)

round(model.score(X, y_train['Outcome'])*100, 2)

model1 = RandomForestClassifier()
model1.fit(X, y_train['Outcome'])
pred1 = model1.predict(test)

from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test['Outcome'], pred))
print(roc_auc_score(y_test['Outcome'], pred1))
# round(model1.score(X, y_train['Outcome'])*100, 2)

output = pd.DataFrame({'idx' : X_test.index, 'Outcome': pred1})
output.head()

output.to_csv('4.result_0000.csv', index=False)
