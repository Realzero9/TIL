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
    
df = pd.read_csv("6.train_insurance.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='charges')

# X_train.shape, X_test.shape, y_train.shape, y_test.shape

X_train.info()
X_train['smoker'].unique()
X_train['region'].unique()
X_train.isnull().sum()
X_test.isnull().sum()
X_train.head()
X_train.columns
#Index(['id', 'age', 'sex', 'bmi', 'children', 'smoker', 'region'], dtype='object')
# X_test_id = X_test.pop('id')

# from sklearn.preprocessing import LabelEncoder
cols = ['sex', 'smoker', 'region']
# for col in cols:
#     le = LabelEncoder()
#     X_train[col] = le.fit_transform(X_train[col])
#     X_test[col] = le.fit_transform(X_test[col])

X_train = pd.get_dummies(X_train, columns=cols)
X_test = pd.get_dummies(X_test, columns=cols)

X_train.head()
y_train.nunique()

y_train['charges'] = np.log1p(y_train['charges'])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train['bmi'] = scaler.fit_transform(X_train[['bmi']])
X_test['bmi'] = scaler.transform(X_test[['bmi']])

X_train['age'] = X_train['age'].apply(lambda x: x//10)
X_test['age'] = X_test['age'].apply(lambda x: x//10)

X_train.head()


target = y_train['charges']
X_train = X_train.drop('id', axis=1)

from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(X_train, target, test_size=0.2, random_state=10)
# X_tr.shape, X_val.shape, y_tr.shape, y_val.shape

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import mean_squared_error
def rmse2(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

rmse2(y_val, pred)

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true-y_pred)**2))

rmse(y_val, pred)


from xgboost import XGBRegressor
xgb = XGBRegressor()
xgb.fit(X_tr, y_tr)
pred1 = xgb.predict(X_val)

rmse2(y_val, pred1)
# rmse(y_val, pred1)

'''# 연속형 변수는 불가능!
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_val, pred))
print(roc_auc_score(y_val, pred1))'''

rf.fit(X_train, target)
pred2 = rf.predict(X_test.drop('id', axis=1))

# y_test['charges'] = np.log1p(y_test['charges'])
y = y_test['charges']

rmse2(y, pred2)
rmse(y, pred2)

pred22 = np.exp(pred2)

output = pd.DataFrame({'id': X_test.index, 'charges': pred22})
output.head()

output.to_csv('6.result_0000.csv', index=False)
rmse(y, pred22)