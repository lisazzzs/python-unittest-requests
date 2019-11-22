# 这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应。
import requests
import json


class RunMain():

  def send_post(self,url,data):
    result = requests.post(url=url,data=data,verify=False).json()
    res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
    return res

  def send_get(self,url,data):
    result = requests.get(url=url, params=data,verify=False).json()
    res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
    return res

  def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
    result = None
    if method == 'post':
      result = self.send_post(url, data)
    elif method == 'get':
      result = self.send_get(url, data)
    else:
       print("method值错误！！！")
    return result


if __name__ == '__main__':
  result1 = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming','pwd':'111'})
  result2 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=111')
  print(result1)
  print(result2)
