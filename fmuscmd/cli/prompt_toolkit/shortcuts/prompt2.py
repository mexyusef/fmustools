"""
Line editing functionality.
---------------------------

This provides a UI for a line input, similar to GNU Readline, libedit and
linenoise.

Either call the `prompt` function for every line input. Or create an instance
of the :class:`.PromptSession` class and call the `prompt` method from that
class. In the second case, we'll have a 'session' that keeps all the state like
the history in between several calls.

There is a lot of overlap between the arguments taken by the `prompt` function
and the `PromptSession` (like `completer`, `style`, etcetera). There we have
the freedom to decide which settings we want for the whole 'session', and which
we want for an individual `prompt`.

Example::

        # Simple `prompt` call.
        result = prompt('Say something: ')

        # Using a 'session'.
        s = PromptSession()
        result = s.prompt('Say something: ')
"""
from __future__ import annotations

from asyncio import get_running_loop
from contextlib import contextmanager
from enum import Enum
from functools import partial
from typing import TYPE_CHECKING, Callable, Generic, Iterator, TypeVar, Union, cast

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.auto_suggest import AutoSuggest, DynamicAutoSuggest
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.clipboard import Clipboard, DynamicClipboard, InMemoryClipboard
from prompt_toolkit.completion import Completer, DynamicCompleter, ThreadedCompleter
from prompt_toolkit.cursor_shapes import (
    AnyCursorShapeConfig,
    CursorShapeConfig,
    DynamicCursorShapeConfig,
)
from prompt_toolkit.document import Document
from prompt_toolkit.enums import DEFAULT_BUFFER, SEARCH_BUFFER, EditingMode
from prompt_toolkit.eventloop import InputHook
from prompt_toolkit.filters import (
    Condition,
    FilterOrBool,
    has_arg,
    has_focus,
    is_done,
    is_true,
    renderer_height_is_known,
    to_filter,
)
from prompt_toolkit.formatted_text import (
    AnyFormattedText,
    StyleAndTextTuples,
    fragment_list_to_text,
    merge_formatted_text,
    to_formatted_text,
)
from prompt_toolkit.history import History, InMemoryHistory
from prompt_toolkit.input.base import Input
from prompt_toolkit.key_binding.bindings.auto_suggest import load_auto_suggest_bindings
from prompt_toolkit.key_binding.bindings.completion import (
    display_completions_like_readline,
)
from prompt_toolkit.key_binding.bindings.open_in_editor import (
    load_open_in_editor_bindings,
)
from prompt_toolkit.key_binding.key_bindings import (
    ConditionalKeyBindings,
    DynamicKeyBindings,
    KeyBindings,
    KeyBindingsBase,
    merge_key_bindings,
)
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout import Float, FloatContainer, HSplit, VSplit, Window
from prompt_toolkit.layout.containers import ConditionalContainer, WindowAlign
from prompt_toolkit.layout.controls import (
    BufferControl,
    FormattedTextControl,
    SearchBufferControl,
)
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.menus import CompletionsMenu, MultiColumnCompletionsMenu
from prompt_toolkit.layout.processors import (
    AfterInput,
    AppendAutoSuggestion,
    ConditionalProcessor,
    DisplayMultipleCursors,
    DynamicProcessor,
    HighlightIncrementalSearchProcessor,
    HighlightSelectionProcessor,
    PasswordProcessor,
    Processor,
    TabsProcessor,
    ReverseSearchProcessor,
    merge_processors,
)
from prompt_toolkit.layout.utils import explode_text_fragments
from prompt_toolkit.lexers import DynamicLexer, Lexer
from prompt_toolkit.output import ColorDepth, DummyOutput, Output
from prompt_toolkit.styles import (
    BaseStyle,
    ConditionalStyleTransformation,
    DynamicStyle,
    DynamicStyleTransformation,
    StyleTransformation,
    SwapLightAndDarkStyleTransformation,
    merge_style_transformations,
)
from prompt_toolkit.utils import (
    get_cwidth,
    is_dumb_terminal,
    suspend_to_background_supported,
    to_str,
)
from prompt_toolkit.validation import DynamicValidator, Validator
from prompt_toolkit.widgets.toolbars import (
    SearchToolbar,
    SystemToolbar,
    ValidationToolbar,    
)

from prompt_toolkit.widgets import Button, ProgressBar, TextArea
from prompt_toolkit.layout import ScrollablePane
from prompt_toolkit.lexers import PygmentsLexer

from pygments.lexers.markup import MarkdownLexer
from pygments.lexers.html import HtmlLexer
# C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\pygments\lexers\python.py
from pygments.lexers.python import PythonLexer
from pygments.lexers.shell import (
    BashLexer,
    BashSessionLexer,
    PowerShellLexer,
    PowerShellSessionLexer,
    FishShellLexer,
    ExeclineLexer,
)

