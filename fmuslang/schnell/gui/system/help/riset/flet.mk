--% getting started
https://flet.dev/docs/
https://github.com/flet-dev/flet/discussions

https://flutterrepos.com/lib/flet-enables-developers-to-easily-build-realtime-web-mobile-and-desktop-apps-in-python-no-frontend-experience-required
https://flutterrepos.com/lib/intel-rohd

ini jd topik tersendiri krn begitu menarik konsepnya

ada yg namanya flet.exe dan fletd.exe, aku asumsikan ini dari client/ dan server/
aku asumsikan: program flet python (sdk/) ke client/, lalu ke server/.

struktur
```
flet/
    ci/
    client/
    docs/
    media/
    sdk/
    server/
```

sementara pypkg-nya
```

C:\Users\usef\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\flet>wsl tree
.
├── __init__.py
├── __pyinstaller
│   ├── __init__.py
│   ├── hook-flet.py
│   ├── rthooks
│   │   └── pyi_rth_localhost_fletd.py
│   └── rthooks.dat
├── alert_dialog.py
├── alignment.py
├── animated_switcher.py
├── animation.py
├── app_bar.py
├── banner.py
├── bin
│   ├── flet
│   │   ├── data
│   │   │   ├── app.so
│   │   │   ├── flutter_assets
│   │   │   │   ├── AssetManifest.json
│   │   │   │   ├── FontManifest.json
│   │   │   │   ├── NOTICES.Z
│   │   │   │   ├── fonts
│   │   │   │   │   └── MaterialIcons-Regular.otf
│   │   │   │   ├── packages
│   │   │   │   │   ├── cupertino_icons
│   │   │   │   │   │   └── assets
│   │   │   │   │   │       └── CupertinoIcons.ttf
│   │   │   │   │   └── window_manager
│   │   │   │   │       └── images
│   │   │   │   │           ├── ic_chrome_close.png
│   │   │   │   │           ├── ic_chrome_maximize.png
│   │   │   │   │           ├── ic_chrome_minimize.png
│   │   │   │   │           └── ic_chrome_unmaximize.png
│   │   │   │   └── shaders
│   │   │   │       └── ink_sparkle.frag
│   │   │   └── icudtl.dat
│   │   ├── flet.exe
│   │   ├── flutter_windows.dll
│   │   ├── msvcp140.dll
│   │   ├── screen_retriever_plugin.dll
│   │   ├── url_launcher_windows_plugin.dll
│   │   ├── vcruntime140.dll
│   │   ├── vcruntime140_1.dll
│   │   └── window_manager_plugin.dll
│   └── fletd.exe
├── border.py
├── border_radius.py
├── buttons.py
├── card.py
├── checkbox.py
├── circle_avatar.py
├── clipboard.py
├── colors.py
├── column.py
├── connection.py
├── constants.py
├── constrained_control.py
├── container.py
├── control.py
├── divider.py
├── drag_target.py
├── draggable.py
├── dropdown.py
├── elevated_button.py
├── embed_json_encoder.py
├── event.py
├── event_handler.py
├── filled_button.py
├── filled_tonal_button.py
├── flet.py
├── floating_action_button.py
├── focus.py
├── form_field_control.py
├── gradients.py
├── grid_view.py
├── icon.py
├── icon_button.py
├── icons.py
├── image.py
├── launch_url.py
├── list_tile.py
├── list_view.py
├── margin.py
├── markdown.py
├── navigation_rail.py
├── outlined_button.py
├── padding.py
├── page.py
├── popup_menu_button.py
├── progress_bar.py
├── progress_ring.py
├── protocol.py
├── pubsub.py
├── radio.py
├── radio_group.py
├── reconnecting_websocket.py
├── ref.py
├── row.py
├── shader_mask.py
├── slider.py
├── snack_bar.py
├── stack.py
├── switch.py
├── tabs.py
├── template_route.py
├── text.py
├── text_button.py
├── textfield.py
├── theme.py
├── transform.py
├── types.py
├── user_control.py
├── utils.py
├── version.py
├── vertical_divider.py
└── view.py
```
--#

--% sdk/flet.py
coba verifikasi, bahwa, dari python sdk, loncat ke go server flexd.exe
dari fletd.exe masuk ke flet.exe.

