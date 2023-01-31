from openpyxl import *

wb = Workbook()

ws = wb.active

wb.save(filename = "try.xlsx")

# wb2 = load_workbook('newhdfcDetails.xlsx')
# wb2.create_sheet('sid1')
# wb2.save('newhdfcDetails.xlsx')

# "Name", "Best For", "Joining Fee", "Renewal Fee", "Welcome Bonus", "Reward Rates", "travel", "Domestic Lounge Access", "Insurance Benefits", "Movie & Dining", "Reward redemption", "Golf", "International lounge access", "Zero Liability Protection", "Spend based waiver", "Reward redemption fee", "Foreign currency markup", "Interest Rates", "Fuel Surcharge", "Cash advance charge"	"Add on card fee"
