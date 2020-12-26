from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#ws.insert_rows(8) #8 번째 줄 비움
#ws.insert_rows(8,5) # 8에 5줄 추가
ws.insert_cols(2) #2 열 비우기
#ws.insert_cols(2,5) #2 열로부터 5칸 비우기.

wb.save("sample_insert_cols.xlsx")