```
def app(
    name="",
    host=None,
    port=0,
    target=None,
    permissions=None,
    view: AppViewer = FLET_APP,
    assets_dir=None,
    web_renderer="canvaskit",
    route_url_strategy="hash",
):
    ...
    conn = _connect_internal(
        page_name=name,
        host=host,
        port=port,
        is_app=True,
        permissions=permissions,
        session_handler=target,
        assets_dir=assets_dir,
        web_renderer=web_renderer,
        route_url_strategy=route_url_strategy,
    )
    ...

def _connect_internal(
    page_name=None,
    host=None,
    port=0,
    is_app=False,
    update=False,
    share=False,
    server=None,
    token=None,
    permissions=None,
    session_handler=None,
    assets_dir=None,
    web_renderer=None,
    route_url_strategy=None,
):
    server_ip = host if host not in [None, "", "*"] else "127.0.0.1"
    port = _start_flet_server(
        host, port, attached, assets_dir, web_renderer, route_url_strategy
    )
    server = f"http://{server_ip}:{port}"

def _start_flet_server(
    host, port, attached, assets_dir, web_renderer, route_url_strategy
):
    fletd_exe = "fletd.exe" if is_windows() else "fletd"
    # check if flet.exe exists in "bin" directory (user mode)
    p = Path(__file__).parent.joinpath("bin", fletd_exe)
    if p.exists():
        fletd_path = str(p)
        logging.info(f"Flet Server found in: {fletd_path}")
    else:
        # check if flet.exe is in PATH (flet developer mode)
        fletd_path = which(fletd_exe)
        if not fletd_path:
            # download flet from GitHub (python module developer mode)
            fletd_path = _download_fletd()
        else:
            logging.info(f"Flet Server found in PATH")
    fletd_env = {**os.environ}
    subprocess.Popen(
        args,
        env=fletd_env,
        creationflags=creationflags,
        start_new_session=start_new_session,
        stdout=subprocess.DEVNULL if log_level >= logging.WARNING else None,
        stderr=subprocess.DEVNULL if log_level >= logging.WARNING else None,
        startupinfo=startupinfo,
    )
    return port
```
contoh program:
```
import flet
from flet import Page, Text

def main(page: Page):
    page.add(Text("Hello, world!"))

flet.app(target=main)
```

cek apa ini mengingatkan atau menyadarkan sesuatu? page adlh top-level ya kan
```

def on_session_created(conn, session_data):
    page = Page(conn, session_data.sessionID)
    conn.sessions[session_data.sessionID] = page
    print("Session started:", session_data.sessionID)
    try:
        session_handler(page)
    except Exception as e:
        print(
            f"Unhandled error processing page session {page.session_id}:",
            traceback.format_exc(),
        )
        page.error(f"There was an error while processing your request: {e}")

ws_url = _get_ws_url(server)
ws = ReconnectingWebSocket(ws_url)
conn = Connection(ws) # kita gunakan conn, dia membungkus ws...
conn.on_event = on_event
if session_handler != None:
    conn.on_session_created = on_session_created
#
ws.on_connect = _on_ws_connect
ws.on_failed_connect = _on_ws_failed_connect
ws.connect()
#

def page(
    name="",
    host=None,
    port=0,
    permissions=None,
    view: AppViewer = WEB_BROWSER,
    assets_dir=None,
    web_renderer="canvaskit",
    route_url_strategy="hash",
):
    conn = _connect_internal(
        page_name=name,
        host=host,
        port=port,
        is_app=False,
        permissions=permissions,
        assets_dir=assets_dir,
        web_renderer=web_renderer,
        route_url_strategy=route_url_strategy,
    )
    print("Page URL:", conn.page_url)
    page = Page(conn, constants.ZERO_SESSION)
    conn.sessions[constants.ZERO_SESSION] = page

    if view == WEB_BROWSER:
        open_in_browser(conn.page_url)

    return page
```
aku asumsikan pengiriman json dari sdk ke fletd.exe adlh via websocket.
--#

