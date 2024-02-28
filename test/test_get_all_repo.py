import json
import requests
import os
import base64
import loguru
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 从环境变量中获取TOKEN
TOKEN = os.getenv('TOKEN')


# 定义获取组织仓库的函数
def get_repos(org_name, token):
    headers = {
        'Authorization': f'token {token}',
    }
    url = f'https://api.github.com/orgs/{org_name}/repos'
    response = requests.get(url, headers=headers, params={'per_page': 200, 'page': 0})
    if response.status_code == 200:
        repos = response.json()
        loguru.logger.info(f'Fetched {len(repos)} repositories for {org_name}.')
        # 保存仓库名到文本文件
        with open('repositories.txt', 'w', encoding='utf-8') as file:
            for repo in repos:
                file.write(repo['name'] + '\n')
        return repos
    else:
        loguru.logger.error(f"Error fetching repositories: {response.status_code}")
        loguru.logger.error(response.text)
        return []


# 定义拉取仓库README文件的函数
def fetch_repo_readme(org_name, repo_name, token):
    headers = {
        'Authorization': f'token {token}',
    }
    url = f'https://api.github.com/repos/{org_name}/{repo_name}/readme'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        readme_content = response.json()['content']
        # 解码base64内容
        readme_content = base64.b64decode(readme_content).decode('utf-8')
        # 保存README到文件
        temp_dir = 'temp'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        repo_dir = os.path.join(temp_dir, repo_name)
        if not os.path.exists(repo_dir):
            os.makedirs(repo_dir)
        with open(os.path.join(repo_dir, 'README.md'), 'w', encoding='utf-8') as file:
            file.write(readme_content)
    else:
        loguru.logger.error(f"Error fetching README for {repo_name}: {response.status_code}")
        loguru.logger.error(response.text)


# 主函数
if __name__ == '__main__':
    # 配置组织名称
    org_name = 'datawhalechina'

    # 获取仓库列表
    repos = get_repos(org_name, TOKEN)

    # 打印仓库名称
    if repos:
        for repo in repos:
            repo_name = repo['name']
            # 拉取每个仓库的README
            fetch_repo_readme(org_name, repo_name, TOKEN)
    # 清理临时文件夹
    # if os.path.exists('temp'):
    #     shutil.rmtree('temp')
