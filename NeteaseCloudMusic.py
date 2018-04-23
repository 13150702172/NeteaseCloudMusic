import json
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class NeteaseCloudMusic:

    #配置文件
    def __init__(self,headers,url,params):
        self.headers = headers
        self.url = url
        self.params = params

    #执行请求操作
    def request(self):
        res = requests.post(self.url,headers=self.headers,params=self.params)

        if res.status_code == 200:
            result = json.loads(res.text)

            # 创建热门评论对象，存储到集合中
            hotComments = []

            for res in result['hotComments']:
                info = {
                    "nickName": res["user"]["nickname"],
                    "commentsCount": res["likedCount"],
                    "content": res["content"]
                }
                hotComments.append(info)

            # 绘图
            nickname = []
            count = []
            content = []

            for item in hotComments:
                nickname.append(item['nickName'])
                count.append(item['commentsCount'])
                content.append(item['content'])

            plt.rcParams.update({'figure.autolayout': True})

            plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

            fig, ax = plt.subplots()
            ax.barh(nickname, count)
            labels = ax.get_xticklabels()
            plt.setp(labels, rotation=45, horizontalalignment='right')
            ax.set(xlabel='点赞数量', ylabel='昵称', title='网易云音乐-成都 热评统计')

            # wordcloud词云
            content_text = " ".join(content)
            wordcloud = WordCloud("C:\Windows\Fonts\simfang.ttf").generate(content_text)
            plt.figure()
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.show()

        else:
            raise ValueError("请求失败，状态码："+res.status_code)

    #绘图

