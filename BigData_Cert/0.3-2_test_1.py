import pandas as pd
import numpy as np

df = pd.read_csv('0.3-2_travel_insurance_train.csv')
# df.head()
# df.columns
'''Index(['ID', 'Age', 'Employment Type', 'GraduateOrNot', 'AnnualIncome',
       'FamilyMembers', 'ChronicDiseases', 'FrequentFlyer',
       'EverTravelledAbroad', 'TravelInsurance'],
      dtype='object')
'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df, df['TravelInsurance'], test_size=0.2, random_state=20, stratify=df['TravelInsurance'])

x_train = x_train.drop(['ID', 'TravelInsurance'], axis=1)
x_test = x_test.drop(['ID', 'TravelInsurance'], axis=1)
# x_train.isnull().sum()
# x_test.isnull().sum()

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
# x_train.dtypes
label = ['Employment Type', 'GraduateOrNot', 'FrequentFlyer', 'EverTravelledAbroad']
# x_train[label] = le.fit_transform(x_train[label]) xxxxxxxxxxxxxxxxxxxxxxx
# x_train[label] = x_train[label].apply(LabelEncoder().fit_transform)
# print(x_train[label])
for la in label:
    le = LabelEncoder()
    x_train[la] = le.fit_transform(x_train[la])
    x_test[la] = le.fit_transform(x_test[la])
# print(x_train.info())
# print(x_train['ChronicDiseases'].unique())
for i in label:
    x_train[i] = x_train[i].astype('category')
for i in label:
    x_test[i] = x_test[i].astype('category')

print(x_train.info())
print(x_train.head())
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)
# print(x_train.info())
# print(x_train)

x_train['AnnualIncome_qcut'] = pd.qcut(x_train['AnnualIncome'], 5, labels=False)
x_test['AnnualIncome_qcut'] = pd.qcut(x_test['AnnualIncome'], 5, labels=False)

from sklearn.preprocessing import minmax_scale
# from sklearn.preprocessing import MinMaxScaler # MinMaxScaler()
scaler = ['Age', 'AnnualIncome', 'FamilyMembers']
'''min = MinMaxScaler()
min.fit(x_train[scaler])
# print(x_train)
x_train[scaler] = min.transform(x_train[scaler])
x_test[scaler] = min.transform(x_test[scaler])
'''
# print(x_train)
x_train[scaler] = minmax_scale(x_train[scaler])
x_test[scaler] = minmax_scale(x_test[scaler])

X_train, X_valid, Y_train, Y_valid = train_test_split(x_train, y_train, test_size=0.2, random_state=20, stratify=y_train)


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model1 = LogisticRegression()

model.fit(X_train, Y_train)
model1.fit(X_train, Y_train)

pred = pd.DataFrame(model.predict_proba(X_valid))
pred1 = pd.DataFrame(model1.predict_proba(X_valid))

# print(pred)

from sklearn.metrics import roc_auc_score
roc_auc_score(Y_valid, pred.iloc[:,1])
roc_auc_score(Y_valid, pred1.iloc[:,1])

result = pd.DataFrame(model.predict_proba(x_test))
result = result.iloc[:,1]
# print(result)
pd.DataFrame({'index': x_test.index, 'y_pred': result}).to_csv('0000.csv', index=False)


newfile = pd.read_csv('0000.csv')
np.mean(newfile['y_pred'])


'''
model2 = RandomForestClassifier()
model3 = LogisticRegression()

model2.fit(x_train, y_train)
model3.fit(x_train, y_train)

pred2 = pd.DataFrame(model2.predict_proba(X_valid))
pred3 = pd.DataFrame(model3.predict_proba(X_valid))

roc_auc_score(Y_valid, pred2.iloc[:,1])
roc_auc_score(Y_valid, pred3.iloc[:,1])

result2 = pd.DataFrame(model2.predict_proba(x_test))
result2 = result2.iloc[:,1]
# print(result2)
pd.DataFrame({'index': x_test.index, 'y_pred': result2}).to_csv('0001.csv', index=False)


newfile2 = pd.read_csv('0001.csv')
np.mean(newfile2['y_pred'])'''