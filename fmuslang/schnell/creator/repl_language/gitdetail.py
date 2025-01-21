import os, sys
from pprint import pprint as pp
from uuid import uuid4 as u4
import datetime
from dataclasses import dataclass
from functools import lru_cache
import rich.repr
from rich.console import RenderableType
from rich.syntax import Syntax
from rich.table import Table
from rich.traceback import Traceback
from rich.layout import Layout
from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.tree import Tree
from rich.text import Text

# import github

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sys.path.extend([schnelldir, '..'])
import sys
from pathlib import Path
sidoarjodir = Path(__file__).resolve().parent.parent.parent
#                              file     app     sch   sid
sys.path.append(sidoarjodir)

# from schnell.app.transpiler.frontend.main import process_language
# from schnell.app.printutils import indah4
# from schnell.app.treeutils import (
#   anak,
#   data, 
#   token,
#   child1,
#   child2,
#   child3
#   child4,
#   child,
#   chdata,
#   chtoken,
#   ispohon,
#   istoken,
#   beranak,
#   sebanyak,
#   jumlahanak,
# )
# from schnell.app.dirutils import joiner
# from schnell.app.fileutils import file_write
# from schnell.app.utils import env_get
from schnell.app.githubutils import (
    get_issues,
    get_issue_bynumber,
    get_pullrequests,
    get_pr_bynumber
)
from schnell.app.urlutils import get_content
from schnell.app.fakerutils import get_by_datatypes

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
from schnell.vendor.textual.widgets import (
    TreeControl, TreeClick, TreeNode, NodeID
)
from schnell.vendor.textual.message import Message
from schnell.vendor.textual._types import MessageTarget
from schnell.vendor.textual import events



class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        time = datetime.now().strftime("%c")
        return Align.center(time, vertical="middle")

class Header:
    def __init__(self) -> None:
        self.visible = True

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Rich[/b] Layout application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")

@dataclass
class DirEntry:
    title: str
    number: int

# EntryClick(self, dir_entry.title, dir_entry.number)
@rich.repr.auto
class EntryClick(Message, bubble=True):
    def __init__(self, sender: MessageTarget, category: str, title: str, number: int) -> None:
        """
        nanti App tinggal
        handle_entry_click(self, message: EntryClick) -> None
            message.title
            message.number
        """
        self.title = title
        self.number = number
        self.category = category
        super().__init__(sender)


issue_pr_mapping = {
    'category': ['Issue', 'PR'],
    'Issue': {
        'theme': 'xcode',
        'fetches': get_issues,
        'fetch': get_issue_bynumber,
    },
    'PR': {
        'theme': 'inkpot',
        'fetches': get_pullrequests,
        'fetch': get_pr_bynumber,
    },
}

