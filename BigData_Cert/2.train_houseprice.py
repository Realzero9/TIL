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
    
    X_train, X_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=2021)
    y_train = X_train[[id_name, target]]
    X_train = X_train.drop(columns=[id_name, target])
    y_test = X_test[[id_name, target]]
    X_test = X_test.drop(columns=[id_name, target])
    return X_train, X_test, y_train, y_test 
    
df = pd.read_csv("train_houseprice.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='SalePrice', id_name='Id')

# X_train.shape, X_test.shape, y_train.shape, y_test.shape
# X_train.info()

X_train.isnull().sum().sort_values(ascending=False)[:20]
X_test.isnull().sum().sort_values(ascending=False)[:20]

X_train_n = X_train.select_dtypes(exclude=['object'])
X_test_n = X_test.select_dtypes(exclude=['object'])

target = y_train['SalePrice']

# X_train_n.head(3)
from sklearn.impute import SimpleImputer

imp = SimpleImputer()
X_train_n = imp.fit_transform(X_train_n)
X_test_n = imp.fit_transform(X_test_n)

x_train, x_val, Y_train, Y_val = train_test_split(X_train_n, target, test_size=0.2, random_state=10)

from sklearn.metrics import roc_auc_score, mean_squared_error
def rmsle(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBRegressor
from sklearn.svm import SVC

model = SVC(random_state=10)
model.fit(x_train, Y_train)
pred = model.predict(x_val)
print('RMSLE : ' + str(rmsle(Y_val, pred)))

model1 = XGBRegressor()
model1.fit(x_train, Y_train, verbose=False)
pred1 = model1.predict(x_val)
print('RMSLE : ' + str(rmsle(Y_val, pred1)))

model2 = RandomForestClassifier()
model2.fit(x_train, Y_train)
pred2 = model2.predict(x_val)
print('RMSLE : ' + str(rmsle(Y_val, pred2)))

y = y_train['SalePrice']

final_model = XGBRegressor()
final_model.fit(X_train_n, y)
prediction = final_model.predict(X_test_n)

y_test
submission = pd.DataFrame(data={'ID':y_test.Id, 'income': prediction})
# submission.head()

submission.to_csv('houseprice_0000.csv', index=False)
print('RMSLE : ' + str(rmsle(y_test['SalePrice'], prediction)))