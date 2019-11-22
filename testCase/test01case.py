#读取userCase.xlsx中的用例，使用unittest来进行断言校验
import sys,os
sys.path.append('D:\python\myj\common')
sys.path.append('D:\python\myj\\testFile')
# print(sys.path)
import json
import unittest
from  configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel


url = geturlParams.geturlParams().get_Url()
login_xls = readExcel.readExcel().get_xls('userCase.xlsx','login')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
  def setParameters(self,case_name,path,query,method):
    """

    set params
    :param case_name:
    :param path
    :param query
    :param method
    :return:
    """

    self.case_name = str(case_name)
    self.path = str(path)
    self.query = str(query)
    self.method = str(method)

  def description(self):
    """

    test report description
    :return:
    """

    self.case_name

  def setUp(self):
    """

    :return:
    """

    print(self.case_name+"测试开始前准备")

  def test01case(self):
    self.checkResult()

  def tearDown(self):
    print("测试结束，输出log完结\n\n")

  def checkResult(self):
    """
    check test result
    :return:
    """

    url1 = "http://www.xxx.com/login?"
    new_url = url1 + self.query
    data1 = dict(urllib.parse.parse_qs(urllib.parse.urlsplit(new_url).query))
    info = RunMain().run_main(self.method,url,data1)
    ss = json.loads(info)
    if self.case_name == 'login':
      self.assertEqual(ss['code'],200)
    if self.case_name == 'login_error':
      self.assertEqual(['code'],-1)
    if self.case_name == 'login_null':
      self.assertEqual(ss['code'],10001)