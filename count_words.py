
import pandas as pd
df= pd.read_csv('movies.csv')
df['count_word'] = df['title'].apply(lambda x: x.split('(')[0].strip()).apply(lambda x: len(x.split(' ')))
df['title'] = df['title'].apply(lambda x: x.split('(')[0].strip()).apply(lambda x: x.split(' '))
res_df = pd.DataFrame()
for x in range(1, df['count_word'].max()):
    tmp = df[df['count_word'] == x]
    for i in range(x):
        res_df = res_df.append(pd.DataFrame({ 'word' : tmp['title'].apply(lambda x: x[i])}))
result = res_df['word'].value_counts().reset_index()['index'].values[0]
print(result)
