import git, os, sys
from git import Repo, InvalidGitRepositoryError

# import os, sys
# from pprint import pprint as pp
# from uuid import uuid4 as u4
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sys.path.extend([schnelldir, '..'])
# # print(schnelldir)
# from schnell.app.transpiler.frontend.main import process_language
# from schnell.app.printutils import indah4
# from schnell.app.treeutils import (
#   anak,
#   data, 
#   token, 
#   child1, 
#   child2, 
#   child3, 
#   child4,
#   child,
#   chdata,
#   chtoken,  
#   ispohon, istoken,
#   beranak,
#   sebanyak,
#   jumlahanak, 
# )
from schnell.app.dirutils import first_part_of_relative_dir, joiner, joinhere
from schnell.app.utils import env_get, perintah_shell_wait, perintah_shell
from schnell.app.datetimeutils import sejam, sekarang, epoch

from rich.console import RenderableType
from rich.syntax import Syntax
from rich.table import Table
from rich.traceback import Traceback
from rich.layout import Layout
from schnell.vendor.textual.app import App
from schnell.vendor.textual.reactive import Reactive
from schnell.vendor.textual.widgets import (
    Header, Footer, 
    FileClick, DirClick, 
    ScrollView, Static, Placeholder,
    DirectoryTree,
)
from schnell.vendor.textual.widget import Widget
from schnell.vendor.textual.views import GridView
from schnell.app.githubutils import get_issues


fetch_origin_status = {}


