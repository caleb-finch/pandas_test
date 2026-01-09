##test the pandas import and see if i can import a csv, get the list, change the contents of the list, and save the csv

import pandas as pd

def main():
  df = pd.read_csv('database.csv')
  df_as_a_list = df.values.tolist()
  for x in df_as_a_list:
    print(x[0])
    if x[0] == 'ljames':
       username = x[0]
       break
  fullList = x
  print(fullList)
  print(username)
      

    
    #print(df_as_a_list(x))

  #print(df)
  #print(df.loc[:, 'username'])
  #usernameList = df.loc[:, 'username']
  #print(usernameList)
  #for x in df.loc[:, 'username']:
  #  if x=='ljames':
  #    print('true! Username is {x}')



  #print(df.shape)
  #[x,y] = df.shape
  #print(x)
  #print(y)

main()