--% sdk/connection.py
```
class Connection:
    def __init__(self, ws: ReconnectingWebSocket):
        self._ws = ws
        self._ws.on_message = self._on_message # ini tentu the real deal...
        self._ws_callbacks = {}
        self._on_event = None
        self._on_session_created = None
        self.host_client_id = None
        self.page_name = None
        self.page_url = None
        self.sessions = {}
        self.pubsubhub = PubSubHub()
#

def _on_message(self, data):
    logging.debug(f"_on_message: {data}")
    msg_dict = json.loads(data)
    msg = Message(**msg_dict)
    if msg.id != "":
        # callback
        evt = self._ws_callbacks[msg.id][0]
        self._ws_callbacks[msg.id] = (None, msg.payload)
        evt.set()
    elif msg.action == Actions.PAGE_EVENT_TO_HOST:
        if self._on_event != None:
            th = threading.Thread(
                target=self._on_event,
                args=(
                    self,
                    PageEventPayload(**msg.payload),
                ),
                daemon=True,
            )
            th.start()
            # self._on_event(self, PageEventPayload(**msg.payload))
    elif msg.action == Actions.SESSION_CREATED:
        if self._on_session_created != None:
            th = threading.Thread(
                target=self._on_session_created,
                args=(
                    self,
                    PageSessionCreatedPayload(**msg.payload),
                ),
                daemon=True,
            )
            th.start()
    else:
        # it's something else
        print(msg.payload)

```

proses kirim-mengirim 
```

def send_command(self, page_name: str, session_id: str, command: Command):
    payload = PageCommandRequestPayload(page_name, session_id, command)
    response = self._send_message_with_result(
        Actions.PAGE_COMMAND_FROM_HOST, payload
    )
    result = PageCommandResponsePayload(**response)
    if result.error != "":
        raise Exception(result.error)
    return result

def _send_message_with_result(self, action_name, payload):
    msg_id = uuid.uuid4().hex
    msg = Message(msg_id, action_name, payload)
    j = json.dumps(msg, cls=CommandEncoder, separators=(",", ":"))
    logging.debug(f"_send_message_with_result: {j}")
    evt = threading.Event()
    self._ws_callbacks[msg_id] = (evt, None)
    self._ws.send(j)
    evt.wait()
    return self._ws_callbacks.pop(msg_id)[1]
```
spt nya yg kucari harusnya adlh PAGE_EVENT_TO_HOST???
krn PAGE_COMMAND_FROM_HOST ini tentu dari flexd.exe?

coba cari send_command dimana saja:
```
C:\src\flet-flutter\flet\sdk\python\flet>grep -r "send_command(" .
./connection.py:    def send_command(self, page_name: str, session_id: str, command: Command):
./control.py:            return self.__page._send_command("clean", [self.uid])
./page.py:            return self._send_command("clean", [self.uid])
./page.py:            self._send_command("error", [message])
./page.py:        return self._send_command("signout", None)
./page.py:            self._send_command("canAccess", [users_and_groups]).result.lower() == "true"
./page.py:    def _send_command(self, name: str, values: List[str]):
./page.py:        return self.__conn.send_command(

# dari page.py

def _send_command(self, name: str, values: List[str]):
    return self.__conn.send_command(
        self.__conn.page_name,
        self._session_id,
        Command(0, name, values, None, None),
    )
```
--#

--% alert_dialog.py
C:\Users\usef\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\flet\alert_dialog.py
--#

--% alignment.py
--#

--% animated_switcher.py
--#

--% animation.py
--#

--% app_bar.py
--#

--% banner.py
--#

--% border.py
--#

--% border_radius.py
--#

--% buttons.py
--#

--% card.py
--#

--% checkbox.py
--#

--% circle_avatar.py
--#

--% clipboard.py
--#

--% colors.py
--#

--% column.py
--#

--% connection.py
--#

--% constants.py
--#

--% constrained_control.py
--#