class MyApp(App):
    
    content1 : Reactive[str] = Reactive('')
    content2 : Reactive[str] = Reactive('')
    content_issues: Reactive[str] = Reactive('')
    content_branches: Reactive[str] = Reactive('')
    location = env_get('ULIBPY_DATA_FOLDER_ABS')
    current_repo = Reactive('')


    async def on_load(self) -> None:
        await self.bind("b", "view.toggle('sidebar')", "Sidebar")
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")
        await self.bind("ctrl+d", "git_detail", "View Git")
        self.path = self.location


    async def action_git_detail(self) -> None:
        from .gitdetail import git_detail
        if self.current_repo and self.current_repo.startswith('https://github.com/'):
            # belum berhasil jalankan...
            # git_detail(self.current_repo, self.current_repo)
            detailer = joinhere(__file__, 'gitdetail.py')
            perintah_shell(f'python {detailer}')
            # try:
            #     await git_detail(self.current_repo, self.current_repo)
            # except Exception as err:
            #     print(f"""
            #     {err}
            #     ==
            #     repo = {self.current_repo}
            #     """)

    async def on_mount(self) -> None:
        # self.body = MyEditor(name='main')
        # self.body = ScrollView()

        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        self.directory = DirectoryTree(self.path, "Code")
        # await self.view.dock(ScrollView(self.directory), edge="left", size=48, name="sidebar")
        self.editor_issues = ScrollView(contents=Syntax(self.content_issues, 'python', theme='material', line_numbers=True, word_wrap=True, indent_guides=True))
        self.editor_branches = ScrollView(contents=Syntax(self.content_branches, 'python', theme='murphy', line_numbers=True, word_wrap=True, indent_guides=True))
        sidebar_grid = await self.view.dock_grid(edge="left", name="sidebar", size=48)
        sidebar_grid.add_column(fraction=1, name='col_sidebar')
        sidebar_grid.add_row(fraction=4, name='row_dirtree')
        sidebar_grid.add_row(fraction=2, name='row_issue')
        sidebar_grid.add_row(fraction=1, name='row_branch')
        sidebar_grid.add_areas(
            area1='col_sidebar,row_dirtree',
            area2='col_sidebar,row_issue',
            area3='col_sidebar,row_branch',
        )
        sidebar_grid.place(
            area1=ScrollView(self.directory),
            # area2=Placeholder(name='issues'),
            area2=self.editor_issues,
            # area3=Placeholder(name='branches'),
            area3=self.editor_branches,
        )

        # await self.view.dock(self.body, edge="top")
        grid = await self.view.dock_grid(edge="top", name="body")
        grid.add_column(fraction=1, name='single', min_size=20)
        grid.add_row(fraction=1, name='pertama')
        grid.add_row(fraction=2, name='kedua')
        grid.add_areas(
            area1='single,pertama',
            area2='single,kedua',
        )
        self.editor1 = ScrollView(contents=Syntax(self.content1, 'python', theme='dracula', line_numbers=True, word_wrap=True, indent_guides=True))
        self.editor2 = ScrollView(contents=Syntax(self.content2, 'python', theme='xcode', line_numbers=True, word_wrap=True, indent_guides=True))
        grid.place(
            area1=self.editor1,
            area2=self.editor2,
        )


    async def handle_file_click(self, message: FileClick) -> None:
        """
        A message sent by the directory tree when a file is clicked.
        await self.emit(FileClick(self, dir_entry.path))
        """
        # syntax: RenderableType
        # try:
        #     syntax = Syntax(message.path, 'python', line_numbers=True, word_wrap=True, indent_guides=True, theme="monokai")
        # except Exception:
        #     syntax = Traceback(theme="monokai", width=None, show_locals=True)
        self.app.sub_title = os.path.basename(message.path)

        content1 = Syntax(message.path, 'python', theme='dracula', line_numbers=True, word_wrap=True, indent_guides=True)
        await self.editor1.update(content1)

        content2 = Syntax.from_path(message.path, theme='xcode', line_numbers=True, word_wrap=True, indent_guides=True)
        await self.editor2.update(content2)
        # await self.body.lower_scroll.update(syntax)
        # editor = MyEditor('ok', message.path, f'info mengenai {message.path}')
        # await self.body.update(editor)
        # self.body.set_contents(bawah=message.path)


    async def editor_content(self, content, which='editor1'):
        if which == 'editor1':
            syntax_content = Syntax(content, 'python', theme='dracula', line_numbers=True, word_wrap=True, indent_guides=True)
            await self.editor1.update(syntax_content)
        elif which == 'editor2':
            syntax_content = Syntax(content, 'python', theme='xcode', line_numbers=True, word_wrap=True, indent_guides=True)
            await self.editor2.update(syntax_content)
        elif which == 'editor_issues':
            syntax_content = Syntax(content, 'python', theme='material', line_numbers=True, word_wrap=True, indent_guides=True)
            await self.editor_issues.update(syntax_content)
        elif which == 'editor_branches':
            syntax_content = Syntax(content, 'python', theme='murphy', line_numbers=True, word_wrap=True, indent_guides=True)
            await self.editor_branches.update(syntax_content)


    async def handle_dir_click(self, message: DirClick) -> None:
        diffcontent = message.path
        awalnya = MyApp.location
        jarak = os.path.relpath(message.path, awalnya)
        is_direct_child = os.path.basename(message.path) == jarak
        subjudul = message.path
        repo = None
        if is_direct_child: # jika folder git
            if not jarak in fetch_origin_status:
                '''
                jika belum fetch, maka fetch dulu origin
                di awal, waktu manggil gitor, sudah ada proses fetch dengan thread
                '''
                repo = Repo(message.path)
                fetch_origin_status[jarak] = {
                    'waktu': sekarang(),
                    'repo': repo,
                }
                fetchinfo = repo.remotes.origin.fetch()
                if fetchinfo:
                    # bedaorigin = repo.index.diff(repo.remotes.origin.refs.master.commit)
                    bedaorigin = repo.index.diff(repo.remotes.origin.refs.HEAD.commit)
                    daftar_file_pulled = [item.a_path for item in bedaorigin]
                    content = '\n'.join(daftar_file_pulled)
            else:
                '''
                jika sudah fetch origin, objek repo either sudah terisi atau None
                tiap repo bisa non-git, kita allow nilai null utk fetch_origin_status[jarak]['repo']
                    ini karena waktu di awal terjadi exception coba buat Repo pada folder
                '''
                if fetch_origin_status[jarak]['repo']:
                    repo = fetch_origin_status[jarak]['repo']
                    # mending kita kasih log saja, sejak hari ini???
                    cetak = '%n%ar, %an (%ae) wrote "%s" = %h'
                    content = repo.git.log(f'--format={cetak}', '--stat', '-n 10')
                else:
                    '''
                    utk non-git folder
                    '''
                    content = message.path + ' is not a git folder.'
            if repo: # if 'diff' in fetch_origin_status[jarak]:
                self.current_repo = repo.remotes.origin.url
                diffcontent = repo.git.log('--format=%n************************%n[%h by %an (%ae), %ar, %s]', '--diff-merges=first-parent', '-p', '-n 5')
                if not diffcontent:
                    diffcontent = 'NO DIFFS'
                
                content2 = Syntax(diffcontent, lexer='python', theme='xcode', line_numbers=True, word_wrap=True, indent_guides=True)
                await self.editor2.update(content2)
                # diffcontent = 'ini diffcontent dummy, jk ada repo'
                # proses diffcontent
                # diff --git a/any-non-space b/.*
                # print('terima diffcontent', diffcontent[:100])

                origins = [h.name for h in repo.remote().refs]
                await self.editor_content('\n'.join(origins), 'editor_branches')

                issues = get_issues(repo.remotes.origin.url)
                issues = [f'[{item.number}] {item.title}' for item in issues]
                await self.editor_content('\n'.join(issues), 'editor_issues')
        else:
            # subfolder dalam git-folder gak perlu diproses
            # atau subsubfolder git dalam subfolder non-git
            content = message.path

        # self.app.sub_title = f"""{message.path} => {jarak} [{is_direct_child}]"""
        # self.app.sub_title = f"""{message.path} => {jarak}"""
        if repo:
            subjudul = repo.remotes.origin.url
        self.app.sub_title = subjudul
        
        content1 = Syntax(content, 'python', theme='dracula', line_numbers=True, word_wrap=True, indent_guides=True)
        await self.editor1.update(content1)


