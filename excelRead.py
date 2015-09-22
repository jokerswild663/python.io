import pandas

def test():
  pd.show_versions(as_json=False)

def readExcelFile(filepath,sprint):
  excelObject=pandas.ExcelFile(filepath)
  codeList=excelObject.parse(sheetname=sprint, header=14,parse_cols='O')
  print(codeList.values.flatten())
#  print(excelObject.sheet_names)
#  print(excelObject)
  
