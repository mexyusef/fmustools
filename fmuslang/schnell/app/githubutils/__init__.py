# https://pygithub.readthedocs.io/en/latest/reference.html
# https://pygithub.readthedocs.io/en/latest/examples.html
# https://pygithub.readthedocs.io/en/latest/introduction.html
# https://github.com/PyGithub/PyGithub

# pip install PyGithub
# pip install gitpython PyGithub
import os
import re
import requests
import keyboard
import pyperclip

import git
from github import Github
# pip install jq
from jq import jq
# import jq

from schnell.app.envvalues import github_token


current_working_token = github_token()
github = Github(current_working_token)
user = github.get_user()
github_prefix_url = 'https://github.com/'


def get_issues(github_repo='django/django', labels=[]):

    if github_repo.startswith(github_prefix_url):
        github_repo = github_repo.removeprefix(github_prefix_url)

    r = github.get_repo(github_repo)
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.get_issues
    if labels:
        result = r.get_issues(state='open', sort='created', labels=labels)
    else:
        result = r.get_issues(state='open', sort='created') # jadi ngawur urutan, apa karena sort='created'? cek di ipynb
    # result = [f"[{i.number}] {i.title}" for i in issues]
    # result = reversed(issues) # TypeError: object of type 'PaginatedList' has no len()
    # result = issues[::-1]
    return result


def print_issues(issues):
    # issues = get_issues(repo)
    daftar = [f'[{item.number}] {item.title}' for item in issues]
    for d in daftar:
        print(d)


def print_repo_issues(repo, labels=['good first issue']):
    issues = get_issues(repo, labels)
    print_issues(issues)


def get_issue_bynumber(issue_num, github_repo='django/django'):
    if github_repo.startswith(github_prefix_url):
        github_repo = github_repo.removeprefix(github_prefix_url)

    r = github.get_repo(github_repo)
    issue = r.get_issue(issue_num)
    return issue


def get_pullrequests(github_repo='django/django'):

    if github_repo.startswith(github_prefix_url):
        github_repo = github_repo.removeprefix(github_prefix_url)

    r = github.get_repo(github_repo)
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.get_issues
    result = r.get_pulls(state='open', sort='created') # base='master', base='main'
    # prs = r.get_pulls(state='open') # jadi ngawur urutan
    # result = [f"[{i.number}] {i.title}" for i in prs]
    # result = reversed(prs) # TypeError: object of type 'PaginatedList' has no len()
    # result = prs[::-1]
    return result


def get_pr_bynumber(pr_num, github_repo='django/django'):
    if github_repo.startswith(github_prefix_url):
        github_repo = github_repo.removeprefix(github_prefix_url)

    r = github.get_repo(github_repo)
    pr = r.get_pull(pr_num)
    return pr


def create_repo(name='hapus1', description='ini contoh untuk dihapus saja', private=True):
    """
    create by org:
    https://stackoverflow.com/questions/28675121/how-to-create-a-new-repository-with-pygithub
    """
    repo = user.create_repo(name=name, description=description, private=private)
    return repo


def delete_repo(repo_name):
    """
    https://stackoverflow.com/questions/64384089/can-you-delete-a-repo-via-pygithub
    """
    repo = user.get_repo(repo_name)
    repo.delete()


def edit_repo():
    pass


def list_repo():
    """
    https://stackoverflow.com/questions/59861312/how-to-get-the-list-of-source-repositories-of-a-user-organisation-on-github
    """
    repos = user.get_repos()
    non_forks = []
    for repo in user.get_repos():
        if repo.fork is False:
            non_forks.append(repo.name)
    return repos


def detail_repo():
    pass


def user_repos(username):
    user = github.get_user(username) # target user
    counter = 1
    # https://docs.github.com/en/rest/repos/repos#list-public-repositories
    for repo in user.get_repos(sort='updated', direction='desc', per_page=100, page=1):
        if repo.fork is False:
            # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
            print(f"""{counter}.
            name = {repo.name}
            full name = {repo.full_name}
            description = {repo.description}
            git_url = {repo.git_url}
            clone_url = {repo.clone_url}
            master_branch = {repo.master_branch}
            updated_at = {repo.updated_at}
            """)
            counter += 1


