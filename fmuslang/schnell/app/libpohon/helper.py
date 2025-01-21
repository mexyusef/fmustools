from schnell.app.treeutils import (
    assignment_paramlist_type,
    ASSIGNMENT_PARAMLIST_PREFIX,
    ASSIGNMENT_PARAMLIST_COMMA,
    ASSIGNMENT_PARAMLIST_NEWLINE0,
    ASSIGNMENT_PARAMLIST_NEWLINE1,

    assignment_firstcolumn,
    assignment_paramlist,
    assignment_paramlist_value,
    assignment_pydict_all,
    assignment_pydict_first,
    assignment_pydict_rest,
    ASSIGNMENT_FIRSTCOLUMN,
    ASSIGNMENT_PARAMLIST_SIMPLE,
    ASSIGNMENT_PARAMLIST_VALUE,
    ASSIGNMENT_PYDICT_ALL,
    ASSIGNMENT_PYDICT_FIRST,
    ASSIGNMENT_PYDICT_REST,
)


def detect_replace_assignment(table_string_content, TableNode, pemetaan=None):
    """
    digunakan di .app_content
    for TableNode in RootNode.children:
        content = detect_replace_assignment(content, TableNode, pemetaan=provider)
    """
    if ASSIGNMENT_PARAMLIST_PREFIX in table_string_content or \
        ASSIGNMENT_FIRSTCOLUMN in table_string_content or \
        ASSIGNMENT_PYDICT_ALL in table_string_content or \
        ASSIGNMENT_PYDICT_FIRST in table_string_content or \
        ASSIGNMENT_PYDICT_REST in table_string_content:

        table_string_content = table_string_content \
            .replace(ASSIGNMENT_PARAMLIST_SIMPLE, assignment_paramlist(TableNode)) \
            .replace(ASSIGNMENT_PARAMLIST_VALUE, assignment_paramlist_value(TableNode)) \
            .replace(ASSIGNMENT_PARAMLIST_COMMA, assignment_paramlist_type(TableNode, pemetaan, delimiter=', ', num_tab=0)) \
            .replace(ASSIGNMENT_PARAMLIST_NEWLINE0, assignment_paramlist_type(TableNode, pemetaan, delimiter='\n', num_tab=0)) \
            .replace(ASSIGNMENT_PARAMLIST_NEWLINE1, assignment_paramlist_type(TableNode, pemetaan, delimiter='\n', num_tab=1)) \
            .replace(ASSIGNMENT_FIRSTCOLUMN, assignment_firstcolumn(TableNode)) \
            .replace(ASSIGNMENT_PYDICT_ALL, assignment_pydict_all(TableNode)) \
            .replace(ASSIGNMENT_PYDICT_FIRST, assignment_pydict_first(TableNode)) \
            .replace(ASSIGNMENT_PYDICT_REST, assignment_pydict_rest(TableNode)) \

    return table_string_content