--% container.py
```
class Container(ConstrainedControl):
    def __init__(
        self,
        content: Control = None,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        tooltip: str = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        padding: PaddingValue = None,
        margin: MarginValue = None,
        alignment: Alignment = None,
        bgcolor: str = None,
        gradient: Gradient = None,
        blend_mode: BlendMode = None,
        border: Border = None,
        border_radius: BorderRadiusValue = None,
        image_src: str = None,
        image_src_base64: str = None,
        image_repeat: ImageRepeat = None,
        image_fit: ImageFit = None,
        image_opacity: OptionalNumber = None,
        ink: bool = None,
        animate: AnimationValue = None,
        on_click=None,
        on_long_press=None,
        on_hover=None,
    ):
    def _get_control_name(self):
    def _before_build_command(self):
    def _get_children(self):
    # alignment
    @property
    def alignment(self):
    @alignment.setter
    @beartype
    def alignment(self, value: Optional[Alignment]):
    # padding
    @property
    def padding(self):
    @padding.setter
    @beartype
    def padding(self, value: PaddingValue):
    # margin
    @property
    def margin(self):
    @margin.setter
    @beartype
    def margin(self, value: MarginValue):
    # bgcolor
    @property
    def bgcolor(self):
    @bgcolor.setter
    def bgcolor(self, value):
    # gradient
    @property
    def gradient(self):
    @gradient.setter
    @beartype
    def gradient(self, value: Optional[Gradient]):
    # blend_mode
    @property
    def blend_mode(self):
    @blend_mode.setter
    @beartype
    def blend_mode(self, value: Optional[BlendMode]):
    # border
    @property
    def border(self):
    @border.setter
    @beartype
    def border(self, value: Optional[Border]):
    # border_radius
    @property
    def border_radius(self):
    @border_radius.setter
    @beartype
    def border_radius(self, value: BorderRadiusValue):
    # image_src
    @property
    def image_src(self):
    @image_src.setter
    def image_src(self, value):
    # image_src_base64
    @property
    def image_src_base64(self):
    @image_src_base64.setter
    def image_src_base64(self, value):
    # image_fit
    @property
    def image_fit(self):
    @image_fit.setter
    @beartype
    def image_fit(self, value: ImageFit):
    # image_repeat
    @property
    def image_repeat(self):
    @image_repeat.setter
    @beartype
    def image_repeat(self, value: ImageRepeat):
    # image_opacity
    @property
    def image_opacity(self):
    @image_opacity.setter
    @beartype
    def image_opacity(self, value: OptionalNumber):
    # content
    @property
    def content(self):
    @content.setter
    @beartype
    def content(self, value: Optional[Control]):
    # ink
    @property
    def ink(self):
    @ink.setter
    @beartype
    def ink(self, value: Optional[bool]):
    # animate
    @property
    def animate(self) -> AnimationValue:
    @animate.setter
    @beartype
    def animate(self, value: AnimationValue):
    # on_click
    @property
    def on_click(self):
    @on_click.setter
    def on_click(self, handler):
    # on_long_press
    @property
    def on_long_press(self):
    @on_long_press.setter
    def on_long_press(self, handler):
    # on_hover
    @property
    def on_hover(self):
    @on_hover.setter
    def on_hover(self, handler):
```
--#

