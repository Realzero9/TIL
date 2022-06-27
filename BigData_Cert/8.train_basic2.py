# 라이브러리 불러오기
import pandas as pd

df = pd.read_csv("8.train_basic2.csv", parse_dates=['Date'])
df.head()
df.info()
df.isnull().sum()

df['year'] = df['Date'].dt.year
df['mon'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['dayofweek'] = df['Date'].dt.dayofweek

df['weekend'] = df['dayofweek'].apply(lambda x: x>=5, 1, 0)
df.head()

weekend_con = (df['year']==2022)&(df['mon']==5)&(df['weekend'])
weekday_con = (df['year']==2022)&(df['mon']==5)&(~df['weekend'])

end_sale = round(df[weekend_con]['Sales'].mean(), 2)
day_sale = round(df[weekday_con]['Sales'].mean(), 2)

result = end_sale - day_sale
print(round(result,2))