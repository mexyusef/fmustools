from asyncio import Future, ensure_future
import asyncio
import os, random, subprocess
from textwrap import dedent
from prompt_toolkit import prompt
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.widgets import (
    Button,
    Dialog,
    Label,
    MenuContainer,
    MenuItem,
    SearchToolbar,
    TextArea,
)
from prompt_toolkit.layout.containers import (
    ConditionalContainer,
    Float,
    HSplit,
    VSplit,
    Window,
    WindowAlign,
)
from prompt_toolkit.layout.dimension import D

from schnell.app.dirutils import joinhere, joiner, isfile
from schnell.app.printutils import (
    indah4,
    print_source_code_copy,
    is_source_code,
    print_source_code,
    print_source_code_file,
    print_highlight_query,
    print_highlight_query_file,
    print_source_code_file_with_markdown,
)
from schnell.gui.system.searcher.widgets.actorhandler import actor_handler
from schnell.db.writer_service import process_writer
from schnell.app.fileutils import file_write_timestamped, file_content
from schnell.app.formatutils.markdownutils import (
    print_markdown_content,
    print_markdown_file,
)
from schnell.app.fileutils import file_write, file_prepend, file_append, file_content
from schnell.app.fmus.fileops import insert_at_lines
# print('pgup1')
from schnell.app.llmutils.langchainutils.llms.llm_gemini import invoke_llm_vision_chat_by_screen_capture
# print('pgup2')
from configuration_values import help_file, config_app
from ui.doubleeditor import show_double_editor, Application, append_output
from ui.pager import show_pager
# print('pgup3')
from fpgemini import send_chat_stream, gemini_header
# print('pgup4')
from fpprogress import progress_rainbow
from fmuslib import (
    temp_file_write,
    trypaste,
    run_fmus_for_content,
    run_fmus_for_content_in_thread,
    run_fmus_for_file_in_thread,
    run_fmus_for_file,
    trycopy,
)
# print('pgup5')
# from schnell.app.filemanager.tui_browser import file_browser, inquire_text, inquire_yn, file_browser_pick
from schnell.app.imageutils4 import display_images_from_clipboard
from schnell.app.filemanager.tui_browser import file_browser_pick
from schnell.app.filemanager.survey_browser import file_browser
from schnell.app.inpututils.tkinput import input_text_ctk, input_integer_ctk, input_float_ctk, input_boolean_ctk
from schnell.app.inpututils.survey_input import input_survey_text, input_survey_boolean
from schnell.app.printutils import indah4, print_list_warna, indah3
# print('pgup6')
# from schnell.app.llmutils.langchainutils.agents.role_just_scrape import generate_code
# print('pgup6b')
# print('pgup7')
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\workers\researcher\sample.py
# from schnell.app.llmutils.langchainutils.workers.researcher.sample import run_research, do_research, sync_main_process, wrap_do_research

# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llms\invoker.py
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm, invoke_llm_all
# print('pgup8')
from schnell.app.llmutils.langchainutils.llm_config import all_accounts, invoke_all
# print('pgup9')
from schnell.app.windowsutils import minimize_terminal
# print('pgup10')
from keybinders.common import extract_digit_and_rest, terima_prompt
from keybinders.peta_operasi import peta_operasi
from vendor.survey import survey
# print('pgup11')
# target sebelum apply
# RAG github, youtube, website, google => agent/write file
# copilot di visual studio (groq, gemini, openai)
# opendevin, devika, ... sudah bisa jalan manual (mungkin ini jadi lama)

# teknik, gak bisa minta agent utk nulis file: gak konsisten
# kesulitan juga utk nulis code...mending invoke, ambil content dan write sendiri...

async def run_until_complete_wrapper(query, coro):
    # task = asyncio.create_task(coro(query))
    # await task
    # indah3(task.result(), warna='yellow')
    result = await coro(query)
    indah3(result, warna='yellow')


def run_until_complete(query, coro):
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(coro)
    # asyncio.run(
    #     run_until_complete_wrapper(query, coro)
    # )
    asyncio.create_task(run_until_complete_wrapper(query, coro))

