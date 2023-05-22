from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

def bank_eligibility(bank,cards,ages,incomes):
    driver = webdriver.Firefox()

    # Navigate to the website you want to scrape
    wait=WebDriverWait(driver,10)
    driver.get(f"https://cardinsider.com/{bank}/credit-card-eligibility-criteria-check/")
    tables = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"table")))
    print(len(tables))
    sleep(3)
    for table in tables:
        sleep(3)
        # Find all table headers (th) in the table
        headers = table.find_element(By.XPATH,".//tr[1]")
        cells = headers.find_elements(By.XPATH,".//td")
        for i, cell in enumerate(cells):
            if 'credit card' in cell.text.lower():
                rows = table.find_elements(By.XPATH,".//tr")
                print(f"Total Cards = {len(rows)}")
                for row in rows:
                    cells = row.find_elements(By.XPATH,f".//td[{i+1}]")
                    for cell in cells:
                        print(cell.text)
                        cards.append(cell.text)

            if 'age' in cell.text.lower():
                rows = table.find_elements(By.XPATH,".//tr")
                print(f"Total Cards = {len(rows)}")
                for row in rows:
                    cells = row.find_elements(By.XPATH,f".//td[{i+1}]")
                    for cell in cells:
                        print(cell.text)
                        ages.append(cell.text)

            if 'income' in cell.text.lower():
                rows = table.find_elements(By.XPATH,".//tr")
                print(f"Total Cards = {len(rows)}")
                for row in rows:
                    cells = row.find_elements(By.XPATH,f".//td[{i+1}]")
                    for cell in cells:
                        print(cell.text)
                        incomes.append(cell.text)

        cc = pd.DataFrame({"1": cards})
        age = pd.DataFrame({"2": ages})
        inc = pd.DataFrame({"3": incomes})
        

    # data={'0':cards,'1':ages,'2':incomes}
    data = [cc, age, inc]
    sleep(3)
    driver.quit()
    return data
    # df.to_excel("output.xlsx",index=False)
