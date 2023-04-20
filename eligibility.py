from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import openpyxl as opx
from openpyxl import *
from time import sleep
import requests
# create a new Chrome browser instance


browser = webdriver.Firefox()


# navigate to the bank's website

banks = ['icici-bank']
for bankName in banks:
    browser.get(f"https://cardinsider.com/{bankName}")
    cctrial = browser.find_elements(By.CLASS_NAME, "title_list_link")
    ccls = [xs.text for xs in cctrial]
    print(ccls)

    df = pd.DataFrame(columns=['Name', "Particular", "Eligibility"])

    # close the browser
    browser.quit()

    firstCCName = ccls[0]

    for x in range(len(ccls)):
        # sfx = ccls[x].find("Card")+4
        # ccls[x] = ccls[x][:sfx]
        ccls[x] = ccls[x].replace(" ", '-')
        ccls[x] = ccls[x].replace("-–-", '-')
        ccls[x] = ccls[x].replace("’", "")
        ccls[x] = ccls[x].lower()

        print(f"New Name: {ccls[x]}")

    print(ccls)

    for ccname in ccls:
        print(ccname)
        # print("hello",index)
        # print(UrlName['Names'][index])

        browser = webdriver.Firefox()

        # navigate to the bank's website

        ccurl = f"https://cardinsider.com/{bankName}/{ccname}/"

        # print(f"hello: {ccurl}")

        if requests.get(ccurl, headers={'User-Agent': 'Mozilla/5.0'}).status_code == 200:
            browser.get(f"{ccurl}")
        else:
            cn = ccname
            print(f'cn: {cn}')
            sfx = cn.find("card")+4
            cn = cn[:sfx]
            print(f'cn2: {cn}')

            if requests.get(f"https://cardinsider.com/{bankName}/{cn}/", headers={'User-Agent': 'Mozilla/5.0'}).status_code == 200:
                browser.get(f"https://cardinsider.com/{bankName}/{cn}/")
            else:
                nccn = cn.replace("-bank", "")
                browser.get(f"https://cardinsider.com/{bankName}/{nccn}/")

        # this is from main2.py---------------------------------------

        # extract the name and features of all credit cards

        credit_card_name = browser.find_elements(
            By.CSS_SELECTOR, ".title_list_link")
        for name in credit_card_name:
            credit_card_name = name.text
            print(name.text)

        print("-------------")

        etr = []
        vrt = []

        try:
            prd = browser.find_element(By.ID, 'wpdtSimpleTable-1052')
            prc = prd.find_elements(By.TAG_NAME, "tr")
            for p in prc:
                z = p.find_elements(By.TAG_NAME, "td")

                for y in range(len(z)):
                    if (y % 2 == 0):
                        etr.append(z[y].text)
                    
                    else:
                        vrt.append(z[y].text)
        except Exception as e:
            print(e)
            print("no product details")

        df = df.append({"Name": credit_card_name,  "Particular": etr, "Eligibility": vrt}, ignore_index=True)
        # close the browser
        browser.quit()


df.to_csv("All_CC_Details4.csv", index=False)

sleep(10.0)
