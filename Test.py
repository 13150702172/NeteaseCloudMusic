from NeteaseCloud.NeteaseCloudMusic import NeteaseCloudMusic
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#配置文件
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Referer':'http://music.163.com/song?id=551816010',
    'Origin':'http://music.163.com',
    'Host':'music.163.com'
}

params = {
"params":"hDETJVGZZoK83juBufkImQVkKOZd0I1FqO498zsMp/+tjJUo797rTCjAzLJocRvXn3jrKE0vwX7DCORiuNk4Xj3D8EZlUMJkZgQ5QRl3wU4VFlXQvvhUBnSBve4WjXhk5j75i05ysXb2piaozm9ryN1QYLk/FE9xvkv7XpdVbWFzcxI0Vuu876Pp8oPhUWeu",
"encSecKey":"31b685c9033e6c039698cfde2f2c79bc3f19071bc5eda8eb4af5c4a7e218c46b4d071ef0fb39e648322c316c86fd6f0e01d2cf57579746a1d41704ab8260020303cb4c1afaef76f514edbf3db5b81d189cdcdbc49529df26d7eca087441d6523ede954d818343d7631a77624bbeced13fac0cf27ce51b6c31e4085ad50545bb6"
}

url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_436514312?csrf_token='

#调用请求逻辑
neteaseCloudMusic = NeteaseCloudMusic()

neteaseCloudMusic.config(headers,url,params)

result = neteaseCloudMusic.request()

#创建热门评论对象，存储到集合中
hotComments = []

for res in result['hotComments']:
    info = {
        "nickName":res["user"]["nickname"],
        "commentsCount":res["likedCount"],
        "content":res["content"]
    }
    hotComments.append(info)

#绘图
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
ax.set( xlabel='点赞数量', ylabel='昵称',title='网易云音乐-成都 热评统计')

#wordcloud词云
content_text = " ".join(content)
wordcloud = WordCloud("C:\Windows\Fonts\simfang.ttf").generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()








