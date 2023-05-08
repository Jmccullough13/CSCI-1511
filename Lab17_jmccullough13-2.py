# Plotting other language repos
# Jeffrey McCullough
# April 25, 2023,
# Collects most starred Java programs from GitHub API and displays in a graph, displaying creator name and url of project.

import requests
from plotly import offline
from plotly.graph_objs import Bar

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
repo_dict = repo_dicts[0]
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}</br>{description}"
    labels.append(label)
# Make a visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(0, 255, 0)',
        'line': {'width': 1.5, 'color': 'rgb(255, 0, 0)'}
    },
    'opacity': 0.5
}]
my_layout = {
    'title': 'Most Starred Java Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Repository', 'titlefont': {'size': 24}, 'tickfont': {'size': 16}},
    'yaxis': {'title': 'Stars', 'titlefont': {'size': 24}, 'tickfont': {'size': 16}}
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='java_repos.html')