from .prompt import (
    _split_multiline_prompt,
    _T,
    _StyleAndTextTuplesCallable,
    _RPrompt,
    CompleteStyle,
    PromptContinuationText,
)
class PromptSession2(Generic[_T]):
    """
    """

    _fields = (
        "message",
        "lexer",
        "completer",
        "complete_in_thread",
        "is_password",
        "editing_mode",
        "key_bindings",
        "is_password",
        "bottom_toolbar",
        "style",
        "style_transformation",
        "swap_light_and_dark_colors",
        "color_depth",
        "cursor",
        "include_default_pygments_style",
        "rprompt",
        "multiline",
        "prompt_continuation",
        "wrap_lines",
        "enable_history_search",
        "search_ignore_case",
        "complete_while_typing",
        "validate_while_typing",
        "complete_style",
        "mouse_support",
        "auto_suggest",
        "clipboard",
        "validator",
        "refresh_interval",
        "input_processors",
        "placeholder",
        "enable_system_prompt",
        "enable_suspend",
        "enable_open_in_editor",
        "reserve_space_for_menu",
        "tempfile_suffix",
        "tempfile",
    )

    def button_clicked(self, which):
        if which==1:
            self.button1.text = '1 Dipencet'
        elif which==2:
            self.button2.text = '2 Dipencet'
        elif which==3:
            self.button3.text = '3 Dipencet'
    def __init__(
        self,
        message: AnyFormattedText = "",
        *,
        multiline: FilterOrBool = False,
        wrap_lines: FilterOrBool = True,
        is_password: FilterOrBool = False,
        vi_mode: bool = False,
        editing_mode: EditingMode = EditingMode.EMACS,
        complete_while_typing: FilterOrBool = True,
        validate_while_typing: FilterOrBool = True,
        enable_history_search: FilterOrBool = False,
        search_ignore_case: FilterOrBool = False,
        lexer: Lexer | None = None,
        enable_system_prompt: FilterOrBool = False,
        enable_suspend: FilterOrBool = False,
        enable_open_in_editor: FilterOrBool = False,
        validator: Validator | None = None,
        completer: Completer | None = None,
        complete_in_thread: bool = False,
        reserve_space_for_menu: int = 8,
        complete_style: CompleteStyle = CompleteStyle.COLUMN,
        auto_suggest: AutoSuggest | None = None,
        style: BaseStyle | None = None,
        style_transformation: StyleTransformation | None = None,
        swap_light_and_dark_colors: FilterOrBool = False,
        color_depth: ColorDepth | None = None,
        cursor: AnyCursorShapeConfig = None,
        include_default_pygments_style: FilterOrBool = True,
        history: History | None = None,
        clipboard: Clipboard | None = None,
        prompt_continuation: PromptContinuationText | None = None,
        rprompt: AnyFormattedText = None,
        bottom_toolbar: AnyFormattedText = None,
        mouse_support: FilterOrBool = False,
        input_processors: list[Processor] | None = None,
        placeholder: AnyFormattedText | None = None,
        key_bindings: KeyBindingsBase | None = None,
        erase_when_done: bool = False,
        tempfile_suffix: str | Callable[[], str] | None = ".txt",
        tempfile: str | Callable[[], str] | None = None,
        refresh_interval: float = 0,
        input: Input | None = None,
        output: Output | None = None,
        text_area_height: int = 7,
        text_area_style: str = "bg:#ansibrightyellow",
        text_area_lexer: str = "bash",
        show_textarea: bool = True,
        text_area_editor_width: int = 10,
        text_area_editor_style: str = "bg:#ansibrightyellow",
        text_area_editor_lexer: str = "fish",
        show_textarea_editor: bool = True,
        show_editor_toolbar: bool = True,
        enable_page_navigation_bindings: bool = False,
        progress_day: int = 25,
        progress_hour: int = 75,
    ) -> None:
        history = history or InMemoryHistory()
        clipboard = clipboard or InMemoryClipboard()

        # Ensure backwards-compatibility, when `vi_mode` is passed.
        if vi_mode:
            editing_mode = EditingMode.VI

        # Store all settings in this class.
        self._input = input
        self._output = output

        self.text_area_height = text_area_height
        self.text_area_style = text_area_style
        self.text_area_lexer = text_area_lexer
        # self.show_textarea: bool = False
        self.show_textarea: bool = show_textarea
        self.textarea_content: str = ''

        # self.enable_page_navigation_bindings: bool = enable_page_navigation_bindings

        self.text_area_editor_width = text_area_editor_width
        self.text_area_editor_style = text_area_editor_style
        self.text_area_editor_lexer = text_area_editor_lexer
        self.show_textarea_editor = show_textarea_editor

        self.show_editor_toolbar = show_editor_toolbar
        # self.progress_editor_percent = 25
        self.progress_bar_day = ProgressBar(progress_day)
        # self.progress_bar_day.percentage = progress_day
        self.progress_bar_hour = ProgressBar(progress_hour)
        # self.progress_bar_hour.percentage = progress_hour
        self.button1 = Button(
            self.progress_bar_day.label.text,
            left_symbol='',
            right_symbol='',
            width=4,
            handler=lambda: self.button_clicked(1))

        self.button2 = Button(
            "fmush",
            left_symbol='▶️',
            right_symbol='◀️',
            # style='bg:ansiblue ansirightyellow',
            handler=lambda: self.button_clicked(2))

        # self.button2.window.style = 'bg:ansiblue ansirightyellow'

        self.button3 = Button(
            self.progress_bar_hour.label.text,
            left_symbol='',
            right_symbol='',
            width=4,
            handler=lambda: self.button_clicked(3))

        # Store attributes.
        # (All except 'editing_mode'.)
        self.message = message
        self.lexer = lexer
        self.completer = completer
        self.complete_in_thread = complete_in_thread
        self.is_password = is_password
        self.key_bindings = key_bindings
        self.bottom_toolbar = bottom_toolbar
        self.style = style
        self.style_transformation = style_transformation
        self.swap_light_and_dark_colors = swap_light_and_dark_colors
        self.color_depth = color_depth
        self.cursor = cursor
        self.include_default_pygments_style = include_default_pygments_style
        self.rprompt = rprompt
        self.multiline = multiline
        self.prompt_continuation = prompt_continuation
        self.wrap_lines = wrap_lines
        self.enable_history_search = enable_history_search
        self.search_ignore_case = search_ignore_case
        self.complete_while_typing = complete_while_typing
        self.validate_while_typing = validate_while_typing
        self.complete_style = complete_style
        self.mouse_support = mouse_support
        self.auto_suggest = auto_suggest
        self.clipboard = clipboard
        self.validator = validator
        self.refresh_interval = refresh_interval
        self.input_processors = input_processors
        self.placeholder = placeholder
        self.enable_system_prompt = enable_system_prompt
        self.enable_suspend = enable_suspend
        self.enable_open_in_editor = enable_open_in_editor
        self.reserve_space_for_menu = reserve_space_for_menu
        self.tempfile_suffix = tempfile_suffix
        self.tempfile = tempfile

        # Create buffers, layout and Application.
        self.history = history
        self.default_buffer = self._create_default_buffer()
        self.search_buffer = self._create_search_buffer()
        self.layout = self._create_layout()
        self.app = self._create_application(
            editing_mode,
            erase_when_done,
            enable_page_navigation_bindings
        )

    def _dyncond(self, attr_name: str) -> Condition:
        """
        Dynamically take this setting from this 'PromptSession' class.
        `attr_name` represents an attribute name of this class. Its value
        can either be a boolean or a `Filter`.

        This returns something that can be used as either a `Filter`
        or `Filter`.
        """

        @Condition
        def dynamic() -> bool:
            value = cast(FilterOrBool, getattr(self, attr_name))
            return to_filter(value)()

        return dynamic

    def _create_default_buffer(self) -> Buffer:
        """
        Create and return the default input buffer.
        """
        dyncond = self._dyncond

        # Create buffers list.
        def accept(buff: Buffer) -> bool:
            """Accept the content of the default buffer. This is called when
            the validation succeeds."""
            cast(Application[str], get_app()).exit(result=buff.document.text)
            return True  # Keep text, we call 'reset' later on.

        return Buffer(
            name=DEFAULT_BUFFER,
            # Make sure that complete_while_typing is disabled when
            # enable_history_search is enabled. (First convert to Filter,
            # to avoid doing bitwise operations on bool objects.)
            complete_while_typing=Condition(
                lambda: is_true(self.complete_while_typing)
                and not is_true(self.enable_history_search)
                and self.complete_style != CompleteStyle.READLINE_LIKE
            ),
            validate_while_typing=dyncond("validate_while_typing"),
            enable_history_search=dyncond("enable_history_search"),
            validator=DynamicValidator(lambda: self.validator),
            completer=DynamicCompleter(
                lambda: ThreadedCompleter(self.completer)
                if self.complete_in_thread and self.completer
                else self.completer
            ),
            history=self.history,
            auto_suggest=DynamicAutoSuggest(lambda: self.auto_suggest),
            accept_handler=accept,
            tempfile_suffix=lambda: to_str(self.tempfile_suffix or ""),
            tempfile=lambda: to_str(self.tempfile or ""),
        )

    def _create_search_buffer(self) -> Buffer:
        return Buffer(name=SEARCH_BUFFER)

    def _create_layout(self) -> Layout:
        """
        Create `Layout` for this prompt.
        """
        dyncond = self._dyncond

        # Create functions that will dynamically split the prompt. (If we have
        # a multiline prompt.)
        (
            has_before_fragments,
            get_prompt_text_1,
            get_prompt_text_2,
        ) = _split_multiline_prompt(self._get_prompt)

        default_buffer = self.default_buffer
        search_buffer = self.search_buffer

        # Create processors list.
        @Condition
        def display_placeholder() -> bool:
            return self.placeholder is not None and self.default_buffer.text == ""

        all_input_processors = [
            HighlightIncrementalSearchProcessor(),
            HighlightSelectionProcessor(),
            ConditionalProcessor(
                AppendAutoSuggestion(), has_focus(default_buffer) & ~is_done
            ),
            ConditionalProcessor(PasswordProcessor(), dyncond("is_password")),
            DisplayMultipleCursors(),
            # Users can insert processors here.
            DynamicProcessor(lambda: merge_processors(self.input_processors or [])),
            ConditionalProcessor(
                AfterInput(lambda: self.placeholder),
                filter=display_placeholder,
            ),
        ]

        # Create bottom toolbars.
        bottom_toolbar = ConditionalContainer(
            Window(
                FormattedTextControl(
                    lambda: self.bottom_toolbar, style="class:bottom-toolbar.text"
                ),
                style="class:bottom-toolbar",
                dont_extend_height=True,
                height=Dimension(min=1),
            ),
            filter=Condition(lambda: self.bottom_toolbar is not None)
            & ~is_done
            & renderer_height_is_known,
        )

        search_toolbar = SearchToolbar(
            search_buffer, ignore_case=dyncond("search_ignore_case")
        )

        search_buffer_control = SearchBufferControl(
            buffer=search_buffer,
            input_processors=[ReverseSearchProcessor()],
            ignore_case=dyncond("search_ignore_case"),
        )

        system_toolbar = SystemToolbar(
            enable_global_bindings=dyncond("enable_system_prompt")
        )

        def get_search_buffer_control() -> SearchBufferControl:
            "Return the UIControl to be focused when searching start."
            if is_true(self.multiline):
                return search_toolbar.control
            else:
                return search_buffer_control

        default_buffer_control = BufferControl(
            buffer=default_buffer,
            search_buffer_control=get_search_buffer_control,
            input_processors=all_input_processors,
            include_default_input_processors=False,
            lexer=DynamicLexer(lambda: self.lexer),
            preview_search=True,
        )

        self.default_buffer_window = Window(
            default_buffer_control,
            height=self._get_default_buffer_control_height,
            get_line_prefix=partial(
                self._get_line_prefix, get_prompt_text_2=get_prompt_text_2
            ),
            wrap_lines=dyncond("wrap_lines"),
        )

        @Condition
        def multi_column_complete_style() -> bool:
            return self.complete_style == CompleteStyle.MULTI_COLUMN

        self.text_area = TextArea(
            text=self.textarea_content,
            # read_only=True,
            scrollbar=True,
            line_numbers=True,
            # height=10,
            height=self.text_area_height,
            style=self.text_area_style,
            # search_field=search_field,
            # from pygments.lexers import guess_lexer, get_lexer_for_filename, get_lexer_by_name
            # default_lexer = guess_lexer(content)
            # lexer=DynamicLexer(
            #     lambda: PygmentsLexer.from_filename(
            #         ApplicationState.current_path or ".txt", sync_from_start=False
            #     )
            # ),
            # C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\layout\processors.py
            # input_processors=[TabsProcessor],
            focus_on_click=True,
            lexer=PygmentsLexer(
                PythonLexer 
                    if self.text_area_lexer=='python'
                    else (
                        MarkdownLexer
                            if self.text_area_lexer=='markdown'
                            else (HtmlLexer if self.text_area_lexer=='html' else (
                                BashLexer if self.text_area_lexer=='bash' else (
                                    PowerShellLexer if self.text_area_lexer=='psh' else (
                                        FishShellLexer if self.text_area_lexer=='fish' else ExeclineLexer
                                    )
                                )
                            ))
                    )
            ),
            # lexer=PygmentsLexer.guess_lexer(self.textarea_content),
        )
        self.text_area_editor = TextArea(
            scrollbar=True,
            line_numbers=True,
            # width=self.text_area_editor_width,
            style=self.text_area_editor_style,
            lexer=PygmentsLexer(
                PythonLexer 
                    if self.text_area_editor_lexer=='python'
                    else (
                        MarkdownLexer
                            if self.text_area_editor_lexer=='markdown'
                            else (HtmlLexer if self.text_area_editor_lexer=='html' else (
                                BashLexer if self.text_area_editor_lexer=='bash' else (
                                    PowerShellLexer if self.text_area_editor_lexer=='psh' else (
                                        FishShellLexer if self.text_area_editor_lexer=='fish' else ExeclineLexer
                                    )
                                )
                            ))
                    )
            ),
        )


        self.prompt_control = FormattedTextControl(get_prompt_text_1)
        self.prompt_window = Window(
            self.prompt_control,
            dont_extend_height=True,
        )

        # Build the layout.
        self.root_container0 = HSplit(
            [
                # ke depan kita kasih MenuContainer dll
                ConditionalContainer(
                    HSplit([
                        ConditionalContainer(
                            VSplit([
                                self.button1,
                                self.progress_bar_day,
                                self.button2,
                                self.progress_bar_hour,
                                self.button3,
                            ]),
                            filter=Condition(lambda: self.show_editor_toolbar)
                        ),
                        VSplit([
                            self.text_area,
                            ConditionalContainer(
                                self.text_area_editor,
                                filter=Condition(lambda: self.show_textarea_editor)
                            ),
                        ]),
                    ]),
                    # ScrollablePane(self.text_area),
                    # ScrollablePane(HSplit([self.text_area])),
                    filter=Condition(lambda: self.show_textarea)
                    # dyncond("show_textarea") & ~is_done
                ),
                # The main input, with completion menus floating on top of it.
                FloatContainer(
                    HSplit(
                        [
                            ConditionalContainer(
                                self.prompt_window,
                                Condition(has_before_fragments),
                            ),
                            ConditionalContainer(
                                self.default_buffer_window,
                                Condition(
                                    lambda: get_app().layout.current_control
                                    != search_buffer_control
                                ),
                            ),
                            ConditionalContainer(
                                Window(search_buffer_control),
                                Condition(
                                    lambda: get_app().layout.current_control
                                    == search_buffer_control
                                ),
                            ),
                        ]
                    ),
                    [
                        # Completion menus.
                        # NOTE: Especially the multi-column menu needs to be
                        #       transparent, because the shape is not always
                        #       rectangular due to the meta-text below the menu.
                        Float(
                            xcursor=True,
                            ycursor=True,
                            transparent=True,
                            content=CompletionsMenu(
                                max_height=16,
                                scroll_offset=1,
                                extra_filter=has_focus(default_buffer)
                                & ~multi_column_complete_style,
                            ),
                        ),
                        Float(
                            xcursor=True,
                            ycursor=True,
                            transparent=True,
                            content=MultiColumnCompletionsMenu(
                                show_meta=True,
                                extra_filter=has_focus(default_buffer)
                                & multi_column_complete_style,
                            ),
                        ),
                        # The right prompt.
                        Float(
                            right=0,
                            top=0,
                            hide_when_covering_content=True,
                            content=_RPrompt(lambda: self.rprompt),
                        ),
                    ],
                ),
                ConditionalContainer(ValidationToolbar(), filter=~is_done),
                ConditionalContainer(
                    system_toolbar, dyncond("enable_system_prompt") & ~is_done
                ),
                # In multiline mode, we use two toolbars for 'arg' and 'search'.
                ConditionalContainer(
                    Window(FormattedTextControl(self._get_arg_text), height=1),
                    dyncond("multiline") & has_arg,
                ),
                ConditionalContainer(search_toolbar, dyncond("multiline") & ~is_done),
                bottom_toolbar,
            ]
        )

        # utk dukung message box kita wrap self.root_container0
        self.root_container = FloatContainer(
            self.root_container0,
            floats=[
            # err...ini bikin double menu completion
            #     Float(
            #         xcursor=True,
            #         ycursor=True,
            #         content=CompletionsMenu(max_height=16, scroll_offset=1),
            #     ),
            ],
        )

        return Layout(self.root_container, self.default_buffer_window)

    def _create_application(
        self, editing_mode: EditingMode, erase_when_done: bool, enable_page_navigation_bindings: bool
    ) -> Application[_T]:
        """
        Create the `Application` object.
        """
        dyncond = self._dyncond

        # Default key bindings.
        auto_suggest_bindings = load_auto_suggest_bindings()
        open_in_editor_bindings = load_open_in_editor_bindings()
        prompt_bindings = self._create_prompt_bindings()

        # Create application
        application: Application[_T] = Application(
            layout=self.layout,
            style=DynamicStyle(lambda: self.style),
            style_transformation=merge_style_transformations(
                [
                    DynamicStyleTransformation(lambda: self.style_transformation),
                    ConditionalStyleTransformation(
                        SwapLightAndDarkStyleTransformation(),
                        dyncond("swap_light_and_dark_colors"),
                    ),
                ]
            ),
            include_default_pygments_style=dyncond("include_default_pygments_style"),
            clipboard=DynamicClipboard(lambda: self.clipboard),
            key_bindings=merge_key_bindings(
                [
                    merge_key_bindings(
                        [
                            auto_suggest_bindings,
                            ConditionalKeyBindings(
                                open_in_editor_bindings,
                                dyncond("enable_open_in_editor")
                                & has_focus(DEFAULT_BUFFER),
                            ),
                            prompt_bindings,
                        ]
                    ),
                    DynamicKeyBindings(lambda: self.key_bindings),
                ]
            ),
            mouse_support=dyncond("mouse_support"),
            editing_mode=editing_mode,
            erase_when_done=erase_when_done,
            reverse_vi_search_direction=True,
            color_depth=lambda: self.color_depth,
            cursor=DynamicCursorShapeConfig(lambda: self.cursor),
            refresh_interval=self.refresh_interval,
            input=self._input,
            output=self._output,
            # waktu aktifkan textarea kiri, kita enablekan
            enable_page_navigation_bindings=enable_page_navigation_bindings,
        )

        # During render time, make sure that we focus the right search control
        # (if we are searching). - This could be useful if people make the
        # 'multiline' property dynamic.
        """
        def on_render(app):
            multiline = is_true(self.multiline)
            current_control = app.layout.current_control

            if multiline:
                if current_control == search_buffer_control:
                    app.layout.current_control = search_toolbar.control
                    app.invalidate()
            else:
                if current_control == search_toolbar.control:
                    app.layout.current_control = search_buffer_control
                    app.invalidate()

        app.on_render += on_render
        """

        return application

    def _create_prompt_bindings(self) -> KeyBindings:
        """
        Create the KeyBindings for a prompt application.
        """
        kb = KeyBindings()
        handle = kb.add
        default_focused = has_focus(DEFAULT_BUFFER)

        @Condition
        def do_accept() -> bool:
            return not is_true(self.multiline) and self.app.layout.has_focus(
                DEFAULT_BUFFER
            )

        @handle("enter", filter=do_accept & default_focused)
        def _accept_input(event: E) -> None:
            "Accept input when enter has been pressed."
            self.default_buffer.validate_and_handle()

        @Condition
        def readline_complete_style() -> bool:
            return self.complete_style == CompleteStyle.READLINE_LIKE

        @handle("tab", filter=readline_complete_style & default_focused)
        def _complete_like_readline(event: E) -> None:
            "Display completions (like Readline)."
            display_completions_like_readline(event)

        @handle("c-c", filter=default_focused)
        @handle("<sigint>")
        def _keyboard_interrupt(event: E) -> None:
            "Abort when Control-C has been pressed."
            event.app.exit(exception=KeyboardInterrupt, style="class:aborting")

        @Condition
        def ctrl_d_condition() -> bool:
            """Ctrl-D binding is only active when the default buffer is selected
            and empty."""
            app = get_app()
            return (
                app.current_buffer.name == DEFAULT_BUFFER
                and not app.current_buffer.text
            )

        @handle("c-d", filter=ctrl_d_condition & default_focused)
        def _eof(event: E) -> None:
            "Exit when Control-D has been pressed."
            event.app.exit(exception=EOFError, style="class:exiting")

        suspend_supported = Condition(suspend_to_background_supported)

        @Condition
        def enable_suspend() -> bool:
            return to_filter(self.enable_suspend)()

        @handle("c-z", filter=suspend_supported & enable_suspend)
        def _suspend(event: E) -> None:
            """
            Suspend process to background.
            """
            event.app.suspend_to_background()

        return kb

    def prompt(
        self,
        # When any of these arguments are passed, this value is overwritten
        # in this PromptSession.
        message: AnyFormattedText | None = None,
        # `message` should go first, because people call it as
        # positional argument.
        *,
        editing_mode: EditingMode | None = None,
        refresh_interval: float | None = None,
        vi_mode: bool | None = None,
        lexer: Lexer | None = None,
        completer: Completer | None = None,
        complete_in_thread: bool | None = None,
        is_password: bool | None = None,
        key_bindings: KeyBindingsBase | None = None,
        bottom_toolbar: AnyFormattedText | None = None,
        style: BaseStyle | None = None,
        color_depth: ColorDepth | None = None,
        cursor: AnyCursorShapeConfig | None = None,
        include_default_pygments_style: FilterOrBool | None = None,
        style_transformation: StyleTransformation | None = None,
        swap_light_and_dark_colors: FilterOrBool | None = None,
        rprompt: AnyFormattedText | None = None,
        multiline: FilterOrBool | None = None,
        prompt_continuation: PromptContinuationText | None = None,
        wrap_lines: FilterOrBool | None = None,
        enable_history_search: FilterOrBool | None = None,
        search_ignore_case: FilterOrBool | None = None,
        complete_while_typing: FilterOrBool | None = None,
        validate_while_typing: FilterOrBool | None = None,
        complete_style: CompleteStyle | None = None,
        auto_suggest: AutoSuggest | None = None,
        validator: Validator | None = None,
        clipboard: Clipboard | None = None,
        mouse_support: FilterOrBool | None = None,
        input_processors: list[Processor] | None = None,
        placeholder: AnyFormattedText | None = None,
        reserve_space_for_menu: int | None = None,
        enable_system_prompt: FilterOrBool | None = None,
        enable_suspend: FilterOrBool | None = None,
        enable_open_in_editor: FilterOrBool | None = None,
        tempfile_suffix: str | Callable[[], str] | None = None,
        tempfile: str | Callable[[], str] | None = None,
        # Following arguments are specific to the current `prompt()` call.
        default: str | Document = "",
        accept_default: bool = False,
        pre_run: Callable[[], None] | None = None,
        set_exception_handler: bool = True,
        handle_sigint: bool = True,
        in_thread: bool = False,
        inputhook: InputHook | None = None,
    ) -> _T:
        """
        Display the prompt.

        The first set of arguments is a subset of the :class:`~.PromptSession`
        class itself. For these, passing in ``None`` will keep the current
        values that are active in the session. Passing in a value will set the
        attribute for the session, which means that it applies to the current,
        but also to the next prompts.

        Note that in order to erase a ``Completer``, ``Validator`` or
        ``AutoSuggest``, you can't use ``None``. Instead pass in a
        ``DummyCompleter``, ``DummyValidator`` or ``DummyAutoSuggest`` instance
        respectively. For a ``Lexer`` you can pass in an empty ``SimpleLexer``.

        Additional arguments, specific for this prompt:

        :param default: The default input text to be shown. (This can be edited
            by the user).
        :param accept_default: When `True`, automatically accept the default
            value without allowing the user to edit the input.
        :param pre_run: Callable, called at the start of `Application.run`.
        :param in_thread: Run the prompt in a background thread; block the
            current thread. This avoids interference with an event loop in the
            current thread. Like `Application.run(in_thread=True)`.

        This method will raise ``KeyboardInterrupt`` when control-c has been
        pressed (for abort) and ``EOFError`` when control-d has been pressed
        (for exit).
        """
        # NOTE: We used to create a backup of the PromptSession attributes and
        #       restore them after exiting the prompt. This code has been
        #       removed, because it was confusing and didn't really serve a use
        #       case. (People were changing `Application.editing_mode`
        #       dynamically and surprised that it was reset after every call.)

        # NOTE 2: YES, this is a lot of repeation below...
        #         However, it is a very convenient for a user to accept all
        #         these parameters in this `prompt` method as well. We could
        #         use `locals()` and `setattr` to avoid the repetition, but
        #         then we loose the advantage of mypy and pyflakes to be able
        #         to verify the code.
        if message is not None:
            self.message = message
        if editing_mode is not None:
            self.editing_mode = editing_mode
        if refresh_interval is not None:
            self.refresh_interval = refresh_interval
        if vi_mode:
            self.editing_mode = EditingMode.VI
        if lexer is not None:
            self.lexer = lexer
        if completer is not None:
            self.completer = completer
        if complete_in_thread is not None:
            self.complete_in_thread = complete_in_thread
        if is_password is not None:
            self.is_password = is_password
        if key_bindings is not None:
            self.key_bindings = key_bindings
        if bottom_toolbar is not None:
            self.bottom_toolbar = bottom_toolbar
        if style is not None:
            self.style = style
        if color_depth is not None:
            self.color_depth = color_depth
        if cursor is not None:
            self.cursor = cursor
        if include_default_pygments_style is not None:
            self.include_default_pygments_style = include_default_pygments_style
        if style_transformation is not None:
            self.style_transformation = style_transformation
        if swap_light_and_dark_colors is not None:
            self.swap_light_and_dark_colors = swap_light_and_dark_colors
        if rprompt is not None:
            self.rprompt = rprompt
        if multiline is not None:
            self.multiline = multiline
        if prompt_continuation is not None:
            self.prompt_continuation = prompt_continuation
        if wrap_lines is not None:
            self.wrap_lines = wrap_lines
        if enable_history_search is not None:
            self.enable_history_search = enable_history_search
        if search_ignore_case is not None:
            self.search_ignore_case = search_ignore_case
        if complete_while_typing is not None:
            self.complete_while_typing = complete_while_typing
        if validate_while_typing is not None:
            self.validate_while_typing = validate_while_typing
        if complete_style is not None:
            self.complete_style = complete_style
        if auto_suggest is not None:
            self.auto_suggest = auto_suggest
        if validator is not None:
            self.validator = validator
        if clipboard is not None:
            self.clipboard = clipboard
        if mouse_support is not None:
            self.mouse_support = mouse_support
        if input_processors is not None:
            self.input_processors = input_processors
        if placeholder is not None:
            self.placeholder = placeholder
        if reserve_space_for_menu is not None:
            self.reserve_space_for_menu = reserve_space_for_menu
        if enable_system_prompt is not None:
            self.enable_system_prompt = enable_system_prompt
        if enable_suspend is not None:
            self.enable_suspend = enable_suspend
        if enable_open_in_editor is not None:
            self.enable_open_in_editor = enable_open_in_editor
        if tempfile_suffix is not None:
            self.tempfile_suffix = tempfile_suffix
        if tempfile is not None:
            self.tempfile = tempfile

        self._add_pre_run_callables(pre_run, accept_default)
        self.default_buffer.reset(
            default if isinstance(default, Document) else Document(default)
        )
        self.app.refresh_interval = self.refresh_interval  # This is not reactive.

        # If we are using the default output, and have a dumb terminal. Use the
        # dumb prompt.
        if self._output is None and is_dumb_terminal():
            with self._dumb_prompt(self.message) as dump_app:
                return dump_app.run(in_thread=in_thread, handle_sigint=handle_sigint)

        return self.app.run(
            set_exception_handler=set_exception_handler,
            in_thread=in_thread,
            handle_sigint=handle_sigint,
            inputhook=inputhook,
        )

    @contextmanager
    def _dumb_prompt(self, message: AnyFormattedText = "") -> Iterator[Application[_T]]:
        """
        Create prompt `Application` for prompt function for dumb terminals.

        Dumb terminals have minimum rendering capabilities. We can only print
        text to the screen. We can't use colors, and we can't do cursor
        movements. The Emacs inferior shell is an example of a dumb terminal.

        We will show the prompt, and wait for the input. We still handle arrow
        keys, and all custom key bindings, but we don't really render the
        cursor movements. Instead we only print the typed character that's
        right before the cursor.
        """
        # Send prompt to output.
        self.output.write(fragment_list_to_text(to_formatted_text(self.message)))
        self.output.flush()

        # Key bindings for the dumb prompt: mostly the same as the full prompt.
        key_bindings: KeyBindingsBase = self._create_prompt_bindings()
        if self.key_bindings:
            key_bindings = merge_key_bindings([self.key_bindings, key_bindings])

        # Create and run application.
        application = cast(
            Application[_T],
            Application(
                input=self.input,
                output=DummyOutput(),
                layout=self.layout,
                key_bindings=key_bindings,
            ),
        )

        def on_text_changed(_: object) -> None:
            self.output.write(self.default_buffer.document.text_before_cursor[-1:])
            self.output.flush()

        self.default_buffer.on_text_changed += on_text_changed

        try:
            yield application
        finally:
            # Render line ending.
            self.output.write("\r\n")
            self.output.flush()

            self.default_buffer.on_text_changed -= on_text_changed

    async def prompt_async(
        self,
        # When any of these arguments are passed, this value is overwritten
        # in this PromptSession.
        message: AnyFormattedText | None = None,
        # `message` should go first, because people call it as
        # positional argument.
        *,
        editing_mode: EditingMode | None = None,
        refresh_interval: float | None = None,
        vi_mode: bool | None = None,
        lexer: Lexer | None = None,
        completer: Completer | None = None,
        complete_in_thread: bool | None = None,
        is_password: bool | None = None,
        key_bindings: KeyBindingsBase | None = None,
        bottom_toolbar: AnyFormattedText | None = None,
        style: BaseStyle | None = None,
        color_depth: ColorDepth | None = None,
        cursor: CursorShapeConfig | None = None,
        include_default_pygments_style: FilterOrBool | None = None,
        style_transformation: StyleTransformation | None = None,
        swap_light_and_dark_colors: FilterOrBool | None = None,
        rprompt: AnyFormattedText | None = None,
        multiline: FilterOrBool | None = None,
        prompt_continuation: PromptContinuationText | None = None,
        wrap_lines: FilterOrBool | None = None,
        enable_history_search: FilterOrBool | None = None,
        search_ignore_case: FilterOrBool | None = None,
        complete_while_typing: FilterOrBool | None = None,
        validate_while_typing: FilterOrBool | None = None,
        complete_style: CompleteStyle | None = None,
        auto_suggest: AutoSuggest | None = None,
        validator: Validator | None = None,
        clipboard: Clipboard | None = None,
        mouse_support: FilterOrBool | None = None,
        input_processors: list[Processor] | None = None,
        placeholder: AnyFormattedText | None = None,
        reserve_space_for_menu: int | None = None,
        enable_system_prompt: FilterOrBool | None = None,
        enable_suspend: FilterOrBool | None = None,
        enable_open_in_editor: FilterOrBool | None = None,
        tempfile_suffix: str | Callable[[], str] | None = None,
        tempfile: str | Callable[[], str] | None = None,
        # Following arguments are specific to the current `prompt()` call.
        default: str | Document = "",
        accept_default: bool = False,
        pre_run: Callable[[], None] | None = None,
        set_exception_handler: bool = True,
        handle_sigint: bool = True,
    ) -> _T:
        if message is not None:
            self.message = message
        if editing_mode is not None:
            self.editing_mode = editing_mode
        if refresh_interval is not None:
            self.refresh_interval = refresh_interval
        if vi_mode:
            self.editing_mode = EditingMode.VI
        if lexer is not None:
            self.lexer = lexer
        if completer is not None:
            self.completer = completer
        if complete_in_thread is not None:
            self.complete_in_thread = complete_in_thread
        if is_password is not None:
            self.is_password = is_password
        if key_bindings is not None:
            self.key_bindings = key_bindings
        if bottom_toolbar is not None:
            self.bottom_toolbar = bottom_toolbar
        if style is not None:
            self.style = style
        if color_depth is not None:
            self.color_depth = color_depth
        if cursor is not None:
            self.cursor = cursor
        if include_default_pygments_style is not None:
            self.include_default_pygments_style = include_default_pygments_style
        if style_transformation is not None:
            self.style_transformation = style_transformation
        if swap_light_and_dark_colors is not None:
            self.swap_light_and_dark_colors = swap_light_and_dark_colors
        if rprompt is not None:
            self.rprompt = rprompt
        if multiline is not None:
            self.multiline = multiline
        if prompt_continuation is not None:
            self.prompt_continuation = prompt_continuation
        if wrap_lines is not None:
            self.wrap_lines = wrap_lines
        if enable_history_search is not None:
            self.enable_history_search = enable_history_search
        if search_ignore_case is not None:
            self.search_ignore_case = search_ignore_case
        if complete_while_typing is not None:
            self.complete_while_typing = complete_while_typing
        if validate_while_typing is not None:
            self.validate_while_typing = validate_while_typing
        if complete_style is not None:
            self.complete_style = complete_style
        if auto_suggest is not None:
            self.auto_suggest = auto_suggest
        if validator is not None:
            self.validator = validator
        if clipboard is not None:
            self.clipboard = clipboard
        if mouse_support is not None:
            self.mouse_support = mouse_support
        if input_processors is not None:
            self.input_processors = input_processors
        if placeholder is not None:
            self.placeholder = placeholder
        if reserve_space_for_menu is not None:
            self.reserve_space_for_menu = reserve_space_for_menu
        if enable_system_prompt is not None:
            self.enable_system_prompt = enable_system_prompt
        if enable_suspend is not None:
            self.enable_suspend = enable_suspend
        if enable_open_in_editor is not None:
            self.enable_open_in_editor = enable_open_in_editor
        if tempfile_suffix is not None:
            self.tempfile_suffix = tempfile_suffix
        if tempfile is not None:
            self.tempfile = tempfile

        self._add_pre_run_callables(pre_run, accept_default)
        self.default_buffer.reset(
            default if isinstance(default, Document) else Document(default)
        )
        self.app.refresh_interval = self.refresh_interval  # This is not reactive.

        # If we are using the default output, and have a dumb terminal. Use the
        # dumb prompt.
        if self._output is None and is_dumb_terminal():
            with self._dumb_prompt(self.message) as dump_app:
                return await dump_app.run_async(handle_sigint=handle_sigint)

        return await self.app.run_async(
            set_exception_handler=set_exception_handler, handle_sigint=handle_sigint
        )

    def _add_pre_run_callables(
        self, pre_run: Callable[[], None] | None, accept_default: bool
    ) -> None:
        def pre_run2() -> None:
            if pre_run:
                pre_run()

            if accept_default:
                # Validate and handle input. We use `call_from_executor` in
                # order to run it "soon" (during the next iteration of the
                # event loop), instead of right now. Otherwise, it won't
                # display the default value.
                get_running_loop().call_soon(self.default_buffer.validate_and_handle)

        self.app.pre_run_callables.append(pre_run2)

    @property
    def editing_mode(self) -> EditingMode:
        return self.app.editing_mode

    @editing_mode.setter
    def editing_mode(self, value: EditingMode) -> None:
        self.app.editing_mode = value

    def _get_default_buffer_control_height(self) -> Dimension:
        # If there is an autocompletion menu to be shown, make sure that our
        # layout has at least a minimal height in order to display it.
        if (
            self.completer is not None
            and self.complete_style != CompleteStyle.READLINE_LIKE
        ):
            space = self.reserve_space_for_menu
        else:
            space = 0

        if space and not get_app().is_done:
            buff = self.default_buffer

            # Reserve the space, either when there are completions, or when
            # `complete_while_typing` is true and we expect completions very
            # soon.
            if buff.complete_while_typing() or buff.complete_state is not None:
                return Dimension(min=space)

        return Dimension()

    def _get_prompt(self) -> StyleAndTextTuples:
        return to_formatted_text(self.message, style="class:prompt")

    def _get_continuation(
        self, width: int, line_number: int, wrap_count: int
    ) -> StyleAndTextTuples:
        """
        Insert the prompt continuation.

        :param width: The width that was used for the prompt. (more or less can
            be used.)
        :param line_number:
        :param wrap_count: Amount of times that the line has been wrapped.
        """
        prompt_continuation = self.prompt_continuation

        if callable(prompt_continuation):
            continuation: AnyFormattedText = prompt_continuation(
                width, line_number, wrap_count
            )
        else:
            continuation = prompt_continuation

        # When the continuation prompt is not given, choose the same width as
        # the actual prompt.
        if continuation is None and is_true(self.multiline):
            continuation = " " * width

        return to_formatted_text(continuation, style="class:prompt-continuation")

    def _get_line_prefix(
        self,
        line_number: int,
        wrap_count: int,
        get_prompt_text_2: _StyleAndTextTuplesCallable,
    ) -> StyleAndTextTuples:
        """
        Return whatever needs to be inserted before every line.
        (the prompt, or a line continuation.)
        """
        # First line: display the "arg" or the prompt.
        if line_number == 0 and wrap_count == 0:
            if not is_true(self.multiline) and get_app().key_processor.arg is not None:
                return self._inline_arg()
            else:
                return get_prompt_text_2()

        # For the next lines, display the appropriate continuation.
        prompt_width = get_cwidth(fragment_list_to_text(get_prompt_text_2()))
        return self._get_continuation(prompt_width, line_number, wrap_count)

    def _get_arg_text(self) -> StyleAndTextTuples:
        "'arg' toolbar, for in multiline mode."
        arg = self.app.key_processor.arg
        if arg is None:
            # Should not happen because of the `has_arg` filter in the layout.
            return []

        if arg == "-":
            arg = "-1"

        return [("class:arg-toolbar", "Repeat: "), ("class:arg-toolbar.text", arg)]

    def _inline_arg(self) -> StyleAndTextTuples:
        "'arg' prefix, for in single line mode."
        app = get_app()
        if app.key_processor.arg is None:
            return []
        else:
            arg = app.key_processor.arg

            return [
                ("class:prompt.arg", "(arg: "),
                ("class:prompt.arg.text", str(arg)),
                ("class:prompt.arg", ") "),
            ]

    # Expose the Input and Output objects as attributes, mainly for
    # backward-compatibility.

    @property
    def input(self) -> Input:
        return self.app.input

    @property
    def output(self) -> Output:
        return self.app.output

