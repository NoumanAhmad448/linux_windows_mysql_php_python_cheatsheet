```
import pandas as pd
```
```
data_pd = pd.read_csv("sample_data.csv")
index = 0
image_name = data_pd.iloc[index, 0]
image_label = data_pd.iloc[index, 1]
```
drop nan data
```
data.dropna(subset=['sender', 'recipients'], inplace=True)
```
Iterate for loop reterive data 
```
data.iterrows()
```
Add new column using existed column
```
data['sender'] = data['message'].str.extract('From: (.+?)\n')
```
