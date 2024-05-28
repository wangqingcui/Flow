import requests

url = 'https://api.vvhan.com/api/text/joke?type=json'  # 替换为你要请求的 URL

# 发送 GET 请求
response = requests.get(url)
print(reponse)
if response.status_code == 200:
    print('请求成功！')
    data = response.json()  # 解析响应数据
    print(data)
else:
    print('请求失败，状态码：', response.status_code)