def repo_get_subfolder_content(repo_name, folder_name):
    """
    https://stackoverflow.com/questions/53527783/pygithub-how-to-get-contents-of-the-subfolder-in-the-repo
    """
    repo = github.get_repo(repo_name)
    result = []
    contents = repo.get_contents(folder_name)
    akhir = 0
    while len(contents)>akhir:
        file_content = contents.pop(0)
        if file_content.type == 'dir':
            new_contents = repo.get_contents(file_content.path)
            contents.extend(new_contents)
        else:
            result.append(file_content)
    return result


def create_user():
    pass


def delete_user():
    pass


def edit_user():
    pass


def list_user():
    pass


def detail_user():
    pass


def create_gist(content, new_name='coba1', description='first gist', private=True):
    fcontent = github.InputFileContent(content=content, new_name=new_name)
    gist = user.create_gist(public=not private, files={f'{new_name}.txt':fcontent}, description=description)
    # Gist(id="42995bed447e0f922103d9422042d4ed")
    return gist


def search_by_lang(language='python', jumlah=10, warna=True):
    """
    """
    from .printutils import print_list_warna
    repositories = github.search_repositories(query=f'language:{language}') [:jumlah]
    if warna:
        print_list_warna(repositories)
    else:
        for i,item in enumerate(repositories):
            print(f"{i}. {item}")


def good_first_issues(jumlah=10, warna=True):
    """
    DANGER: jangan sampai kebanyakan, rate limited utk tiap token
    https://pygithub.readthedocs.io/en/latest/examples/MainClass.html#get-current-user
    https://github.com/topics/good-first-issue
    https://dev.to/ohbarye/how-to-find-good-first-issues-to-contribute-oss-jl7
    """
    from .printutils import print_list_warna
    repositories = github.search_repositories(query='good-first-issues:>3') [:jumlah]
    if warna:
        print_list_warna(repositories)
    else:
        for i,item in enumerate(repositories):
            print(f"{i}. {item}")


def search_github_repos(keyword, sort_by_star=False, github_token_arg=current_working_token):
    url = 'https://api.github.com/search/repositories'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'Bearer {github_token_arg}'
    }
    params = {
        'q': keyword,
        'sort': 'stars' if sort_by_star else 'updated'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            repos_info = data['items']
            return [(repo_info['name'], repo_info['description']) for repo_info in repos_info]

    return []

# if __name__ == '__main__':
#     keyword = 'state manager'
#     sort_by = 'stars'  # 'stars' for sorting by stars, 'updated' for sorting by last updated date
#     repos = search_github_repos(keyword, sort_by)
#     if repos:
#         print(f"Repositories related to '{keyword}' (sorted by {sort_by}):")
#         for repo_name, repo_description in repos:
#             print(f"Repo Name: {repo_name}")
#             print(f"Description: {repo_description}\n")
#     else:
#         print(f"No repositories found related to '{keyword}'.")


def get_repos_from_githubusername(githubusername):
    """
    /ref)schnell.app.githubutils/get_repos_from_githubusername/app-generator
    """
    from .redisutils import handle_publish_to_redis
    repos = 'EMPTY'
    url = githubusername
    page = 1
    # bezkoder#100
    m = re.match(r'([A-Za-z0-9_\-]+)#(\d+)', url)
    if m:
        url = m.group(1)
        page = int(m.group(2))
    API_START = 'https://api.github.com/users/'
    if not url.startswith(API_START) and url.startswith('https://github.com'):
        from schnell.app.urlutils import first_path
        username = first_path(url)
        url = API_START + username + '/repos?sort=updated'
    elif re.match(r'[A-Za-z0-9_\-]+', githubusername):
        url = API_START + url + '/repos?sort=updated'
    url += f'&per_page=1000&page={page}'
    r = requests.get(url)
    print('list_github_repos for:', url, 'hasilkan:', r)
    if 200 <= r.status_code < 300:
        repos = '\n'.join([item['html_url'] for item in r.json()])
        handle_publish_to_redis(repos)
    return repos


def list_github_repos(bariskalimat: str, returning=True):  # bariskalimat = github owner/user name
    # if self.hasSelectedText():
    #     bariskalimat, _,_,_,_ = self.get_selected_text()
    # else:
    #     bariskalimat = self.get_line_text()
    url = bariskalimat.strip()
    page = 1
    result = []
    # bezkoder#100
    m = re.match(r'([A-Za-z0-9_\-]+)#(\d+)', url)
    if m:
        url = m.group(1)
        page = int(m.group(2))
    API_START = 'https://api.github.com/users/'
    if not url.startswith(API_START) and url.startswith('https://github.com'):
        from schnell.app.urlutils import first_path
        username = first_path(url)
        url = API_START + username + '/repos?sort=updated'
    elif re.match(r'[A-Za-z0-9_\-]+', bariskalimat):
        url = API_START + url + '/repos?sort=updated'
    url += f'&per_page=1000&page={page}'
    r = requests.get(url)
    print('list_github_repos for:', url, 'hasilkan:', r)
    if 200 <= r.status_code < 300:
        from schnell.app.printutils import indah3
        result = [item['html_url'] for item in r.json()]
        repos = '\n'.join(result)
        # self.publishrequest.emit(repos)
        indah3(repos)
    else:
        from schnell.app.promptutils import message_box_application
        message_box_application(f'{url} not found.')
    if returning:
        return result

def is_github_repo(url):
    # Define a regular expression for a GitHub repository URL
    github_repo_pattern = re.compile(r'https://github\.com/([^/]+)/([^/]+)')

    # Check if the URL matches the GitHub repository pattern
    match = github_repo_pattern.match(url)
    return bool(match)


def github_callback(url):
    os.system(f'git clone {url}')


def github_watcher(github_callback=github_callback):
    print("Listening to clipboard. Press 'q' to quit.")

    while True:
        # Get the current clipboard content
        clipboard_content = pyperclip.paste()

        # Check if the clipboard content is a GitHub repository address
        if is_github_repo(clipboard_content):
            print(f"GitHub Repository found: {clipboard_content}")
            # input('Press to continue...')
            github_callback(clipboard_content)
            pyperclip.copy('')
            print('----- END -----')

        # Check if the user pressed 'q' to quit
        if keyboard.is_pressed('q'):
            print("Exiting the loop.")
            break


def get_github_commit_info2(repo):
    # Get the latest commit SHA
    commit_sha_url = f"https://api.github.com/repos/{repo}/commits?per_page=1"
    commit_sha_response = requests.get(commit_sha_url).json()
    commit_sha = jq('.[0].sha').transform(commit_sha_response)

    # Get detailed information about the commit
    commit_info_url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}"
    commit_info_response = requests.get(commit_info_url).json()
    
    # Display relevant information
    author = jq('.author.login').transform(commit_info_response)
    email = jq('.commit.author.email').transform(commit_info_response)
    date = jq('.commit.author.date').transform(commit_info_response)
    message = jq('.commit.message').transform(commit_info_response)

    # Display file changes and diffs
    files = jq('.files').transform(commit_info_response)
    patches = [jq('.patch').transform(file) for file in files]

    return {
        'Author': author,
        'Email': email,
        'Date': date,
        'Message': message,
        'Files': files,
        'Patches': patches
    }


