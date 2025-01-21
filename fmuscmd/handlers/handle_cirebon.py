import os, subprocess, traceback

from schnell.app.dirutils import (
    files, dirs,
    isfile, isdir,
    joiner,
    joinhere,
)
from schnell.app.fileutils import (
    define_filepath_barisentry,
    define_filepath_equal,
    get_daftar_isi,
)
from schnell.app.githubutils import list_github_repos
from schnell.app.printutils import (
    indah4,
    print_source_code_copy,
    print_source_code_file,
    print_source_code_file_with_markdown,
    print_json,
)
from .common import run_command_in_folder, count_suffix
from configuration_values import cirebon_files_mapping, config_app
from fmuslib import (
	run_fmus_for_content,
	run_fmus_for_content_in_thread, 
	run_fmus_for_file_in_thread,
	run_fmus_for_file,
)


FILE_FMUS = joinhere(__file__, 'handle_cirebon.fmus')


def handle_cirebon(base_folder, self_temporary_prompt, self_refresh_completer):
    """
    """
    github_repo = cirebon_files_mapping.get(base_folder)
    daftar_folder = dirs(base_folder)
    daftar_isi = (get_daftar_isi(FILE_FMUS)
        + ['new-download', 'explorer']
        )
    meta_dict = {k:None for k in daftar_isi}
    meta_dict.update({
        item: {
            'clone': None,
            'git pull': None,
        }
        for item in daftar_folder
    })
    jawab = None
    try:
        while jawab not in ['x', 'exit']:
            jawab = self_temporary_prompt(f"[{base_folder}]👉 ",
                meta_dict=meta_dict,
                choices=daftar_isi,
                do_validation=False)
            indah4(jawab, warna='cyan')
            if jawab:
                if jawab == 'c':
                    os.system('cls')
                    print()
                    os.system(f'vscode {FILE_FMUS}')
                    print()
                    os.system(f'vscode {base_folder}')
                    print()
                    ciledugfile = r'C:\work\ciledug\ciledug\fmusperintah\cirebon.txt'
                    os.system(f'vscode {ciledugfile}')
                    print()
                elif jawab == 'explorer':
                    os.system(f'explorer {base_folder}')
                    print()
                elif jawab == 'new-download':
                    repo_list = list_github_repos(github_repo)
                    for repo in repo_list:
                        run_command_in_folder(base_folder, f'git clone {repo}')
                elif jawab.endswith(' clone'):
                    repo_folder = jawab.removesuffix(' clone').strip()
                    fmus_content = define_filepath_barisentry(FILE_FMUS, 'clone repo to curdir')
                    fmus_content = (
                        fmus_content
                        .replace('__REPONAME__', repo_folder)
                        .replace('__REPOPATH__', joiner(base_folder, repo_folder))
                    )
                    if config_app['thread']:
                        run_fmus_for_content_in_thread(fmus_content, dirpath=os.getcwd(), filepath=FILE_FMUS)
                    else:
                        run_fmus_for_content(fmus_content, dirpath=os.getcwd(), filepath=FILE_FMUS)
                elif jawab.endswith(' git pull'):
                    repo_folder = jawab.removesuffix(' git pull').strip()
                    repo_path = joiner(base_folder, repo_folder)
                    run_command_in_folder(repo_path, 'git pull')
    except KeyboardInterrupt:
        indah4('[handle_cirebon] Press Ctrl+C')
    except Exception as exc:
        indah4(f'[handle_cirebon] Exception: {str(exc)}.')
    self_refresh_completer()
