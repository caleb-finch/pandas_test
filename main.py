##test the pandas import and see if i can import a csv, get the list, change the contents of the list, and save the csv

import pandas as pd

def main():
  df = pd.read_csv('database.csv',index_col=None)
  df_as_a_list = df.values.tolist()
  print(df)

  for x in df_as_a_list:
    if x[0] == 'cfinch':
      username = x[0]
      savingsAmnt = x[1]
      checkingAmnt = x[2]
      print(checkingAmnt)
      transsavingsAmnt = x[1] + 69
      transcheckingAmnt = x[2] + 420
      print(transcheckingAmnt)
      break
  df=df.replace({'savingsAmnt': savingsAmnt}, transsavingsAmnt)
  df=df.replace({'checkingAmnt': checkingAmnt}, transcheckingAmnt)
  print(df)
  df.to_csv('database.csv', sep=',', index=False)

main()
