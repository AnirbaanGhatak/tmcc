import pandas as pd

cdm = pd.read_excel('cc_kuch_toh.xlsx', sheet_name='Sheet3')
# print(cdm)

cdt = pd.read_excel('cc_kuch_toh.xlsx', sheet_name='Sheet1')
# print(cdt)

# cdt.to_json()

cdm.to_json(r'C:\Users\Anirbaan\OneDrive\Desktop\LearnSelenium\kuch_toh.json')

print(cdm.to_json())




variants=cdt['Variant'].values.tolist()

print("Cards are: ")

for a in variants:
    print(a)

x = int(input("Select Cards:"))

x = x-1

print(cdt['Variant'][x])
