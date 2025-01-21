from github import Github

# from schnell.app.githubutils.remote_git import RemoteGit
class RemoteGit:
    def __init__(self, github_token, owner, repo_name):
        self.github = Github(github_token)
        self.repo = self.github.get_repo(f"{owner}/{repo_name}")

    def get_branches(self):
        return [branch.name for branch in self.repo.get_branches()]

    def get_releases(self):
        return [{
            "tag_name": release.tag_name,
            "published_at": release.published_at
        } for release in self.repo.get_releases()]

    def get_tags(self):
        return [{
            "name": tag.name,
            "tarball_url": f"https://github.com/{self.repo.full_name}/archive/refs/tags/{tag.name}.tar.gz"
        } for tag in self.repo.get_tags()]

    def get_commit_count(self):
        return self.repo.get_commits().totalCount

    def get_commit_page_url(self):
        return f"https://github.com/{self.repo.full_name}/commits"

# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\tools_config.py
# from schnell.app.llmutils.langchainutils.tools_config import tools_config
# tools_config['github']['accounts']