--% control.py
```
import datetime as dt
import json
import threading
from difflib import SequenceMatcher
from typing import Union

from beartype import beartype
from beartype.typing import List, Optional

from flet.embed_json_encoder import EmbedJsonEncoder
from flet.protocol import Command
from flet.ref import Ref

try:
    from typing import Literal
except:
    from typing_extensions import Literal
#

MainAxisAlignment = Literal[
    None,
    "start",
    "end",
    "center",
    "spaceBetween",
    "spaceAround",
    "spaceEvenly",
]

CrossAxisAlignment = Literal[
    None,
    "start",
    "end",
    "center",
    "stretch",
    "baseline",
]

BorderStyle = Literal[
    None,
    "none",
    "solid",
]

TextAlign = Literal[None, "left", "right", "center", "justify", "start", "end"]

InputBorder = Literal[None, "outline", "underline", "none"]

OptionalNumber = Union[None, int, float]

ScrollMode = Literal[None, True, False, "none", "auto", "adaptive", "always", "hidden"]

BlendMode = Literal[
    "clear",
    "color",
    "colorBurn",
    "colorDodge",
    "darken",
    "difference",
    "dst",
    "dstATop",
    "dstIn",
    "dstOut",
    "dstOver",
    "exclusion",
    "hardLight",
    "hue",
    "lighten",
    "luminosity",
    "modulate",
    "multiply",
    "overlay",
    "plus",
    "saturation",
    "screen",
    "softLight",
    "src",
    "srcATop",
    "srcIn",
    "srcOut",
    "srcOver",
    "values",
    "xor",
]

class Control:
    def __init__(
        self,
        ref: Ref = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        tooltip: str = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
    ):
        self.__page = None
        self.__attrs = {}
        self.__previous_children = []
        self._id = None
        self.__uid = None
        self.expand = expand
        self.opacity = opacity
        self.tooltip = tooltip
        self.visible = visible
        self.disabled = disabled
        self.data = data
        self.__event_handlers = {}
        self._lock = threading.Lock()
        if ref:
            ref.current = self
    def _is_isolated(self):
    def _build(self):
    def _before_build_command(self):
    def did_mount(self):
    def will_unmount(self):
    def _get_children(self):
    def _get_control_name(self):
    def _add_event_handler(self, event_name, handler):
    def _get_event_handler(self, event_name):
    def _get_attr(self, name, def_value=None, data_type="string"):
    def _set_attr(self, name, value, dirty=True):
    def _get_value_or_list_attr(self, name, delimiter):
    def _set_value_or_list_attr(self, name, value, delimiter):
    def _set_attr_internal(self, name, value, dirty=True):
    def _set_attr_json(self, name, value):
    def _convert_attr_json(self, value):
    @property
    def event_handlers(self):
    @property
    def _previous_children(self):
    @property
    def _id(self):
    @_id.setter
    def _id(self, value):
    @property
    def page(self):
    @page.setter
    def page(self, page):
    @property
    def uid(self):
    @property
    def expand(self):
    @expand.setter
    @beartype
    def expand(self, value: Union[None, bool, int]):
    @property
    def opacity(self):
    @opacity.setter
    def opacity(self, value):
    @property
    def tooltip(self):
    @tooltip.setter
    def tooltip(self, value):
    @property
    def visible(self):
    @visible.setter
    @beartype
    def visible(self, value: Optional[bool]):
    @property
    def disabled(self):
    @disabled.setter
    @beartype
    def disabled(self, value: Optional[bool]):
    @property
    def data(self):
    @data.setter
    def data(self, value):
    # private methods
    def _build_add_commands(self, indent=0, index=None, added_controls=None):
    def _build_command(self, update=False):
    # public methods
    def update(self):
    def clean(self):
    def build_update_commands(self, index, added_controls, commands, isolated=False):
    def _remove_control_recursively(self, index, control):
```

--#

--% divider.py
--#

--% drag_target.py
--#

--% draggable.py
--#

--% dropdown.py
--#

--% elevated_button.py
--#

--% embed_json_encoder.py
--#

--% event.py
--#

--% event_handler.py
--#

--% filled_button.py
--#

--% filled_tonal_button.py
--#

--% flet.py
--#

--% floating_action_button.py
--#

--% focus.py
--#

--% form_field_control.py
--#

--% gradients.py
--#

--% grid_view.py
```
class GridView(ConstrainedControl):
    def __init__(
        self,
        controls: List[Control] = None,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        horizontal: bool = None,
        runs_count: int = None,
        max_extent: int = None,
        spacing: OptionalNumber = None,
        run_spacing: OptionalNumber = None,
        child_aspect_ratio: OptionalNumber = None,
        padding: PaddingValue = None,
    ):

    def _get_control_name(self):
    def _before_build_command(self):
    def _get_children(self):
    def clean(self):
    @property
    def horizontal(self):
    @horizontal.setter
    @beartype
    def horizontal(self, value: Optional[bool]):
    @property
    def runs_count(self):
    @runs_count.setter
    @beartype
    def runs_count(self, value: Optional[int]):
    @property
    def max_extent(self):
    @max_extent.setter
    @beartype
    def max_extent(self, value: OptionalNumber):
    @property
    def spacing(self):
    @spacing.setter
    @beartype
    def spacing(self, value: OptionalNumber):
    @property
    def run_spacing(self):
    @run_spacing.setter
    @beartype
    def run_spacing(self, value: OptionalNumber):
    @property
    def child_aspect_ratio(self):
    @child_aspect_ratio.setter
    @beartype
    def child_aspect_ratio(self, value: OptionalNumber):
    @property
    def padding(self):
    @padding.setter
    @beartype
    def padding(self, value: PaddingValue):
    @property
    def controls(self):
    @controls.setter
    def controls(self, value):
```
--#

--% icon.py
--#

--% icon_button.py
--#

--% icons.py
--#

--% image.py
--#

--% launch_url.py
--#

