# 시험환경 세팅 (코드 변경 X)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import train

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
    
df = pd.read_csv("5.train_adult.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='income', null_name='?')

# X_train.shape, X_test.shape, y_train.shape, y_test.shape
X_train.info()
X_train.isnull().sum()
y_train.income.unique()
y_train.info()
y_train['income'].value_counts()


X_train_n = X_train.select_dtypes(exclude='object')
X_train_c = X_train.select_dtypes(include='object')
X_train_n.columns
X_train_c.columns

Nume = ['age', 'fnlwgt', 'education.num', 'capital.gain', 'capital.loss', 'hours.per.week']
cate = ['workclass', 'education', 'marital.status', 'occupation', 'relationship', 'race', 'sex', 'native.country']

X_train_n.describe()
X_train_c.describe()

from sklearn.preprocessing import LabelEncoder
# col = ['income']
le = LabelEncoder()
# y_train[col] = y_train[col].apply(le.fit_transform)
# y_test[col] = y_test[col].apply(le.fit_transform)

# for i in col:
#     le = LabelEncoder()
#     y_train[col] = le.fit_transform(y_train[col])
#     y_test[col] = le.fit_transform(y_test[col])

X_train['workclass'].value_counts().mode()[0]
X_train['occupation'].value_counts().mode()[0]
X_train['native.country'].value_counts().mode()[0]

def data_fillna(df):
    df['workclass'] = df['workclass'].fillna(df['workclass'].mode()[0])
    df['occupation'] = df['occupation'].fillna('null')
    df['native.country'] = df['native.country'].fillna(df['native.country'].mode()[0])
    return df

X_train = data_fillna(X_train)
X_test = data_fillna(X_test)

X_train.isnull().sum()


from sklearn.preprocessing import LabelEncoder
all_df = pd.concat([X_train.assign(ind='train'), X_test.assign(ind='test')])
all_df[cate] = all_df[cate].apply(le.fit_transform)

X_train = all_df[all_df['ind']=='train']
X_train = X_train.drop('ind', axis=1)
X_test = all_df[all_df['ind']=='test']
X_test = X_test.drop('ind', axis=1)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train[Nume] = scaler.fit_transform(X_train[Nume])
X_test[Nume] = scaler.transform(X_test[Nume])


y = (y_train['income'] != '<=50K').astype(int)

from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y, test_size=0.2, random_state=10)
X_tr.shape, X_val.shape, y_tr.shape, y_val.shape

X_tr.head()

X_tr = X_tr.drop('id', axis=1)
X_val = X_val.drop('id', axis=1)


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
model = DecisionTreeClassifier()
model.fit(X_tr, y_tr)
pred = model.predict(X_val)
print('acc score', (accuracy_score(y_val, pred)))

from sklearn.ensemble import RandomForestClassifier
model1 = RandomForestClassifier()
model1.fit(X_tr, y_tr)
pred1 = model1.predict(X_val)
print('acc score', (accuracy_score(y_val, pred1)))

X_test_id = X_test.pop('id')
pred2 = model1.predict(X_test)

output = pd.DataFrame({'id': X_test_id, 'income': pred2})
output.to_csv('5.result_0000.csv', index=False)

y_test = (y_test['income'] != '<=50K').astype(int)
print('acc score', (accuracy_score(y_test, pred2)))