# ini ada 2 jenis, issues+pullrequests...
class DirectoryTree(TreeControl[DirEntry]):


    has_focus: Reactive[bool] = Reactive(False)
    guide_style: Reactive[str] = Reactive('bold bright_green')


    def __init__(self, category: str, github_repo: str, name: str = None) -> None:
        """
        category: Issues, Pull Requests
        """
        label = category.capitalize() + ' List'
        data = DirEntry(category, -1) # issue/pr title dan number utk root node
        self.github_repo = github_repo
        self.category = category
        super().__init__(label, name=name, data=data)
        if category == 'PR':
            self.guide_style = 'bold bright_yellow'
        self.root.tree.guide_style = self.guide_style


    def on_focus(self) -> None:
        self.has_focus = True


    def on_blur(self) -> None:
        self.has_focus = False


    async def watch_hover_node(self, hover_node: NodeID) -> None:
        for node in self.nodes.values():
            node.tree.guide_style = (
                "bold not dim red" if node.id == hover_node else self.guide_style
            )
        self.refresh(layout=True)


    def render_node(self, node: TreeNode[DirEntry]) -> RenderableType:
        return self.render_tree_label(
            node,
            # node.data.is_dir,
            node.expanded,
            node.is_cursor,
            node.id == self.hover_node,
            self.has_focus,
        )


    @lru_cache(maxsize=1024 * 32)
    def render_tree_label(
        self,
        node: TreeNode[DirEntry],
        # is_dir: bool,
        expanded: bool,
        is_cursor: bool,
        is_hover: bool,
        has_focus: bool,
    ) -> RenderableType:
        meta = {
            "@click": f"click_label({node.id})",
            "tree_node": node.id,
            "cursor": node.is_cursor,
        }
        label = Text(node.label) if isinstance(node.label, str) else node.label
        if is_hover:
            label.stylize("underline")
        # if is_dir:
        #     label.stylize("bold magenta")
        #     icon = "📂" if expanded else "📁"
        # else:
        #     label.stylize("bright_green")
        #     icon = "📄"
        #     label.highlight_regex(r"\..*$", "green")
        label.stylize("bold blue" if self.category == issue_pr_mapping['category'][1] else "bold magenta")
        icon = "📄" if self.category == issue_pr_mapping['category'][1] else ("📂" if expanded else "📁")

        # if label.plain.startswith("."):
        #     label.stylize("dim")

        if is_cursor and has_focus:
            label.stylize("reverse")

        icon_label = Text(f"{icon} ", no_wrap=True, overflow="ellipsis") + label
        icon_label.apply_meta(meta)
        return icon_label


    async def handle_tree_click(self, message: TreeClick[DirEntry]) -> None:
        dir_entry = message.node.data
        self.label = f'#{dir_entry.number}'
        # self.refresh()
        await self.emit(EntryClick(self, self.category, dir_entry.title, dir_entry.number))


    async def on_mount(self, event: events.Mount) -> None:
        await self.load_directory(self.root)


    async def load_directory(self, node: TreeNode[DirEntry]):
        # for i in range(self.jumlahnodes):
        #     node_name = f'{self.category} #{i+1}'
        #     await node.add(node_name, DirEntry(self.category, i+1))
        fetches = issue_pr_mapping[self.category]['fetches'](self.github_repo)
        for item in fetches:
            # node_name = f'{self.category} #{index+1}'
            item_title = item.title
            item_no = item.number
            node_name = f"[{item_no}] {item_title}"
            await node.add(node_name, DirEntry(item_title, item_no))
        
        node.loaded = True
        await node.expand()
        self.refresh(layout=True)


