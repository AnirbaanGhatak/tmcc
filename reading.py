import pandas as pd

dataframe1 = pd.read_excel('hdfc.xlsx')
print(dataframe1)
dataframe1['Names'] = dataframe1['Names'].str.split('Credit Card').str[0] + "Credit Card"
print(dataframe1)

    # df.to_excel("hdfcCCNames.xlsx",  f"{UrlName['Names'][index]}.xlsx", index=True)
