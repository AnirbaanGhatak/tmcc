from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# create a new Chrome browser instance
browser = webdriver.Chrome()

# navigate to the bank's website
browser.get("https://cardinsider.com/hdfc-bank/hdfc-bank-infinia-credit-card/")

# extract the name and features of all credit cards
credit_card_name = browser.find_elements(By.CSS_SELECTOR, ".title_list_link")
for name in credit_card_name:
    credit_card_name = name.text
    print(name.text)
print("-------------")
category = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[1]/div/div[1]/div[2]/div/div[3]/p")
for p in category:
    category = p.text
    print(p.text)

join_fee = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[1]/div/div[1]/div[2]/div/div[4]/p") #same as renewal fee
for p in join_fee:
    join_fee = p.text
    print(p.text)

renewal_fee = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[1]/div/div[1]/div[2]/div/div[4]/p") 
for p in renewal_fee:
    renewal_fee = p.text
    print(p.text)

welcome_bonus = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[2]/div[1]/p[2]")
for p in welcome_bonus:
    welcome_bonus = p.text
    print(p.text)

rew_rates = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/p[2]")
for p in rew_rates:
    rew_rates = p.text
    print(p.text)

travel = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[3]/p[2]")
for p in travel:
    travel= p.text
    print(p.text)

domestic_lounge_access = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[5]/p[2]")
for p in domestic_lounge_access:
    domestic_lounge_access= p.text
    print(p.text)


insurance_benefits = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[7]/p[2]")
for p in insurance_benefits:
    insurance_benefits= p.text
    print(p.text)

movie_and_dining = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[2]/div[2]/p[2]")
for p in movie_and_dining:
    movie_and_dining= p.text
    print(p.text)

reward_redemption = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[2]/p[2]")
for p in reward_redemption:
    reward_redemption= p.text
    print(p.text)

golf = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[4]/p[2]")
for p in golf:
    golf= p.text
    print(p.text)

international_lounge_access = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[6]/p[2]")
for p in international_lounge_access:
    international_lounge_access= p.text
    print(p.text)

zero_liability_protection = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[1]/div[3]/div/div[8]/p[2]")
for p in zero_liability_protection:
    zero_liability_protection= p.text
    print(p.text)

spend_baised_waiver = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[2]/div[2]/div[3]/p[2]")
for p in spend_baised_waiver:
    spend_baised_waiver= p.text
    print(p.text)