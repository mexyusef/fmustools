import git

# from schnell.app.githubutils.local_git import LocalGit
class LocalGit:
    def __init__(self, local_repo_path):
        self.repo = git.Repo(local_repo_path)
        
    def get_commit_count(self):
        return len(list(self.repo.iter_commits()))

    def get_branches(self):
        return [branch.name for branch in self.repo.branches]

# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\tools_config.py
# from schnell.app.llmutils.langchainutils.tools_config import tools_config
# tools_config['github']['accounts']

# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\tools\github.py
# from schnell.app.llmutils.langchainutils.utils import randomly_select_account
# from schnell.app.cryptoutils import dekripsi