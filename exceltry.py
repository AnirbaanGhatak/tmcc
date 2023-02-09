from openpyxl import *

wb = Workbook()

ws = wb.active

wb.save(filename = "try.xlsx")

# wb2 = load workbook('newhdfcDetails.xlsx')
# wb2.create sheet('sid1')
# wb2.save('newhdfcDetails.xlsx')

# CREATE TABLE ccsl ("Names" VARCHAR(255), "Best For" VARCHAR(255), "Joining Fee" VARCHAR(255), "Renewal Fee" VARCHAR(255), "Welcome Bonus" VARCHAR(255), "Reward Rates" VARCHAR(255), "travel" VARCHAR(255), "Domestic Lounge Access" VARCHAR(255), "Insurance Benefits" VARCHAR(255), "Movie & Dining" VARCHAR(255), "Reward redemption" VARCHAR(255), "Golf" VARCHAR(255), "International lounge access" VARCHAR(255), "Zero Liability Protection" VARCHAR(255), "Spend based waiver" VARCHAR(255), "Reward redemption fee" VARCHAR(255), "Foreign currency markup" VARCHAR(255), "Interest Rates" VARCHAR(255), "Fuel Surcharge" VARCHAR(255), "Cash advance charge" VARCHAR(255), "Add on card fee" VARCHAR(255), CCLimit VARCHAR(255));

    # CREATE TABLE cct ( "Names" VARCHAR(255) VARCHAR(255), "Best For" VARCHAR(255), "Joining Fee" VARCHAR(255)," Renewal Fee" VARCHAR(255), "Welcome Bonus" VARCHAR(255), Reward Rates VARCHAR(255), travel VARCHAR(255), Domestic Lounge Access VARCHAR(255), Insurance Benefits VARCHAR(255), Movie Dining VARCHAR(255), Reward redemption VARCHAR(255), Golf VARCHAR(255), International lounge access VARCHAR(255), Zero Liability Protection VARCHAR(255), Spend based waiver VARCHAR(255), Reward redemption fee VARCHAR(255), Foreign currency markup VARCHAR(255), Interest Rates VARCHAR(255), Fuel Surcharge VARCHAR(255), Cash advance charge VARCHAR(255), Add on card fee VARCHAR(255), Limit VARCHAR(255));
