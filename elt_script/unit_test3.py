import os
import pandas as pd
import numpy as np
files = os.listdir('./elt_script/data')
dfs = {}
print("Extracting and transforming data...")
for csv in files:# loop through all the banks
    file_name = os.path.splitext(csv)[0]
    print(file_name)
    dfs[file_name] = pd.read_csv('./elt_script/data/' + csv)
# create identifier column for each bank 
dfs['capital_one']['bank'] = 'capital one'
dfs['BoA']['bank'] = 'bank of america'
dfs['herbert']['bank'] = 'herbert'
dfs['pnc']['bank'] = 'pnc'
dfs['citi_bank']['bank'] = 'citi'

transaction = pd.concat([dfs['capital_one'],dfs['BoA'],dfs['herbert'],dfs['pnc'],dfs['citi_bank']])
transaction = transaction.merge(dfs['dates'],how='left',left_on='Date',right_on='full_date')
transaction = transaction.merge(dfs['bank'],how='left',on='bank')
transaction['payment_method'] = np.where(
    (transaction['bank'] == 'BoA') | (transaction['bank'] == 'herbert'),
    'debit card',
    'credit card'
)
transaction = transaction.merge(dfs['payment_method'],how='left', on='payment_method')
transaction['id'] = range(1, len(transaction) + 1)

transaction.sort_values(by='Date',inplace=True)
transaction = transaction[
    ['id','date_id','bank_id','payment_method_id','Description','Category','Amount','Payment Modality']
    ] 
transaction.columns = transaction.columns.str.lower()

transaction.to_csv('./processed_data/transactions.csv',index= False)  #export to csv