from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#ws.delete_rows(8) # 8번째의 7번 학생 삭제
#ws.delete_rows(8, 3) #7번부터 3명 삭제
#ws.delete_cols(2) #영어 점수 삭제  삭제.
ws.delete_cols(2,2) #2열부터 2줄 삭제
wb.save("sample_delete_rows.xlsx")