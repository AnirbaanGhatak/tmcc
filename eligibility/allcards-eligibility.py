from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from try_eligibility import bank_eligibility
import pandas as pd
# create a new Chrome browser instance

driver=webdriver.Chrome()
driver.maximize_window()
#indusind,au,idfc,icici,yesbank,hdfc,sbi,standardchartered,axis,kotak
banks_list=['indusind-bank','idfc-first-bank','icici-bank','yes-bank','hdfc-bank','sbi-card','standard-chartered','axis-bank','kotak']

df = pd.DataFrame()
eww = pd.DataFrame()
cards,ages,incomes=[],[],[]
for bank in banks_list:
    data=bank_eligibility(bank,cards,ages,incomes)
    print(f"For {bank}\n{data}\n")

    eww = pd.concat([data[0],data[1], data[2]], axis=1)

    df = pd.concat([df, eww], axis=0)
    # cards += data['0']
    # ages += data['1']
    # incomes += data['2']
    

# Combine the scraped data into a pandas DataFrame
# df = pd.DataFrame({'Credit Cards': cards, 'Age': ages, 'Income/Salary': incomes})

# Write the DataFrame to an excel file
df.to_excel('bank_data.xlsx', index=False)
