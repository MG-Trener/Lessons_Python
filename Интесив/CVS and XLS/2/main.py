from openpyxl import load_workbook

wb = load_workbook('students.xlsx')
ws = wb.active
print(ws)