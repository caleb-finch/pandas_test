import pandas as pd

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
df_as_a_list = df.values.tolist()
print(df)

for x in df_as_a_list:
    print(x)
    if x[0] == 2:
        oldList=x
        sum = x[0] + 7
        colA = x[0]
        colB = x[1]
        colC = x[2]
        print(colB)
        print(colC)
print(colA)
df=df.replace({'A': colA}, sum)
print(df)

