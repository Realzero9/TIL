import pandas as pd
import numpy as np

## 1======
df = pd.read_csv('7.2-1_basic1.csv')
df.head()

df = df.sort_values(by='f5', ascending=False)
min = df['f5'][:10].min()

df['f5'][:10] = min
df.head(10)

df_mean = df[df['age'] >= 80]['f5'].mean()
print(df_mean)
## ======


## 2======
df2 = pd.read_csv('7.2-1_basic1.csv')
df2.head()

df70 = df2[:int((len(df)*0.7))]
df70.tail()

df70.isnull().sum()
df70_std = df70['f1'].std()

med = df70['f1'].median()
df70['f1'] = df70['f1'].fillna(med)

df70_std2 = df70['f1'].std()

print(df70_std-df70_std2)
## ======


## 3======
df3 = pd.read_csv('7.2-1_basic1.csv')
df3.head()

df3.info()
df3.describe()

mean = df3['age'].mean()
std = df3['age'].std()

min = mean - (std*1.5)
max = mean + (std*1.5)

sum = df3[(df3['age']<min)|(df3['age']>max)]['age'].sum()
print(sum)
## ======
