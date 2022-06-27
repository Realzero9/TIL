import pandas as pd
import numpy as np

df = pd.read_csv('0.3-2_travel_insurance_train.csv')
# df.info()
# df.isnull().sum()
# df.describe()
df.columns
'''Index(['ID', 'Age', 'Employment Type', 'GraduateOrNot', 'AnnualIncome',
       'FamilyMembers', 'ChronicDiseases', 'FrequentFlyer',
       'EverTravelledAbroad', 'TravelInsurance'],
      dtype='object')
'''

# df['TravelInsurance'].value_counts()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df, df['TravelInsurance'], test_size=0.2, stratify=df['TravelInsurance'])
print(X_train.shape, X_test.shape)


n_X_train = X_train.select_dtypes(exclude='object').copy()
c_X_train = X_train.select_dtypes(include='object').copy()
n_X_test = X_test.select_dtypes(exclude='object').copy()
c_X_test = X_test.select_dtypes(include='object').copy()

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
cols = ['Age', 'AnnualIncome', 'FamilyMembers', 'ChronicDiseases']

n_X_train[cols] = scaler.fit_transform(n_X_train[cols])
n_X_test[cols] = scaler.fit_transform(n_X_test[cols])
# n_X_train.head()

c_X_train = pd.get_dummies(c_X_train)
c_X_test = pd.get_dummies(c_X_test)
# c_X_train.head()

X_train = pd.concat([n_X_train, c_X_train], axis=1)
X_test = pd.concat([n_X_test, c_X_test], axis=1)
# print(X_train.shape, X_test.shape)

x_train, x_val, y_train, y_val = train_test_split(X_train.drop('TravelInsurance', axis=1), X_train['TravelInsurance'], test_size=0.1, stratify=X_train['TravelInsurance'])
# print(x_train.shape, x_val.shape)
# print(y_train.shape, y_val.shape)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=10, max_depth=10, random_state=10)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_val)[:,1]
print(pred)


from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_val, pred))

X_test = X_test.drop('TravelInsurance', axis=1)
pred1 = rf.predict_proba(X_test)[:,1]
print(pred1)

print(roc_auc_score(y_test, pred1))

pd.DataFrame({'index': X_test.index, 'y_pred': pred1}).to_csv('0002.csv', index=False)
result = pd.read_csv('0002.csv')
print(result)
