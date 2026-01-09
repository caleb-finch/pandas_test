import pandas as pd

df = pd.read_csv('test_database.csv',index_col=None)
df_as_a_list = df.values.tolist()
print(df)

for x in df_as_a_list:
    if x[0] == 2:
        oldList=x
        sum = x[0] + 7
        colA = x[0]
        colB = x[1]
        colC = x[2]
        print(colA)
        print(colB)
        print(colC)
        df=df.replace({'A': colA}, sum)
        print(df)
        df.to_csv('test_database.csv', sep=',', index=False)
    if x[0] == 9:
        oldList=x
        sum = x[0] - 7
        colA = x[0]
        colB = x[1]
        colC = x[2]
        print(colA)
        print(colB)
        print(colC)
        df=df.replace({'A': colA}, sum)
        print(df)
        df.to_csv('test_database.csv', sep=',', index=False)
