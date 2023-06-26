import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)

response_dict = r.json()
print('Total Repos: ', response_dict['total_count'])

repo_dicts = response_dict['items']

name, plot_dicts = [], []
for repo_dict in repo_dicts:
    name.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False, show_y_guides=False, truncate_label=15)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = name

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# repos_dict = r.json()
# # 获取项目名称
# item_name = []
# for item in repos_dict['items']:
#     item_name.append(item['full_name'])
# print(item_name)
#
# repo_dicts = repos_dict['items']
# repo_dic = repo_dicts[1]
# print('Owner: ', repo_dic['owner']['login'])
# print(len(repo_dic))
#
# print(repos_dict.keys())