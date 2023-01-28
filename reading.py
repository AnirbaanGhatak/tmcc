import pandas as pd
import openpyxl as opx

# dataframe1 = pd.read_excel('hdfc.xlsx')
# print(dataframe1)
# dataframe1['Names'] = dataframe1['Names'].str.split('Credit Card').str[0] + "Credit Card"
# print(dataframe1)

    # df.to_excel("hdfcCCNames.xlsx",  f"{UrlName['Names'][index]}.xlsx", index=True)

def get_maximum_rows(*, sheet_object):
    rows = 0
    for max_row, row in enumerate(sheet_object, 1):
        if not all(col.value is None for col in row):
            rows += 1
    return rows

workbook = opx.load_workbook('hdfcCCNames.xlsx')
sheet_object = workbook.active
max_rows = get_maximum_rows(sheet_object=sheet_object)

print(max_rows)