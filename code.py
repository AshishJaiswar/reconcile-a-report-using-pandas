# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df=pd.read_csv(path)
df['state']=df['state'].apply(lambda x: x.lower())
df['total']=df['Jan']+df['Feb']+df['Mar']
sum_row =df[['Jan','Feb','Mar','total']].sum()
df_final=df.append(sum_row,ignore_index=True)

# Code ends here


# --------------
import requests

# Code starts here
url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response=requests.get(url)
df1=pd.read_html(response.content)[0]
df1=df1.loc[11:,:]
df1=df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
df1['United States of America'] = df1['United States of America'].str.replace(' ', '')



# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = dict(zip(df1['United States of America'], df1['US']))
df_final.insert(6,'abbr',df_final['state'])
df_final['abbr']=df_final['state'].map(mapping)


# Code ends here


# --------------
# Code stars here
df_final.abbr.loc[6]='MS'
df_final.abbr.loc[10]='TN'

# Code ends here


# --------------
# Code starts here
df_sub=df_final.groupby(['abbr'])['Jan','Feb','Mar','total'].sum()
formatted_df=df_sub.applymap(lambda x: "{}{}".format('$', x))
# Code ends here


# --------------
# Code starts here
sum_rows=df_sub.sum()
df_sub_sum=pd.DataFrame([sum_rows])
df_sub_sum=df_sub_sum.applymap(lambda x: "{}{}".format('$', x))
final_table=formatted_df.append(df_sub_sum)
print(final_table)



# Code ends here


# --------------
# Code starts here
df_sub['total']=df_sub['Jan']+df_sub['Feb']+df_sub['Mar']
df_sub['total'].plot(kind='pie')
# Code ends here


