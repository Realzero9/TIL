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
    
df = pd.read_csv("1.train_ReachedOnTime.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Reached.on.Time_Y.N', id_name='ID')
# X_train.shape, X_test.shape, y_train.shape, y_test.shape

X_train.info()
X_train.head()
X_train.isnull().sum()
X_test.isnull().sum()
y_train.head()

X_train.select_dtypes('object').columns
X_train[['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']].nunique()
cate = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']

from sklearn.preprocessing import LabelEncoder
for i in cate:
    le = LabelEncoder()
    X_train[i] = le.fit_transform(X_train[i])
    X_test[i] = le.fit_transform(X_test[i])


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier

X_train = X_train.drop('ID', axis=1)
X_test_id = X_test.pop('ID')
y_train = y_train.drop('ID', axis=1)

from sklearn.model_selection import train_test_split
X_tr, X_val, Y_tr, Y_val = train_test_split(X_train, y_train['Reached.on.Time_Y.N'], test_size=0.2, random_state=10)

model1 = LogisticRegression()
model1.fit(X_tr, Y_tr)
print(round((model1.score(X_val, Y_val))*100,2)) #62.16
# pred1 = model1.predict_proba(X_val)
# print(roc_auc_score(Y_val, pred1))
model2 = SVC()
model2.fit(X_tr, Y_tr)
print(round((model2.score(X_val, Y_val))*100,2)) #65.34
# pred2 = model2.predict_proba(X_val)
# print(roc_auc_score(Y_val, pred2))
model3 = DecisionTreeClassifier()
model3.fit(X_tr, Y_tr)
print(round((model3.score(X_val, Y_val))*100,2)) #64.15
# pred3 = model3.predict_proba(X_val)
# print(roc_auc_score(Y_val, pred3))
model4 = RandomForestClassifier()
model4.fit(X_tr, Y_tr)
print(round((model4.score(X_val, Y_val))*100,2)) #66.08
# pred4 = model4.predict_proba(X_val)
# print(roc_auc_score(Y_val, pred4))
model5 = XGBClassifier()
model5.fit(X_tr, Y_tr)
print(round((model5.score(X_val, Y_val))*100,2)) #65.74
# pred5 = model5.predict_proba(X_val)
# print(roc_auc_score(Y_val, pred5))

from sklearn.metrics import roc_auc_score
model6 = KNeighborsClassifier()
model6.fit(X_tr, Y_tr)
print(round((model6.score(X_val, Y_val))*100,2)) #67.33
model6.fit(X_train, y_train)
pred6 = model6.predict(X_test)
print(roc_auc_score(y_test['Reached.on.Time_Y.N'], pred6))

output = pd.DataFrame({'id': X_test_id, 'Reached.on.Time_Y.N': pred6})
output.to_csv('11.0000.csv', index=False)