class MyApp(App):

    status: Reactive[str] = Reactive('Ini status App default')
    github_repo = Reactive('unifyai/ivy')

    # def __init__(self, repo: str, status: str) -> None:
    #     super().__init__()
    #     self.status = status
    #     self.github_repo = repo

    async def on_load(self) -> None:
        # await self.bind("b", "view.toggle('sidebar')", "Sidebar")
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")

    async def on_mount(self) -> None:
        # # bikin table 5x5
        # tbl = Table.grid(padding=1, expand=True)
        # tbl.add_column(style='on green')
        # tbl.add_column()
        # tbl.add_column(style='on magenta')
        # tbl.add_column()
        # tbl.add_column(style='on yellow')
        # for i in range(5):
        #     # tbl.add_row(get_by_datatypes('string'), get_by_datatypes('string'), get_by_datatypes('string'), get_by_datatypes('string'), get_by_datatypes('string'))
        #     tbl.add_row(
        #         Placeholder(name=f'{i},1'),
        #         Placeholder(name=f'{i},2'),
        #         Placeholder(name=f'{i},3'),
        #         Placeholder(name=f'{i},4'),
        #         Placeholder(name=f'{i},5'),
        #     )

        grid = await self.view.dock_grid(edge="top", name="body", gutter=(1,1))

        grid.add_row(fraction=1, name='row1')
        grid.add_row(fraction=7, name='row2')
        grid.add_row(fraction=7, name='row3')
        grid.add_row(fraction=1, name='row4')

        grid.add_column(fraction=3, name='col1')
        grid.add_column(fraction=7, name='col2')

        grid.add_areas(
            area1_2='col1-start|col2-end,row1', 
            area3='col1,row2', area4='col2,row2', area5='col1,row3', area6='col2,row3', 
            area7_8='col1-start|col2-end,row4'
        )

        self.issue_tree = DirectoryTree(issue_pr_mapping['category'][0], github_repo=self.github_repo, name='issue-tree')
        self.pr_tree = DirectoryTree(issue_pr_mapping['category'][1], github_repo=self.github_repo, name='pr-tree')

        self.issue_editor = ScrollView(Syntax(
                'initial content',
                lexer='python',
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                theme=issue_pr_mapping [issue_pr_mapping['category'][0]] ['theme'],
            ))
        self.pr_editor = ScrollView(Syntax(
                'initial content',
                lexer='python',
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                theme=issue_pr_mapping [issue_pr_mapping['category'][1]] ['theme'],
            ))

        # message_panel = Panel(
        #     Align.center(
        #         # Group(intro_message, "\n", Align.center(sponsor_message)),
        #         Header(),
        #         vertical="middle",
        #     ),
        #     box=box.ROUNDED,
        #     padding=(1, 2),
        #     title="[b red]Ini adalah judul",
        #     border_style="bright_blue",
        #     expand=True,
        # )
        self.message_panel = ScrollView(Text(self.status, style='bright_green on black'))
        # self.message_panel = ScrollView(Clock())
        grid.place(
            # header
            area1_2=self.message_panel,

            # issues
            area3=ScrollView(self.issue_tree),
            area4=self.issue_editor,
            
            # pullrequest
            area5=ScrollView(self.pr_tree),
            area6=self.pr_editor,
            
            # footer
            area7_8=Placeholder(name='7 dan 8'))
    


    def issue_pr_content(self, message):
        if message.number <= 0: # root node skip
            return
        data = issue_pr_mapping[message.category]['fetch'](message.number, github_repo=self.github_repo)
        if message.category == issue_pr_mapping['category'][0]:
            # utk issues
            assignees = ', '.join([item.login for item in data.assignees])
            labels = ', '.join([item.name for item in data.labels])
            issue_no = data.number
            username = data.user.login
            content = f"""[{issue_no}][{username}]
created = {data.created_at}
updated = {data.updated_at}
url = [{data.html_url}]
PR = {data.pull_request.html_url if data.pull_request is not None else 'NO PR'}
assignees = {assignees}
labels = {labels}
title = {data.title}
== body
{data.body}
== content
{data.pull_request.diff_url if data.pull_request is not None else 'NO PR'}
            """
            # get_content()
        else:
            # utk prs
            assignees = ', '.join([item.login for item in data.assignees])
            labels = ', '.join([item.name for item in data.labels])
            pr_no = data.number
            username = data.user.login
            content = f"""[{pr_no}][{username}]
created = {data.created_at.ctime()}
updated = {data.updated_at.ctime()}
url = [{data.html_url}]
Issue = {data.issue_url or 'NO ISSUE'}
assignees = {assignees}
labels = {labels}
comments = {data.comments}
url comments = {data.comments_url}
commits = {data.commits}
url commits_url = {data.commits_url}
== body
{data.body}
== content
changed_files = {data.changed_files}
{data.diff_url}
{'*'*10}
{get_content(data.diff_url)}
            """
        return content


    async def handle_entry_click(self, message: EntryClick) -> None:
        # content = f"""
        # category = {message.category}
        # title = {message.title}
        # number = {message.number}
        # """
        syntax = Syntax(
                # content,
                self.issue_pr_content(message),
                lexer='python',
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                # theme="xcode" if message.category=='Issue' else 'inkpot',
                theme = issue_pr_mapping[message.category]['theme'],
            )
        if message.category==issue_pr_mapping['category'][0]:
            await self.issue_editor.update(syntax)
        else:
            await self.pr_editor.update(syntax)


# async 
def git_detail(github_repo='django/django', status='django/django'):
    MyApp.github_repo = github_repo
    MyApp.status = status
    MyApp.run(title="Gitor")
    # lihat source code textual.app.py
    # app = MyApp(title='GiTail')
    # await app.process_messages()

