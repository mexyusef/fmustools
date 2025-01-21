import os
from git import Repo
from .appconfig import programming_data
from .utils import env_get

"""
misal kita punya git folder
folder = /path/to/mmm
maka kita bisa cek statusnya
st = git_status(repo_init(folder))
print(st)

"""
# https://gitpython.readthedocs.io/en/stable/tutorial.html

def create_bare_repo(rw_dir):
    bare_repo = Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
    assert bare_repo.bare


# A repo object provides high-level access to your data,
# it allows you to create and delete heads, tags and remotes 
# and access the configuration of the repository.

def assert_repo_config(repo):
    repo.config_reader()        # get a config reader for read-only access
    with repo.config_writer():  # get a config writer to change configuration
        pass                    # call release() to be sure changes are written 
                                # and locks are released


def query_repo(bare_repo, repo):
    """Query the active branch, 
    query untracked files or whether the repository data has been modified.
    """
    assert not bare_repo.is_dirty() # check the dirty state
    l = repo.untracked_files        # retrieve a list of untracked files
    # ['my_untracked_file']
    print(l)


def clone_existing_repo(repo, rw_dir):
    cloned_repo = repo.clone(os.path.join(rw_dir, 'to/this/path'))
    assert cloned_repo.__class__ is Repo     # clone an existing repository


def init_empty_repo(rw_dir):
    assert Repo.init(os.path.join(rw_dir, 'path/for/new/repo')).__class__ is Repo


def repo_to_tar(repo, rw_dir):
    with open(os.path.join(rw_dir, 'repo.tar'), 'wb') as fp:
        repo.archive(fp)


def get_commits_at_revision(repo, revision):
    """
    repo.commit('master')
    repo.commit('v0.8.1')
    repo.commit('HEAD~10')
    """
    return repo.commit(revision)


def repo_init(dirpath):
    """
    kembalikan "repo" obj dimana kita bisa akses .git dan .index
    """
    return Repo.init(dirpath)


def repo_git(dirpath):
    return repo_init(dirpath).git


def repo_index(dirpath):
    return repo_init(dirpath).index


def git_add(repo, file):
    """
    tentu bisa utk "git add ."
    """
    repo.git.add(file)


def git_adds(repo, files):
    for file in files:
        repo.git.add(file)


def git_status(repo):
    return repo.git.status()


def git_commit(repo, msg):
    return repo.git.commit(m=msg)


def git_co_branch(repo, remotename, localname=None):
    """
    repo.git.checkout( 'origin/somebranch', b='somebranch' )
    """
    if not localname:
        localname = remotename
    return repo.git.checkout(f'origin/{remotename}', b=localname)


def index_commit(index, msg):
    index.commit(msg)


# global utk hold repos, bisa ke flaskfaker, ulang, schnell, dst
# cara pake misalnya
# repo_holder['schnell'] = repo_init(env_get('ULIBPY_ROOTDIR'))
# abis itu tinggal:
# git_status(repo_holder['schnell'])
# atau
# repo_holder['schnell'].git.status()

