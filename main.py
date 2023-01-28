from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import openpyxl as opx
# create a new Chrome browser instance

browser = webdriver.Chrome()

# navigate to the bank's website
browser.get("https://cardinsider.com/hdfc-bank/")

cctrial = browser.find_elements(By.CLASS_NAME, "title_list_link")
ccls = [xs.text for xs in cctrial]
print(ccls) 


# done by kadu i think so ----------------------------------
# extract the name and features of all credit cards``
# credit_cards = browser.find_elements(By.CSS_SELECTOR, ".h3, h3")
# for card in credit_cards:
    # print(card)
    # names = browser.find_elements(By.CSS_SELECTOR, ".h3, h3")
    # features = browser.find_elements(By.CSS_SELECTOR,".card-list .item-points")
    # name_list = [name.text for name in names]
    # feature_list = [feature.text for feature in features]
    # print(name_list)
#------------------------------------------------------------

# df = pd.DataFrame({"Names": name_list, "Features":feature_list})
df = pd.DataFrame({"Names": ccls})

with pd.ExcelWriter("newhdfc.xlsx", mode= 'a', engine= "openpyxl", if_sheet_exists='overlay') as writer1:
    df.to_excel(writer1, sheet_name='Sheet1', index=False)
    df.to_excel(writer1, sheet_name='Sheet2', index=False)
    df.to_excel(writer1, sheet_name='Sheet3', index=False)

# close the browser
browser.quit()




UrlName = pd.read_excel('newhdfc.xlsx', sheet_name="Sheet1")

# print(UrlName)
UrlName['Names'] = UrlName['Names'].str.split('Credit Card').str[0] + "Credit Card"
UrlName['Names'] = UrlName['Names'].str.lower()
UrlName['Names'] = UrlName['Names'].str.replace(" ",'-')
print(" and -\n" ,UrlName)
UrlName['Names'] = UrlName['Names'].str.replace("-–-",'-') #weird-ass case

print("--\n" ,UrlName)


for index in UrlName.index:
    # print("hello",index)
    # print(UrlName['Names'][index])

    browser = webdriver.Chrome()

    # navigate to the bank's website
    browser.get(f"https://cardinsider.com/hdfc-bank/{UrlName['Names'][index]}/")

    # extract the name and features of all credit cards
    credit_card_name = browser.find_elements(By.CSS_SELECTOR, ".title_list_link")
    for name in credit_card_name:
        credit_card_name = name.text
        print(name.text)
    print("-------------")
    category = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[1]/div/div[1]/div[2]/div/div[3]/p")
    for cat in category:
        category = cat.text
        print(cat.text)

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

    reward_redemption_fee = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/p[2]")
    for p in reward_redemption_fee:
        reward_redemption_fee= p.text
        print(p.text)

    foreign_currency_markup = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/p[2]")
    for p in foreign_currency_markup:
        foreign_currency_markup= p.text
        print(p.text)

    interest_rates = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[2]/div[3]/div/div[3]/p[2]")
    for p in interest_rates:
        interest_rates= p.text
        print(p.text)

    fuel_surcharge = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[2]/div[3]/div/div[4]/p[2]")
    for p in fuel_surcharge:
        fuel_surcharge= p.text
        print(p.text)

    cash_adv_charge = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[2]/div[3]/div/div[5]/p[2]")
    for p in cash_adv_charge:
        cash_adv_charge= p.text
        print(p.text)

    add_on_card_fee = browser.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div/div[2]/div[3]/div/div[6]/p[2]")
    for p in add_on_card_fee:
        add_on_card_fee= p.text
        print(p.text)


    df = pd.DataFrame({"Name": [credit_card_name], "Category":[category],"Joining Fee":[join_fee],"Renewal Fee":[renewal_fee],"Welcome Bonus":[welcome_bonus],"Reward Rates":[rew_rates],
    "travel":[travel],"Domestic Lounge Access":[domestic_lounge_access],"Insurance Benefits":[insurance_benefits],"Movie & Dining":[movie_and_dining],"Reward redemption":[reward_redemption],"Golf":[golf],"International lounge access":[international_lounge_access],
    "Zero Liability Protection":[zero_liability_protection],"Spend based waiver":[spend_baised_waiver],"Reward redemption fee":[reward_redemption_fee],"Foreign currency markup":[foreign_currency_markup],"Interest Rates":[interest_rates],"Fuel Surcharge":[fuel_surcharge],
    "Cash advance charge":[cash_adv_charge],"Add on card fee":[add_on_card_fee],
    })

    # def get_maximum_rows(*, sheet_object):
    #     rows = 0
    #     for max_row, row in enumerate(sheet_object, 1):
    #         if not all(col.value is None for col in row):
    #             rows += 1
    #     return rows

    # workbook = opx.load_workbook('hdfcCCName.xlsx')
    # sheet_object = workbook.active
    # max_rows = get_maximum_rows(sheet_object=sheet_object)

    # print(max_rows)

    print(df)


    with pd.ExcelWriter("newhdfc.xlsx", mode= 'a', engine= "openpyxl", if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name= "Sheet2", startrow= index+1)
        df.to_excel(writer, sheet_name= "Sheet3", startrow= index+1, index= False)
        df.to_excel(writer, sheet_name= "Sheet4", startrow= index+1, index= False, header= False)



    # df.to_excel(, sheet_name = f"{UrlName['Names'][index]}.xlsx", index= False)

    # close the browser
    browser.quit()