def handle_operasi(llm_name, current_line, kunci, nilai):
    
    # python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\just_implement\role_just_implement.py
    from schnell.app.llmutils.langchainutils.agents.just_implement.role_just_implement import role_just_implement
    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\english\twitter.py
    from schnell.app.llmutils.langchainutils.agents.english.twitter import generate_twitter
    from schnell.app.llmutils.langchainutils.agents.job_advertisement.role_jobdesc_portfolio import role_jobdesc_portfolio
    from schnell.app.llmutils.langchainutils.agents.role_project_skeleton import skeleton_code
    from schnell.app.llmutils.langchainutils.agents.role_just_scrape import generate_code
    from schnell.app.llmutils.langchainutils.agents.role_just_understand import understand_code
    from schnell.app.llmutils.langchainutils.agents.role_unit_tester import unit_test_code
    from schnell.app.llmutils.langchainutils.agents.role_code_critic import critic_code
    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain\_api\module_import.py:92:
    # LangChainDeprecationWarning: Importing load_tools from langchain.agents is deprecated.
    # Please replace deprecated imports:
    # >> from langchain.agents import load_tools
    # with new imports of:
    # >> from langchain_community.agent_toolkits.load_tools import load_tools
    # You can use the langchain cli to **automatically** upgrade many imports. Please see documentation here https://python.langchain.com/v0.2/docs/versions/v0_2/
    # warn_deprecated(
    
    status = 'NOK'
    generate_code_prompt = None

    if kunci == 'p':
        skeleton_code_prompt = current_line
        if not skeleton_code_prompt:
            skeleton_code_prompt = trypaste()
            if not skeleton_code_prompt:
                return status

        res = invoke_llm(skeleton_code_prompt, llm_name=llm_name)
        indah3(res, warna='green')
        status = 'OK'
    elif kunci == 'P':
        skeleton_code_prompt = current_line
        if not skeleton_code_prompt:
            skeleton_code_prompt = trypaste()
            if not skeleton_code_prompt:
                return status

        res = invoke_llm_all(skeleton_code_prompt)
        for k,v in res.items():
            indah4(f"=== {k} ===\n\n{v}\n", warna=random.choice(['green', 'blue', 'cyan', 'yellow', 'magenta', 'red']))
        res_all = '\n'.join(f"=== {k} ===\n\n{v}\n" for k,v in res.items())
        trycopy(res_all)
        status = 'OK'
    elif kunci == '@':
        user_query = trypaste()
        if user_query:
            print('\ninvoke:', user_query)
            res = invoke_llm(user_query, llm_name=llm_name)
            indah3(res, warna='yellow')
            status = 'OK'
    elif kunci == '@@':
        generate_code_prompt = trypaste()
        if generate_code_prompt:
            print('\ngenerate:', generate_code_prompt)
            jumlah, masukan = extract_digit_and_rest(generate_code_prompt)
            if jumlah:
                res = generate_code(masukan, llm_name=llm_name, jumlah=jumlah)
            else:
                res = generate_code(masukan, llm_name=llm_name)

            indah3(res, warna='yellow')
            status = 'OK'
    elif kunci in ['generate']:  # sementara sama dg generate code, nanti prompt bisa punya fungsi sendiri
        generate_code_prompt = current_line
        if generate_code_prompt:
            print('\ngenerate:', generate_code_prompt)
            jumlah, masukan = extract_digit_and_rest(generate_code_prompt)
            if jumlah:
                res = generate_code(masukan, llm_name=llm_name, jumlah=jumlah)
            else:
                res = generate_code(masukan, llm_name=llm_name)

            indah3(res, warna='yellow')
            status = 'OK'
    elif kunci == 'understand':
        understand_code_prompt = current_line
        if not understand_code_prompt:
            understand_code_prompt = trypaste()
            if not understand_code_prompt:
                return status
        jumlah, masukan = extract_digit_and_rest(understand_code_prompt)
        if jumlah:
            res = understand_code(masukan, llm_name=llm_name, jumlah=jumlah)
        else:
            res = understand_code(masukan, llm_name=llm_name)

        indah3(res, warna='yellow')
        status = 'OK'
    elif kunci == 'review':
        review_code_prompt = current_line
        if not review_code_prompt:
            review_code_prompt = trypaste()
            if not review_code_prompt:
                return status
        jumlah, masukan = extract_digit_and_rest(review_code_prompt)
        if jumlah:
            res = critic_code(masukan, llm_name=llm_name, jumlah=jumlah)
        else:
            res = critic_code(masukan, llm_name=llm_name)

        indah3(res, warna='yellow')
        status = 'OK'
    elif kunci == 'test':
        test_code_prompt = current_line
        if not test_code_prompt:
            test_code_prompt = trypaste()
            if not test_code_prompt:
                return status
        jumlah, masukan = extract_digit_and_rest(test_code_prompt)
        if jumlah:
            res = unit_test_code(masukan, llm_name=llm_name, jumlah=jumlah)
        else:
            res = unit_test_code(masukan, llm_name=llm_name)

        indah3(res, warna='yellow')
        status = 'OK'
    elif kunci == 'skeleton':
        skeleton_code_prompt = current_line
        if not skeleton_code_prompt:
            skeleton_code_prompt = trypaste()
            if not skeleton_code_prompt:
                return status
        jumlah, masukan = extract_digit_and_rest(skeleton_code_prompt)
        if jumlah:
            res = skeleton_code(masukan, llm_name=llm_name, jumlah=jumlah)
        else:
            res = skeleton_code(masukan, llm_name=llm_name)

        indah3(res, warna='yellow')
        status = 'OK'
    elif kunci == 'gpt-research':
        user_query = current_line
        if not user_query:
            user_query = trypaste()
            if not user_query:
                return status
        # res = run_research(user_query)
        # indah3(res, warna='yellow')
        # run_until_complete(user_query, do_research)
        # sync_main_process(user_query)
        # wrap_do_research(user_query)
        # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\workers\researcher\sample.py
        os.system("python " + r'C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\workers\researcher\sample.py '+user_query)
        status = 'OK'

    # 'job-desc'  : 'handle upwork job',
    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_project_manager.py

    elif kunci == 'job-desc':
        user_query = current_line
        if not user_query:
            user_query = trypaste()
            if not user_query:
                return status
        # res = run_research(user_query)
        # indah3(res, warna='yellow')
        # run_until_complete(user_query, do_research)
        # sync_main_process(user_query)
        role_jobdesc_portfolio(user_query)
        status = 'OK'

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\job_advertisement\role_jobdesc_portfolio.py
    # 'job-ad'    : 'handle job vacancy',
    elif kunci == 'job-ad':
        user_query = current_line
        if not user_query:
            user_query = trypaste()
            if not user_query:
                return status
        # res = run_research(user_query)
        # indah3(res, warna='yellow')
        # run_until_complete(user_query, do_research)
        # sync_main_process(user_query)
        role_jobdesc_portfolio(user_query)
        status = 'OK'

    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_qa_engineer.py
    # 'document': 'document code (including OPENAPI)',
    elif kunci == 'document':
        pass
    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_implement.py
    # 'project': 'just implement project',
    # python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\just_implement\role_just_implement.py sample of hello world using web framework axum with rust
    elif kunci == 'project':
        user_query = current_line
        if not user_query:
            user_query = trypaste()
            if not user_query:
                return status
        role_just_implement(user_query)
        status = 'OK'

    elif kunci == 'twitter':
        user_query = current_line
        if not user_query:
            user_query = trypaste()
            if not user_query:
                return status
        res = generate_twitter(user_query, llm_name=llm_name)
        indah4('**************************', warna='cyan')
        indah3(res, warna='yellow')
        indah4('**************************', warna='cyan')
        status = 'OK'

    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_blog_author\role_blog_author.py
    # 'blog1': 'generate blog post',
    elif kunci == 'blog1':
        pass
    # 'blog2': 'generate blog post with sample blog and tools',
    elif kunci == 'blog2':
        pass
    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_book_author\buku-create-agent.py
    # 'book1': 'generate book',
    elif kunci == 'book1':
        pass
    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_researcher.py
    # # cls && python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\workers\researcher\sample.py
    # 'research1': 'general researcher about any topic',
    elif kunci == 'research1':
        pass
    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_screenshot2code\role_screenshot2code.py
    # 'vision0': 'website screenshot vision to UI',
    elif kunci == 'vision0':
        pass
    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_problem_solution\role_by_image.py
    # # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_problem_solution\role_problem_solution.py
    # 'vision1': 'online code problem vision to solution',
    elif kunci == 'vision1':
        pass
    # 'you1': 'generate youtube video',
    elif kunci == 'you1':
        pass
    # 'you2': 'summarize youtube video',
    elif kunci == 'you2':
        pass
    # # ini penting sblm kita bisa pede apply kerja, krn perlu info terbaru
    # "rag-urls"  : 'RAG chat with web urls',
    # "rag-dir"   : 'RAG chat with directory',
    # "rag-file"  : 'RAG chat with files',
    # "rag-gh"    : 'RAG chat with github repo',
    # "rag-you"   : 'RAG chat with youtube channels',
    # "rag-db"    : 'RAG chat with database (rdbms, nosql)',

    # 'cv': 'generate cv',
    elif kunci == 'cv':
        pass
    # 'news': 'latest news',
    elif kunci == 'news':
        pass
    # 'sports': 'latest sports',
    elif kunci == 'sports':
        pass
    # 'politics': 'latest politics',
    elif kunci == 'politics':
        pass
    # 'economy': 'latest economy',
    elif kunci == 'economy':
        pass
    # 'tech': 'latest technology',
    elif kunci == 'tech':
        pass
    # 'science': 'latest science',
    elif kunci == 'science':
        pass
    # 'devin1': 'generate with opendevin',
    elif kunci == 'devin1':
        pass
    # 'devin2': 'generate with devika',
    elif kunci == 'devin2':
        pass
    # 'agent1': 'generate crewai scenario',
    elif kunci == 'agent1':
        pass
    # 'agent2': 'generate 2 agents communicating',
    elif kunci == 'agent2':
        pass
    # 'agent3': 'generate 3 agents communicating',
    elif kunci == 'agent3':
        pass
    return status


