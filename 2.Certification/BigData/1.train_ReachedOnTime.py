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
# X_train.head()
# y_train.head()

y_train['Reached.on.Time_Y.N'].value_counts()
X_train.isnull().sum() 
X_test.isnull().sum() 

X_train.info()
X_train.columns
'''Index(['ID', 'Warehouse_block', 'Mode_of_Shipment', 'Customer_care_calls',
       'Customer_rating', 'Cost_of_the_Product', 'Prior_purchases',
       'Product_importance', 'Gender', 'Discount_offered', 'Weight_in_gms'],
      dtype='object')'''

cols = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
from sklearn.preprocessing import LabelEncoder
for col in cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col])
    X_test[col] = le.fit_transform(X_test[col])
# print(X_train)

# X_train.Warehouse_block.unique()
# X_train.Mode_of_Shipment.unique()

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

X_train_id = X_train.pop('ID')
X_test_id = X_test.pop('ID')

x_tr, x_val, y_tr, y_val = train_test_split(X_train, y_train['Reached.on.Time_Y.N'], test_size=0.2, random_state=10)

model_lr = LogisticRegression()
model_lr.fit(x_tr, y_tr)
round(model_lr.score(x_val, y_val)*100, 2)
# 62.16

model_kn = KNeighborsClassifier()
model_kn.fit(x_tr, y_tr)
round(model_kn.score(x_val, y_val)*100, 2)
# 67.33

model_svc = SVC()
model_svc.fit(x_tr, y_tr)
round(model_svc.score(x_val, y_val)*100, 2)
# 65.34

model_tr = DecisionTreeClassifier()
model_tr.fit(x_tr, y_tr)
round(model_tr.score(x_val, y_val)*100, 2)
# 65.85

model_rf = RandomForestClassifier()
model_rf.fit(x_tr, y_tr)
round(model_rf.score(x_val, y_val)*100, 2)
# 66.48

model_xg = XGBClassifier()
model_xg.fit(x_tr, y_tr)
round(model_xg.score(x_val, y_val)*100, 2)
# 65.74




model_kn = KNeighborsClassifier()
model_kn.fit(X_train, y_train)
pred = model_kn.predict(X_test)[:,1]
print(pred)

from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test['Reached.on.Time_Y.N'], pred))

# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'cust_id': X_test.cust_id, 'gender': pred}).to_csv('003000000.csv', index=False)
pd.DataFrame({'ID': X_test_id, 'Reached.on.Time_Y.N': pred}).to_csv('t2_0002.csv', index=False)