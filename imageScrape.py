from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

browser = webdriver.Firefox()

banks = ['hdfc-bank', 'sbi-card', 'yes-bank', 'idfc-first-bank', 'au-small-finance-bank', 'indusind-bank', 'axis-bank', 'kotak', 'icici-bank']# banks=['sbi-card','yes-bank']
for bankName in banks:
    browser.get(f"https://cardinsider.com/{bankName}")
    cctrial = browser.find_elements(By.CLASS_NAME, "title_list_link")
    ccls = [xs.text for xs in cctrial]
    print(ccls) 

    for x in range(len(ccls)):
        ccls[x] = ccls[x].replace(" ",'-')
        ccls[x] = ccls[x].replace("-–-",'-')
        ccls[x] = ccls[x].replace("’", "")
        ccls[x] = ccls[x].lower()

        print(f"New Name: {ccls[x]}")

    print(ccls)

    for ccname in ccls:
        print(ccname)

        browser = webdriver.Firefox()

        ccurl = f"https://cardinsider.com/{bankName}/{ccname}/"

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
                nccn = cn.replace("-bank","")
                browser.get(f"https://cardinsider.com/{bankName}/{nccn}/")

        credit_card_name = browser.find_elements(By.CSS_SELECTOR, ".title_list_link")
        for name in credit_card_name:
            credit_card_name = name.text
            print(name.text)

        image = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[1]/div/div[1]/div[1]/img")
        for img in image:
            image = img.get_attribute("src")
            response = requests.get(image)
            with open(credit_card_name + ".png","wb") as f:
                f.write(response.content)