--% list_tile.py
```
class ListTile(ConstrainedControl):
    def __init__(
        self,
        text: str = None,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        tooltip: str = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        content_padding: PaddingValue = None,
        leading: Control = None,
        title: Control = None,
        subtitle: Control = None,
        trailing: Control = None,
        is_three_line: bool = None,
        selected: bool = None,
        dense: bool = None,
        autofocus: bool = None,
        on_click=None,
        on_long_press=None,
    ):

    def _get_control_name(self):
    def _before_build_command(self):
    def _get_children(self):
    @property
    def content_padding(self):
    @content_padding.setter
    @beartype
    def content_padding(self, value: PaddingValue):
    @property
    def leading(self):
    @leading.setter
    @beartype
    def leading(self, value: Optional[Control]):
    @property
    def title(self):
    @title.setter
    @beartype
    def title(self, value: Optional[Control]):
    @property
    def subtitle(self):
    @subtitle.setter
    @beartype
    def subtitle(self, value: Optional[Control]):
    @property
    def trailing(self):
    @trailing.setter
    @beartype
    def trailing(self, value: Optional[Control]):
    @property
    def is_three_line(self):
    @is_three_line.setter
    @beartype
    def is_three_line(self, value: Optional[bool]):
    @property
    def selected(self):
    @selected.setter
    @beartype
    def selected(self, value: Optional[bool]):
    @property
    def dense(self):
    @dense.setter
    @beartype
    def dense(self, value: Optional[bool]):
    @property
    def autofocus(self):
    @autofocus.setter
    @beartype
    def autofocus(self, value: Optional[bool]):
    @property
    def on_click(self):
    @on_click.setter
    def on_click(self, handler):
    @property
    def on_long_press(self):
    @on_long_press.setter
    def on_long_press(self, handler):
```
--#

--% list_view.py
```
class ListView(ConstrainedControl):
    def __init__(
        self,
        controls: List[Control] = None,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        horizontal: bool = None,
        spacing: OptionalNumber = None,
        item_extent: OptionalNumber = None,
        first_item_prototype: bool = None,
        divider_thickness: OptionalNumber = None,
        padding: PaddingValue = None,
        auto_scroll: bool = None,
    ):

    def _get_control_name(self):
    def _before_build_command(self):
    def _get_children(self):
    def clean(self):
    @property
    def horizontal(self):
    @horizontal.setter
    @beartype
    def horizontal(self, value: Optional[bool]):
    @property
    def spacing(self):
    @spacing.setter
    @beartype
    def spacing(self, value: OptionalNumber):
    @property
    def divider_thickness(self):
    @divider_thickness.setter
    @beartype
    def divider_thickness(self, value: OptionalNumber):
    @property
    def item_extent(self):
    @item_extent.setter
    @beartype
    def item_extent(self, value: OptionalNumber):
    @property
    def first_item_prototype(self):
    @first_item_prototype.setter
    @beartype
    def first_item_prototype(self, value: Optional[bool]):
    @property
    def padding(self):
    @padding.setter
    @beartype
    def padding(self, value: PaddingValue):
    @property
    def controls(self):
    @controls.setter
    def controls(self, value):
    @property
    def auto_scroll(self):
    @auto_scroll.setter
    @beartype
    def auto_scroll(self, value: Optional[bool]):
```
--#

--% margin.py
--#

--% markdown.py
```
MarkdownExtensionSet = Literal[
    None, "none", "commonMark", "gitHubWeb", "gitHubFlavored"
]

class Markdown(ConstrainedControl):
    def __init__(
        self,
        value: str = None,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        tooltip: str = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        selectable: bool = None,
        extension_set: MarkdownExtensionSet = None,
        on_tap_link=None,
    ):
```
--#

--% navigation_rail.py
```
NavigationRailLabelType = Literal[None, "none", "all", "selected"]

class NavigationRailDestination(Control):
    def __init__(
        self,
        ref: Ref = None,
        icon: str = None,
        icon_content: Control = None,
        selected_icon: str = None,
        selected_icon_content: Control = None,
        label: str = None,
        label_content: Control = None,
        padding: PaddingValue = None,
    ):

class NavigationRail(ConstrainedControl):
    def __init__(
        self,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # NavigationRail-specific
        destinations: List[NavigationRailDestination] = None,
        selected_index: int = None,
        extended: bool = None,
        label_type: NavigationRailLabelType = None,
        bgcolor: str = None,
        leading: Control = None,
        trailing: Control = None,
        min_width: OptionalNumber = None,
        min_extended_width: OptionalNumber = None,
        group_alignment: OptionalNumber = None,
        on_change=None,
    ):
```
--#