def get_github_commit_info3(repo):
    # Get the latest commit SHA
    commit_sha_url = f"https://api.github.com/repos/{repo}/commits?per_page=1"
    commit_sha_response = requests.get(commit_sha_url).json()
    print("Commit SHA Response:", commit_sha_response)  # Added for debugging
    commit_sha = jq('.[0].sha').transform(commit_sha_response)

    # Get detailed information about the commit
    commit_info_url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}"
    commit_info_response = requests.get(commit_info_url).json()
    print("Commit Info Response:", commit_info_response)  # Added for debugging

    # Display relevant information
    author = jq('.author.login').transform(commit_info_response)
    email = jq('.commit.author.email').transform(commit_info_response)
    date = jq('.commit.author.date').transform(commit_info_response)
    message = jq('.commit.message').transform(commit_info_response)

    # Display file changes and diffs
    files = jq('.files').transform(commit_info_response)
    patches = [jq('.patch').transform(file) for file in files]

    return {
        'Author': author,
        'Email': email,
        'Date': date,
        'Message': message,
        'Files': files,
        'Patches': patches
    }


def get_github_commit_info(repo, token=current_working_token):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # Get the latest commit SHA
    commit_sha_url = f"https://api.github.com/repos/{repo}/commits?per_page=1"
    commit_sha_response = requests.get(commit_sha_url, headers=headers).json()
    print("Commit SHA Response:", commit_sha_response)  # Added for debugging
    commit_sha = jq('.[0].sha').transform(commit_sha_response)

    # Get detailed information about the commit
    commit_info_url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}"
    commit_info_response = requests.get(commit_info_url, headers=headers).json()
    print("Commit Info Response:", commit_info_response)  # Added for debugging

    # Display relevant information
    author = jq('.author.login').transform(commit_info_response)
    email = jq('.commit.author.email').transform(commit_info_response)
    date = jq('.commit.author.date').transform(commit_info_response)
    message = jq('.commit.message').transform(commit_info_response)

    # Display file changes and diffs
    files = jq('.files').transform(commit_info_response)
    patches = [jq('.patch').transform(file) for file in files]

    return {
        'Author': author,
        'Email': email,
        'Date': date,
        'Message': message,
        'Files': files,
        'Patches': patches
    }


