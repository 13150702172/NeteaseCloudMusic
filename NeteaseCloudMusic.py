import json
import requests

class NeteaseCloudMusic:

    #配置文件
    def config(self,headers,url,params):
        self.headers = headers
        self.url = url
        self.params = params

    #执行请求操作
    def request(self):
        result = requests.post(self.url,headers=self.headers,params=self.params)
        return json.loads(result.text)