repo_holder = {
    'sido'      : repo_init(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_ROOTDIR"]),
    'mmm'       : repo_init(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_MMMDIR"]),
    'sejarah'   : repo_init(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_ULANGDIR"]),
}
RH = repo_holder


def rh_status(key):
    if key in RH:
        return RH[key].git.status()
    return None


def sido_status():
    return RH['sido'].git.status()


def sido_diff():
    return RH['sido'].git.diff()


def sido_add(file):
    return RH['sido'].git.add(file)


def sido_commit(msg):
    return RH['sido'].git.commit(m=msg)


def sido_push():
    return RH['sido'].git.push()


def is_git_repo(dir_path):
    try:
        repo = Repo(dir_path)
        return True
    except Exception as e:
        return False


def test_is_git_repo():
    directory_path = '/path/to/your/directory'
    if is_git_repo(directory_path):
        print(f"The directory '{directory_path}' is a Git repository.")
    else:
        print(f"The directory '{directory_path}' is not a Git repository.")


def get_branch_and_remote(dir_path):
    branch_name = None
    remote_url = None
    try:
        repo = Repo(dir_path)
        branch_name = repo.active_branch.name
        remote_url = repo.remote().url
        return branch_name, remote_url
    except Exception as e:
        # print(e)
        return branch_name, remote_url


def test_get_branch_and_remote():
    directory_path = '/path/to/your/directory'
    branch_name, remote_url = get_branch_and_remote(directory_path)

    if branch_name and remote_url:
        print(f"Branch: {branch_name}")
        print(f"Remote URL: {remote_url}")
    else:
        print(f"Failed to retrieve branch and remote URL for the directory '{directory_path}'.")


def get_latest_commit_info(dir_path):
    # Check if the given path is a directory
    if not os.path.isdir(dir_path):
        raise ValueError("Invalid directory path")

    # Initialize a Git repository object
    repo = Repo(dir_path)

    # Get the latest commit
    latest_commit = repo.head.commit

    # Extract information from the commit
    commit_datetime = latest_commit.authored_datetime
    # commit_author = latest_commit.author.name
    commit_author = latest_commit.author.email
    commit_message = latest_commit.message
    num_file_changes = sum(len(diff) for diff in latest_commit.diff())

    # Return the commit information as a tuple
    return commit_datetime, commit_author, commit_message, num_file_changes


def test_get_latest_commit_info():
    dir_path = "/path/to/your/git/repo"
    commit_info = get_latest_commit_info(dir_path)

    print("Datetime:", commit_info[0])
    print("Author:", commit_info[1])
    print("Message:", commit_info[2])
    print("Number of File Changes:", commit_info[3])


from git import Repo
from rich.console import Console
from rich.table import Table

# g "/ref)schnell.app.gitutils/list_commits_with_changes"
# g "/ref)schnell.app.gitutils/list_commits_with_changes/max_count=50"
def list_commits_with_changes(repo_path=".", max_count=100):
    # Initialize repository and console
    repo = Repo(repo_path)
    console = Console()

    # Create a rich table
    table = Table(title="Git Commits and Changes")
    table.add_column("SHA", style="cyan", no_wrap=True)
    table.add_column("Message", style="magenta")
    table.add_column("Author", style="green")
    table.add_column("Date", style="yellow")
    table.add_column("Modified Files", style="white")

    # Loop through commits
    # for commit in repo.iter_commits():
    for commit in repo.iter_commits(max_count=max_count):  # Limit to the last 100 commits
        # Get list of files changed in the commit
        files_changed = []
        for diff in commit.diff(commit.parents[0] if commit.parents else None):
            files_changed.append(diff.a_path if diff.a_path else diff.b_path)
        files_changed_str = "\n".join(files_changed) if files_changed else "No files"

        # Add row to the table
        table.add_row(
            commit.hexsha[:7],
            commit.message.strip(),
            commit.author.name,
            str(commit.committed_datetime),
            files_changed_str
        )

    # Print the table
    console.print(table)

# g "/ref)schnell.app.gitutils/file_history"
# g "/ref)schnell.app.gitutils/file_history/file_path=requirements.txt"
# g "/ref)schnell.app.gitutils/file_history/file_path='path/to/file'"
# g "/ref)schnell.app.gitutils/file_history/file_path=aider\repo.py"
def file_history(repo_path=".", file_path=None):
    # Validate input
    if file_path is None:
        print("Error: Please provide a file path.")
        return
    
    # Initialize repository and console
    repo = Repo(repo_path)
    console = Console()

    # Create a rich table
    table = Table(title=f"History of {file_path}")
    table.add_column("SHA", style="cyan", no_wrap=True)
    table.add_column("Message", style="magenta")
    table.add_column("Author", style="green")
    table.add_column("Date", style="yellow")
    table.add_column("File", style="white")

    # Get file history
    try:
        for commit in repo.iter_commits(paths=file_path, reverse=True):  # reverse=True to start from the initial commit
            table.add_row(
                commit.hexsha[:7],
                commit.message.strip(),
                commit.author.name,
                str(commit.committed_datetime),
                file_path
            )
    except Exception as e:
        print(f"Error fetching history for {file_path}: {e}")
        return

    # Print the table
    console.print(table)

if __name__ == "__main__":
    # You can specify the file path as needed, relative to repo path or absolute
    file_history(file_path="path/to/your/file")  # Provide your file path here
