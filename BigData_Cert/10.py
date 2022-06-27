import pandas as pd
import numpy as np

df = pd.read_csv('0.3-2_travel_insurance_train.csv')

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(df, df['TravelInsurance'], test_size=0.2, stratify=df['TravelInsurance'])

X_train.info()
X_train.head()

# X_train.select_dtypes('object').columns
X_train_c = X_train.select_dtypes(include='object').copy()
ob = ['Employment Type', 'GraduateOrNot', 'FrequentFlyer', 'EverTravelledAbroad']
X_train_n = X_train.select_dtypes(exclude='object').copy()
nu = ['Age', 'AnnualIncome', 'FamilyMembers', 'ChronicDiseases']
X_test_c = X_test.select_dtypes(include='object').copy()
X_test_n = X_test.select_dtypes(exclude='object').copy()

from sklearn.preprocessing import RobustScaler
rs = RobustScaler()
X_train_n[nu] = rs.fit_transform(X_train_n[nu])
X_test_n[nu] = rs.fit_transform(X_test[nu])

# from sklearn.preprocessing import LabelEncoder
X_train_c = pd.get_dummies(X_train_c)
X_test_c = pd.get_dummies(X_test_c)

X_train = pd.concat([X_train_n, X_train_c], axis=1)
X_test = pd.concat([X_test_n, X_test_c], axis=1)

X_train = X_train.drop('ID', axis=1)

X_tr, X_val, y_tr, y_val = train_test_split(X_train.drop('TravelInsurance', axis=1), X_train['TravelInsurance'], test_size=0.2, stratify=Y_train)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10, random_state=10, max_depth=10)
model.fit(X_tr, y_tr)
pred = model.predict_proba(X_val)[:,1]
pred

from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_val, pred))

X_test = X_test.drop(['ID', 'TravelInsurance'], axis=1)

model1 = RandomForestClassifier(n_estimators=10, random_state=10, max_depth=10)
model1.fit(X_train.drop('TravelInsurance', axis=1), Y_train)
prediction = model.predict_proba(X_test)[:,1]
prediction1 = model1.predict_proba(X_test)[:,1]

print(roc_auc_score(Y_test, prediction))
print(roc_auc_score(Y_test, prediction1))
