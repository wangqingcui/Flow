import requests

url = 'https://api.tjise.edu.cn/usercenter/connect/token'  # 替换为你要请求的 URL
data = {
    "username": "15142424683",
    "password": "www15963",
    "grant_type": "password",
    "code_verifier": "",
    "client_id": "DDE1F5ACAF194674B13167269861FB7D"
}

# 发送 POST 请求
response = requests.post(url, data)
print(response)

if response.status_code == 200:
    print('请求成功！')
    response_data = response.json()  # 解析响应数据
    print(response_data)
else:
    print('请求失败，状态码：', response.status_code)
