import xlrd



def read_locators(file_path,sheet):
    workbook=xlrd.open_workbook(file_path)
    worksheet=workbook.sheet_by_name(sheet)
    rows=worksheet.get_rows()
    header= next(rows)
    for row in rows:
        d={row[0].value: (row[1].value,row[2].value)}
        return d

def read_test_data(file_path1,sheet):
    workbook=xlrd.open_workbook(file_path1)
    worksheet=workbook.sheet_by_name(sheet)
    rows=worksheet.get_rows()
    header= next(rows)

    data=[(row[0].value,row[1].value)for row in rows]
    return data