--% outlined_button.py
--#

--% padding.py
--#

--% page.py
```
PageDesign = Literal[None, "material", "cupertino", "fluent", "macos", "adaptive"]
ThemeMode = Literal[None, "system", "light", "dark"]

class Page(Control):
    def __init__(self, conn: Connection, session_id):
    def __enter__(self):
    def __exit__(self, type, value, traceback):
    def get_control(self, id):
    def _before_build_command(self):
    def _get_children(self):
    def _fetch_page_details(self):
    def update(self, *controls):
    def __update(self, *controls):
    def add(self, *controls):
    def insert(self, at, *controls):
    def remove(self, *controls):
    def remove_at(self, index):
    def clean(self):
    def error(self, message=""):
    def on_event(self, e: Event):
    def wait_event(self):
    def show_signin(self, auth_providers="*", auth_groups=False, allow_dismiss=False):
    def go(self, route):
    def signout(self):
    def can_access(self, users_and_groups):
    def close(self):
    def _send_command(self, name: str, values: List[str]):
    @beartype
    def set_clipboard(self, value: str):
    @beartype
    def launch_url(self, url: str):
    @beartype
    def show_snack_bar(self, snack_bar: SnackBar):
    def window_destroy(self):
    def window_center(self):
    @property
    def url(self):
    @property
    def name(self):
    @property
    def connection(self):
    @property
    def index(self):
    @property
    def session_id(self):
    @property
    def pubsub(self):
    @property
    def title(self):
    @title.setter
    def title(self, value):
    @property
    def route(self):
    @route.setter
    def route(self, value):
    @property
    def pwa(self):
    @property
    def design(self):
    @design.setter
    @beartype
    def design(self, value: PageDesign):
    @property
    def fonts(self):
    @fonts.setter
    @beartype
    def fonts(self, value: Optional[Dict[str, str]]):
    @property
    def views(self):
    @property
    def controls(self):
    @controls.setter
    @beartype
    def controls(self, value: List[Control]):
    @property
    def appbar(self):
    @appbar.setter
    @beartype
    def appbar(self, value: Optional[AppBar]):
    @property
    def floating_action_button(self):
    @floating_action_button.setter
    @beartype
    def floating_action_button(self, value: Optional[FloatingActionButton]):
    @property
    def horizontal_alignment(self):
    @horizontal_alignment.setter
    @beartype
    def horizontal_alignment(self, value: CrossAxisAlignment):
    @property
    def vertical_alignment(self):
    @vertical_alignment.setter
    @beartype
    def vertical_alignment(self, value: MainAxisAlignment):
    @property
    def spacing(self):
    @spacing.setter
    @beartype
    def spacing(self, value: OptionalNumber):
    @property
    def padding(self):
    @padding.setter
    @beartype
    def padding(self, value: PaddingValue):
    @property
    def bgcolor(self):
    @bgcolor.setter
    def bgcolor(self, value):
    @property
    def scroll(self):
    @scroll.setter
    @beartype
    def scroll(self, value: ScrollMode):
    @property
    def auto_scroll(self):
    @auto_scroll.setter
    @beartype
    def auto_scroll(self, value: Optional[bool]):
    @property
    def splash(self):
    @splash.setter
    @beartype
    def splash(self, value: Optional[Control]):
    @property
    def banner(self):
    @banner.setter
    @beartype
    def banner(self, value: Optional[Banner]):
    @property
    def snack_bar(self):
    @snack_bar.setter
    @beartype
    def snack_bar(self, value: Optional[SnackBar]):
    @property
    def dialog(self):
    @dialog.setter
    @beartype
    def dialog(self, value: Optional[Control]):
    @property
    def theme_mode(self):
    ...sial masih banyak...

class Offstage(Control):
    def __init__(
        self,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
    ):
class ControlEvent(Event):
    def __init__(self, target: str, name: str, data: str, control: Control, page: Page):
        Event.__init__(self, target=target, name=name, data=data)
        self.control: Control = control
        self.page: Page = page
```
--#

--% popup_menu_button.py
--#

--% progress_bar.py
--#

--% progress_ring.py
--#

