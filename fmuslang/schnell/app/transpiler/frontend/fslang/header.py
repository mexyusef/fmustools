from app.fileutils import (
  file_copy,
  replace_entry,
  get_definition_by_key_permissive_start,
  replace_string_in_entry,
)
from app.dirutils import (
  joiner, ayah
)
from .common import program_config, disini


header_left = """
<Nav className="nav mr-auto" navbar>
__TEMPLATE_HEADER_LEFT_CONTENT
</Nav>
"""

header_right = """
<Nav className="ml-auto" navbar>
__TEMPLATE_HEADER_RIGHT_CONTENT
</Nav>
"""

header_title = """
<Nav.Item>
  <Nav.Link
    data-toggle="dropdown"
    href="#fulgent"
    onClick={(e) => e.preventDefault()}
    className="m-0"
  >
    <i className="nc-icon nc-palette"></i>
    <span className="d-lg-none ml-1">Dashboard</span>
  </Nav.Link>
</Nav.Item>
"""

header_search = """
<Nav.Item>
  <Nav.Link
    className="m-0"
    href="#fulgent"
    onClick={(e) => setShowModal(true)}
  >
    <i className="nc-icon nc-zoom-split"></i>
    <span className="d-lg-block"> Search</span>
  </Nav.Link>
</Nav.Item>
"""

header_account = """
<Nav.Item>
  <Nav.Link
    className="m-0"
    href="#fulgent"
    onClick={(e) => setShowModal(true)}
  >
    <span className="no-icon">Account</span>
  </Nav.Link>
</Nav.Item>
"""

header_logout = """
<Nav.Item>
  <Nav.Link
    className="m-0"
    href="#fulgent"
    onClick={(e) => setShowModal(true)}
  >
    <span className="no-icon">Log out</span>
  </Nav.Link>
</Nav.Item>
"""

header_dropdown_badge = """
<Dropdown as={Nav.Item}>

  <Dropdown.Toggle
    as={Nav.Link}
    data-toggle="dropdown"
    id="dropdown-67443507"
    variant="default"
    className="m-0"
  >
    <i className="nc-icon nc-planet"></i>
    <span className="notification">5</span>
    <span className="d-lg-none ml-1">Notification</span>
  </Dropdown.Toggle>

  <Dropdown.Menu>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tc', 'primary')}
    >
      Notification 1
    </Dropdown.Item>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tc', 'primary')}
    >
      Notification 2
    </Dropdown.Item>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tc', 'primary')}
    >
      Notification 3
    </Dropdown.Item>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tc', 'primary')}
    >
      Notification 4
    </Dropdown.Item>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tc', 'primary')}
    >
      Another notification
    </Dropdown.Item>
  </Dropdown.Menu>

</Dropdown>
"""

header_dropdown_color = """
<Dropdown as={Nav.Item}>
  <Dropdown.Toggle
    aria-expanded={false}
    aria-haspopup={true}
    as={Nav.Link}
    data-toggle="dropdown"
    id="navbarDropdownMenuLink"
    variant="default"
    className="m-0"
  >
    <span className="no-icon">Dropdown</span>
  </Dropdown.Toggle>

  <Dropdown.Menu aria-labelledby="navbarDropdownMenuLink">
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tr', 'success')}
    >
      Action
    </Dropdown.Item>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tr', 'success')}
    >
      Another action
    </Dropdown.Item>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tr', 'success')}
    >
      Something
    </Dropdown.Item>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tr', 'success')}
    >
      Something else here
    </Dropdown.Item>
    <div className="divider"></div>
    <Dropdown.Item
      href="#fulgent"
      onClick={()=>pemberitahuan.current.notify('tr', 'success')}
    >
      Separated link
    </Dropdown.Item>
  </Dropdown.Menu>

</Dropdown>
"""

def process_header():
  template = program_config['fe']
  filepath = joiner(disini, f'{template}/header.mk')
  # baris = 'index/fmus'
  baris = '/react-light/src/components/Navbars/AdminNavbar.js'
  content = get_definition_by_key_permissive_start(filepath, baris)
  if content:
    frontend_config['header'] = content
