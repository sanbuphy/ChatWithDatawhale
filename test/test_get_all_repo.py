import requests

# 组织的名称
org_name = 'datawhalechina'
token = ''

# GitHub API URL模板
url = f'https://api.github.com/orgs/{org_name}/repos'

# 设置请求头
headers = {
    'Authorization': token,
}

response = requests.get(url, headers=headers,params={'per_page':200,"page":0})
if response.status_code == 200:
    # 解析响应内容为JSON
    repos = response.json()
    if len(repos) !=0:
        for repo in repos:
            print(repo['name'])
else:
    print(f"Error: Unable to fetch repos (Status code: {response.status_code})")