--% protocol.py
```
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional

class CommandEncoder(json.JSONEncoder):
def default(self, obj):
    if isinstance(obj, Message):
        return obj.__dict__
    elif isinstance(obj, Command):
        d = {}
        return d
    elif isinstance(obj, object):
        return obj.__dict__
    return json.JSONEncoder.default(self, obj)

class Actions:
    REGISTER_HOST_CLIENT = "registerHostClient"
    SESSION_CREATED = "sessionCreated"
    PAGE_COMMAND_FROM_HOST = "pageCommandFromHost"
    PAGE_COMMANDS_BATCH_FROM_HOST = "pageCommandsBatchFromHost"
    PAGE_EVENT_TO_HOST = "pageEventToHost"

@dataclass
class Command:

@dataclass
class Message:

@dataclass
class PageCommandRequestPayload:

@dataclass
class PageCommandResponsePayload:

@dataclass
class PageCommandsBatchRequestPayload:

@dataclass
class PageCommandsBatchResponsePayload:

@dataclass
class PageEventPayload:

@dataclass
class RegisterHostClientRequestPayload:

@dataclass
class RegisterHostClientResponsePayload:

@dataclass
class PageSessionCreatedPayload:
```
--#

--% pubsub.py
```
import logging
import threading
from typing import Callable, Dict, Iterable

class PubSubHub:
    def __init__(self):
    def send_all(self, message: any):
    def send_all_on_topic(self, topic: str, message: any):
    def send_others(self, except_session_id: str, message: any):
    def send_others_on_topic(self, except_session_id: str, topic: str, message: any):
    def subscribe(self, session_id: str, handler: Callable):
    def subscribe_topic(self, session_id: str, topic: str, handler: Callable):
    def unsubscribe(self, session_id: str):
    def unsubscribe_topic(self, session_id: str, topic: str):
    def unsubscribe_all(self, session_id: str):
    def __unsubscribe(self, session_id: str):
    def __unsubscribe_topic(self, session_id: str, topic: str):
    def __send(self, handler: Callable, args: Iterable):

class PubSub:
    def __init__(self, pubsub: PubSubHub, session_id: str):
    def send_all(self, message: any):
    def send_all_on_topic(self, topic: str, message: any):
    def send_others(self, message: any):
    def send_others_on_topic(self, topic: str, message: any):
    def subscribe(self, handler: Callable):
    def subscribe_topic(self, topic: str, handler: Callable):
    def unsubscribe(self):
    def unsubscribe_topic(self, topic: str):
    def unsubscribe_all(self):
```
--#

--% radio.py
--#

--% radio_group.py
--#

--% reconnecting_websocket.py
--#

--% ref.py
```
from typing import Generic, TypeVar
T = TypeVar("T")
class Ref(Generic[T]):
    def __init__(self):
        self._current: T = None

    @property
    def current(self) -> T:
        return self._current

    @current.setter
    def current(self, value: T):
        self._current = value
```
--#

--% row.py
--#

--% shader_mask.py
--#

--% slider.py
--#

--% snack_bar.py
--#

--% stack.py
--#

--% switch.py
--#

--% tabs.py
--#

--% template_route.py
--#

--% text.py
--#

--% text_button.py
--#

--% textfield.py
--#

--% theme.py
--#

--% transform.py
--#

--% types.py
```
from typing import Union

from flet.animation import Animation
from flet.border_radius import BorderRadius
from flet.margin import Margin
from flet.padding import Padding
from flet.transform import Offset, Rotate, Scale

PaddingValue = Union[None, int, float, Padding]

MarginValue = Union[None, int, float, Margin]

BorderRadiusValue = Union[None, int, float, BorderRadius]

RotateValue = Union[None, int, float, Rotate]

ScaleValue = Union[None, int, float, Scale]

OffsetValue = Union[None, Offset]

AnimationValue = Union[None, bool, int, Animation]
```
--#

--% user_control.py

```
from typing import List

from flet.control import Control
from flet.stack import Stack

class UserControl(Stack):
    def build(self):
        pass

    def _build(self):
        content = self.build()
        if isinstance(content, Control):
            self.controls = [content]
        elif isinstance(content, List) and all(
            isinstance(control, Control) for control in content
        ):
            self.controls = content
        else:
            raise Exception(
                f"{self.__class__.__name__}.build() method must be implemented and returning either Control or List[Control]."
            )

    def _is_isolated(self):
        return True

```
--#

--% utils.py
--#

--% version.py
--#

--% vertical_divider.py
--#

--% view.py
--#
