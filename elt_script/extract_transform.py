import os
import pandas as pd
import numpy as np
def extractAndTransformData(file_path):
    dfs = {}
    print("Extracting and transforming data...")
    for csv in file_path:# loop through all the banks
        file_name = os.path.splitext(csv)[0]
        print(file_name)
        dfs[file_name] = pd.read_csv('/app/data/' + csv)
    # create identifier column for each bank 
    dfs['capital_one']['bank'] = 'capital one'
    dfs['BoA']['bank'] = 'bank of america'
    dfs['herbert']['bank'] = 'herbert'
    dfs['pnc']['bank'] = 'pnc'
    dfs['citi_bank']['bank'] = 'citi'

    # create tables: transactions, categories, and banks
    banks = {'bank_id':[1,2,3,4,5],'bank':['capital one','bank of america','herbert','pnc','citi']}
    transactions = pd.DataFrame()
    categories = pd.DataFrame()
    banks = pd.DataFrame(banks)

    for bank in dfs:
        ctg = dfs[bank]['Category'].unique() # get unique categories from each bank and add to categories table
        categories = pd.concat([categories, pd.DataFrame(ctg)])
        if bank != 'BoA': # Create identifier column for banking type
            dfs[bank]['banking_type'] = 'credit card'
        else:
            dfs[bank]['banking_type'] = 'debit card'
        transactions = pd.concat([transactions, dfs[bank]])

    #transform and normalize table
    categories.columns = ['category']
    categories.drop_duplicates(keep='first',inplace=True)
    categories['category_id'] = range(1, len(categories) + 1)
    categories = categories[['category_id','category']]

    transactions = transactions.merge(categories,how='left',left_on='Category',right_on='category').drop(columns='category')
    transactions = transactions.merge(banks, how='left', left_on='bank', right_on='bank')
    transactions.drop(columns=['bank','Category'],inplace=True)
    transactions['Date'] = pd.to_datetime(transactions['Date'])
    transactions['transaction_id'] = np.random.randint(1, 1000000, size=len(transactions))
    transactions.sort_values(by='Date',inplace=True)
    transactions.columns = transactions.columns.str.lower()
    transactions = transactions[
            ['transaction_id','date','description','amount','category_id','bank_id','banking_type']] 

    transactions.to_csv('./processed_data/transactions.csv',index= False)  #export to csv
    categories.to_csv('./processed_data/categories.csv',index= False)
    banks.to_csv('./processed_data/banks.csv',index= False)

    return print('sucessfully extracted and transformed data')