# C:\work\ciledug\ciledug\fmusperintah\fpsurvey.py
def pilih_operasi(llm_name, current_line):
    options = list(peta_operasi.values())
    # Ask the user to select an item
    index = survey.routines.select('Select operation: ',
        options=options,
        focus_mark='👉 ',
        evade_color=survey.colors.basic('yellow'))
    selection = options[index]
    for k,v in peta_operasi.items():
        if selection == v:
            return handle_operasi(llm_name, current_line, k, v)


def bind_pageup(bindings, repl):  # aktifkan text-area, text-area-editor
    # aktifkan text-area (prev=aktifkan completer -> sama dengan tab dll)
    @bindings.add("pageup", "pageup")  # text-area kiri
    def _(event):
        # jk text_area gak aktif, maka keluar
        if not config_app["show_textarea"]:
            indah4("Text area tidak aktif (gunakan ctrl + _ utk toggle)", warna="blue")
            return
        try:
            if not config_app["text_area_focused"]:  # mari fokus ke textarea
                event.app.layout.focus(repl.session.text_area.window)
                config_app["text_area_focused"] = True
                config_app["enable_page_navigation_bindings"] = True
            else:
                # C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\layout\layout.py
                event.app.layout.focus(repl.session.default_buffer_window)
                config_app["text_area_focused"] = False
                config_app["enable_page_navigation_bindings"] = False
        except Exception as gagal:
            indah4(str(gagal), warna="red")
    
    # fokuskan text-area-editor jika aktif
    @bindings.add("pageup", "pagedown")  # text-area-editor kanan
    def _(event):
        if not config_app["show_textarea_editor"]:
            indah4(
                "Text area editor tidak aktif (gunakan ctrl + _ utk toggle text-area, show_textarea_editor=True utk text-area-editor)",
                warna="blue",
            )
            return
        try:
            # config_app['show_textarea_editor'] = not config_app['show_textarea_editor']
            if not config_app["text_area_editor_focused"]:
                event.app.layout.focus(repl.session.text_area_editor.window)
                config_app["text_area_editor_focused"] = True
            else:
                # C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\layout\layout.py
                # default_buffer_window ini ke prompt kan ya, bukan text_area
                event.app.layout.focus(repl.session.default_buffer_window)
                config_app["text_area_editor_focused"] = False
            # repl.refresh_completer()
            # terima_prompt(event)
        except Exception as gagal:
            indah4(str(gagal), warna="red")

    # C:\work\ciledug\ciledug\fmusperintah\fpsurvey.py
    # ikuti gaya file_browser
    # options = ["@", "generate_code", "understand_code", "critique_improve_refactor_code", "unit_test", ]

    @bindings.add("pageup", "left")  # prompt dg active model
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        if not current_line:
            current_line = trypaste()
            # if not current_line:
            #     return status
        if current_line:
            print()
            result = invoke_llm(current_line, all_accounts['active'])
            indah3(result, warna='yellow')
        else:
            indah4("No prompt.", warna='red')

    @bindings.add("pageup", "right")  # prompt dg all models
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        if not current_line:
            current_line = trypaste()
            # if not current_line:
            #     return status
        if current_line:
            print()
            # result = invoke_llm(current_line, all_accounts['active'])
            # indah3(result, warna='yellow')
            res = invoke_llm_all(current_line)
            for k,v in res.items():
                indah4(f"=== {k} ===\n\n{v}\n", warna=random.choice(['green', 'blue', 'cyan', 'yellow', 'magenta', 'red']))
            res_all = '\n'.join(f"=== {k} ===\n\n{v}\n" for k,v in res.items())
            trycopy(res_all)
        else:
            indah4("No prompt.", warna='red')

    @bindings.add("pageup", "escape")  # ganti active
    def _(event):
        # current_line = event.app.current_buffer.text.strip()
        # res = pilih_operasi('gemini', current_line)
        # if res == 'OK':
        #     terima_prompt(event)
        active_account = all_accounts["active"]
        options = list(invoke_all.keys())
        options.remove(active_account)
        options.insert(0, active_account)

        index = survey.routines.select('Select active model: ',
            options=options,
            focus_mark='👉 ',
            evade_color=survey.colors.basic('yellow'))
        selection = options[index]
        if selection in invoke_all:
            all_accounts["active"] = selection
        indah4(f'Selection: {selection}', warna='cyan')

    @bindings.add("pageup", "1")  # vision llm dg prompt menggunakan gemini-pro-vision
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        if not current_line:
            current_line = trypaste()
        if current_line:
            print()
            # result = invoke_llm(current_line, all_accounts['active'])
            # indah3(result, warna='yellow')
            # "gemini-pro-vision"
            # "gemini-1.5-flash-latest"
            result = invoke_llm_vision_chat_by_screen_capture(
                current_line,
                base_folder=r'C:\Users\usef\Desktop\Screenshots\llms',
                wait_alert=False,
                model="gemini-pro-vision"
            )
            indah3(result, warna='yellow')
        else:
            indah4("No prompt.", warna='red')

    @bindings.add("pageup", "2")  # vision llm dg prompt menggunakan gemini-flash
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        if not current_line:
            current_line = trypaste()
        if current_line:
            print()
            # result = invoke_llm(current_line, all_accounts['active'])
            # indah3(result, warna='yellow')
            # "gemini-pro-vision"
            # "gemini-1.5-flash-latest"
            result = invoke_llm_vision_chat_by_screen_capture(
                current_line,
                base_folder=r'C:\Users\usef\Desktop\Screenshots\llms',
                wait_alert=False,
                # model="gemini-1.5-flash-latest",
                model="gemini-1.5-flash",
            )
            indah3(result, warna='yellow')
        else:
            indah4("No prompt.", warna='red')

    @bindings.add("pageup", "3")  # vision llm dg prompt menggunakan openai gpt-4o
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        if not current_line:
            current_line = trypaste()
        if current_line:
            from schnell.app.llmutils.langchainutils.llms.llm_openai import invoke_llm_vision_chat_by_screen_capture as openai_vision
            print()
            # result = invoke_llm(current_line, all_accounts['active'])
            # indah3(result, warna='yellow')
            result = openai_vision(
                current_line,
                base_folder=r'C:\Users\usef\Desktop\Screenshots\llms'
            )
            indah3(result, warna='yellow')
        else:
            indah4("No prompt.", warna='red')

    # number: 0-9
    # letter: a-z
    # f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12,
    # escape,
    # s-escape,
    # s-delete, s-tab
    # s-left, s-right, s-up, s-down
    # left, right, up, down
    # home, end, delete, pageup, pagedown, insert

    @bindings.add("pageup", "s-up")  # vision llm utk custom prompt = test
    def _(event):
        # current_line = event.app.current_buffer.text.strip()
        # current_line = dedent("""
        # The following image contain a coding, data science, or machine learning problem where you might be requested to either
        # - fill the blanks
        # or
        # - select the correct answer(s) from multiple choice question
        # according to the instruction given in the image.

        # First, please give me your description of the content of the image.
        # Last, you try to give solution the problem contained in the image.
        # """)
        from .pageup_prompt import online_test_prompt
        # print()
        # result = invoke_llm(current_line, all_accounts['active'])
        # indah3(result, warna='yellow')
        # "gemini-pro-vision"
        # "gemini-1.5-flash-latest"
        result = invoke_llm_vision_chat_by_screen_capture(
            online_test_prompt,
            base_folder=r'C:\Users\usef\Desktop\Screenshots\llms',
            wait_alert=False,
            # model="gemini-pro-vision"  # pake active llm
            )
        indah3(result, warna='yellow')


    @bindings.add("pageup", "s-down")  # vision llm utk custom prompt = test via langchain
    def _(event):
        # bedanya dg pgup s-up, di sini kita coba ambil deskripsi dari capture image
        # feed kan ke beberapa llm sekaligus, secara paralel
        from .pageup_prompt import online_test_prompt
        result = invoke_llm_vision_chat_by_screen_capture(
            online_test_prompt,
            base_folder=r'C:\Users\usef\Desktop\Screenshots\llms',
            wait_alert=False,
            # model="gemini-pro-vision"  # pake active llm
            )
        indah3(result, warna='yellow')


    @bindings.add("pageup", "c")  # clarify
    def _(event):
        pass

    @bindings.add("pageup", "g")  # gemini*
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        res = pilih_operasi('gemini', current_line)
        if res == 'OK':
            terima_prompt(event)

    @bindings.add("pageup", "h")  # cohere*
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        res = pilih_operasi('cohere', current_line)
        if res == 'OK':
            terima_prompt(event)

    @bindings.add("pageup", "n")  # nvidia
    def _(event):
        pass

    @bindings.add("pageup", "o")  # openai*
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        res = pilih_operasi('openai', current_line)
        if res == 'OK':
            terima_prompt(event)

    @bindings.add("pageup", "q")  # groq*
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        res = pilih_operasi('groq', current_line)
        if res == 'OK':
            terima_prompt(event)

    @bindings.add("pageup", "r")  # replicate
    def _(event):
        pass

    @bindings.add("pageup", "s")  # goose
    def _(event):
        pass

    @bindings.add("pageup", "t")  # together*
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        res = pilih_operasi('together', current_line)
        if res == 'OK':
            terima_prompt(event)

    @bindings.add("pageup", "u")  # huggingface*
    def _(event):
        current_line = event.app.current_buffer.text.strip()
        res = pilih_operasi('huggingface', current_line)
        if res == 'OK':
            # terima_prompt(event)
            # biar masuk history
            print()
