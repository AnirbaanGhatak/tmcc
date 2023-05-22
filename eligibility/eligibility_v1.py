from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

driver = webdriver.Firefox()

# Navigate to the website you want to scrape
wait=WebDriverWait(driver,10)
driver.get("https://cardinsider.com/icici-bank/credit-card-eligibility-criteria-check/")
tables = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"table")))
print(len(tables))

# Create an empty dataframe
df = pd.DataFrame(columns=['Card', 'Age', 'Income'])

sleep(3)
for table in tables:
    sleep(3)
    # Find all table headers (th) in the table
    headers = table.find_element(By.XPATH,".//tr[1]")
    cells = headers.find_elements(By.XPATH,".//td")
    for i, cell in enumerate(cells):
        if 'cards' in cell.text.lower():
            rows = table.find_elements(By.XPATH,".//tr")
            print(f"Total Cards = {len(rows)}")
            for row in rows:
                cells = row.find_elements(By.XPATH,f".//td[{i+1}]")
                for cell in cells:
                    card = cell.text

        if 'age' in cell.text.lower():
            rows = table.find_elements(By.XPATH,".//tr")
            print(f"Total Cards = {len(rows)}")
            for row in rows:
                cells = row.find_elements(By.XPATH,f".//td[{i+1}]")
                for cell in cells:
                    age = cell.text

        if 'income' in cell.text.lower():
            rows = table.find_elements(By.XPATH,".//tr")
            print(f"Total Cards = {len(rows)}")
            for row in rows:
                cells = row.find_elements(By.XPATH,f".//td[{i+1}]")
                for cell in cells:
                    income = cell.text

sleep(3)
driver.quit()

# Export the dataframe to an Excel file
df.to_excel('output.xlsx', index=False)