def reset():
    global fetch_origin_status
    fetch_origin_status = {}


def fetch_origin(lokasi, jarak):
    try:
        r = Repo(lokasi)
        #fi = r.remotes.origin.refs.HEAD.fetch()
        fi = r.remotes.origin.fetch()
        fetch_origin_status[jarak] = {
            'waktu': sekarang(),
            'repo': r,
            'diff': r.git.diff("head", r.remotes.origin.refs.HEAD),
            # 'branches': [h.name for h in r.remote().refs],
        }
        # print(f"{lokasi} = fetch info sebanyak {len(fi)} commit baru.")
    except Exception as err:
        print(f"[{lokasi}] bukan git folder.")
        fetch_origin_status[jarak] = {
            'waktu': sekarang(),
            'repo': None,
        }


def gitor(lokasi=env_get('ULIBPY_DATA_FOLDER_ABS')):
    reset()
    # cek apa lokasi itu git folder atau bukan
    try:
        mainrepo = Repo(lokasi)
        fetch_origin_status['main'] = mainrepo
    except InvalidGitRepositoryError as err:
        fetch_origin_status['main'] = None
        # jika bukan git folder, maka utk tiap anaknya kita "fetch"
        from schnell.app.threadutils import mulai
        a = list(filter(lambda x: not os.path.isdir(x), os.listdir(lokasi)))
        b = [os.path.normpath(os.path.join(lokasi, item)) for item in a]
        for index,item in enumerate(b):
            '''
            a[index] berikan versi basename yg perlu utk "jarak" di fetch_origin_status
            '''
            mulai(fetch_origin, (item,a[index]))
    MyApp.location = lokasi
    MyApp.run(title="Gitor")
