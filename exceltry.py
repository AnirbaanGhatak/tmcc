from openpyxl import load_workbook

wb2 = load_workbook('newhdfcDetails.xlsx')
wb2.create_sheet('sid1')
wb2.save('newhdfcDetails.xlsx')