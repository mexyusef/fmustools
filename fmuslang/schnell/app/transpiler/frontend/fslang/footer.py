from app.fileutils import (
  file_copy,
  replace_entry,
  get_definition_by_key_permissive_start,
  replace_string_in_entry,
)
from .common import program_config, disini


footer_list = """
<ul className="footer-menu">
__ITEMS__
</ul>
"""

footer_item = """
<li>
  <a href="#fulgent" onClick={(e) => e.preventDefault()}>
    __TITLE__
  </a>
</li>
"""

footer_copyright = """
<p className="copyright text-center">
  © {new Date().getFullYear()}{" "}
  <a href="http://fulgent.de">Fulgent</a>, made with love for a better web
</p>
"""

def process_footer():
  template = program_config['fe']
  filepath = joiner(disini, f'{template}/footer.mk')
  baris = '/react-light/src/components/Footer/Footer.js'
  content = get_definition_by_key_permissive_start(filepath, baris)
  # print('footer content:', content, 'dari file:', filepath)
  if content:
    frontend_config['footer'] = content