def test_get_github_commit_info2():
    repo_name = "oven-sh/bun"
    github_token = "YOUR-GITHUB-TOKEN"
    commit_info = get_github_commit_info(repo_name, github_token)
    print("Author:", commit_info['Author'])
    print("Email:", commit_info['Email'])
    print("Date:", commit_info['Date'])
    print("Message:", commit_info['Message'])
    print("Files:", commit_info['Files'])
    print("Patches:", commit_info['Patches'])


def test_get_github_commit_info():
    repo_name = "oven-sh/bun"
    commit_info = get_github_commit_info(repo_name)
    print("Author:", commit_info['Author'])
    print("Email:", commit_info['Email'])
    print("Date:", commit_info['Date'])
    print("Message:", commit_info['Message'])
    print("Files:", commit_info['Files'])
    print("Patches:", commit_info['Patches'])


class GitHubRepoInspector:
    def __init__(self, local_repo_path, remote_repo_url, github_token):
        self.local_repo_path = local_repo_path
        self.remote_repo_url = remote_repo_url
        self.github = Github(github_token)
        self.repo = git.Repo(local_repo_path)
        self.remote = self.repo.remotes.origin
        self.remote.fetch()

    def get_commit_count(self):
        return len(list(self.repo.iter_commits()))

    def get_branches(self):
        return [branch.name for branch in self.repo.branches]

    def is_clone(self):
        for remote in self.repo.remotes:
            for url in remote.urls:
                if url == self.remote_repo_url:
                    return True
        return False

    def get_commit_difference(self):
        local_commit = self.repo.head.commit
        remote_commit = self.remote.refs.master.commit

        local_sha = local_commit.hexsha
        remote_sha = remote_commit.hexsha

        commits_behind = list(self.repo.iter_commits(f'{local_sha}..{remote_sha}'))
        commits_ahead = list(self.repo.iter_commits(f'{remote_sha}..{local_sha}'))

        return {
            'local_commit': local_sha,
            'remote_commit': remote_sha,
            'commits_behind': commits_behind,
            'commits_ahead': commits_ahead
        }

    def display_commit_info(self, commits):
        for commit in commits:
            print(f"Commit: {commit.hexsha}")
            print(f"Author: {commit.author.name} <{commit.author.email}>")
            print(f"Date: {commit.committed_datetime}")
            print(f"Message: {commit.message}")
            print('-' * 80)

    def get_changed_files(self, commits):
        changed_files = {}
        for commit in commits:
            for diff in commit.diff(commit.parents[0] if commit.parents else None):
                file_path = diff.a_path if diff.a_path else diff.b_path
                if file_path not in changed_files:
                    changed_files[file_path] = []
                changed_files[file_path].append({
                    'commit': commit.hexsha,
                    'author': commit.author.name,
                    'date': commit.committed_datetime
                })
        return changed_files

    def generate_report(self):
        if not self.is_clone():
            print("The local repository is not a clone of the remote repository.")
            return

        commit_diff = self.get_commit_difference()
        print(f"Local commit: {commit_diff['local_commit']}")
        print(f"Remote commit: {commit_diff['remote_commit']}")
        print(f"Commits behind: {len(commit_diff['commits_behind'])}")
        print(f"Commits ahead: {len(commit_diff['commits_ahead'])}")

        print("\nCommits behind:")
        self.display_commit_info(commit_diff['commits_behind'])

        print("\nCommits ahead:")
        self.display_commit_info(commit_diff['commits_ahead'])

        changed_files = self.get_changed_files(commit_diff['commits_behind'])
        print("\nChanged files in behind commits:")
        for file, changes in changed_files.items():
            print(f"File: {file}")
            for change in changes:
                print(f"  Commit: {change['commit']} by {change['author']} on {change['date']}")
            print('-' * 80)

# Example usage:
# inspector = GitHubRepoInspector(local_repo_path='/path/to/local/repo', remote_repo_url='https://github.com/username/repo.git', github_token='your_github_token')
# inspector.generate_report()

# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\tools_config.py
# from schnell.app.llmutils.langchainutils.tools_config import tools_config
# tools_config['github']['accounts']