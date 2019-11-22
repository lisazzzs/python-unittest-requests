# 读取Excel的方法
import os
import getpathInfo

from xlrd import open_workbook

path = getpathInfo.get_Path()

class readExcel():
  def get_xls(self,xls_name,sheet_name):
    cls = []

    xlsPath = os.path.join(path,'case',xls_name)
    file = open_workbook(xlsPath,'rb')
    sheet = file.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
      if sheet.row_values(i)[0] != u'case_name':
        cls.append(sheet.row_values(i))
    return cls

if __name__ == '__main__':
  print(readExcel().get_xls('userCase.xlsx', 'login'))
  print(readExcel().get_xls('userCase.xlsx', 'login')[0][1])
  print(readExcel().get_xls('userCase.xlsx', 'login')[1][2])

