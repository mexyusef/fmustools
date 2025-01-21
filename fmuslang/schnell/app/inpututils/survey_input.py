import survey


def input_survey_text(prompt):
    return survey.routines.input(prompt)


def input_survey_text_area(prompt='Limited Message: ', max_chars=180):
    # https://survey.readthedocs.io/reference.html
    # limit = 50
    def info(widget, name, info):
        result = widget.resolve().rstrip('\n')
        remain = max_chars - len(result)
        if remain < 0:
            raise survey.widgets.Abort('no characters left')
        return str(remain)
    value = survey.routines.input(prompt, multi = True, info = info)
    print(f'Answered with {len(value)} characters.')
    return value


def input_survey_numeric(prompt):  # float/decimal/double
    return survey.routines.numeric(prompt)


def input_survey_integer(prompt):
    return survey.routines.numeric(prompt, decimal=False)


def input_survey_datetime(prompt):
    """
    C:\work\ciledug\ciledug\fmusperintah\vendor\survey\survey\_widgets.py
    _DateTime_funnel_enter_arrange_attr_groups = (
        ('year', 'month', 'day'),
        ('hour', 'minute', 'second')
    )

    attrs = ('hour', 'minute')
    """
    return survey.routines.datetime(prompt)


def input_survey_date(prompt):
    """
    attrs = ('hour', 'minute')
    """
    return survey.routines.datetime(prompt, attrs = ('day', 'month', 'year'))


def input_survey_time(prompt):
    """
    attrs = ('hour', 'minute')
    """
    return survey.routines.datetime(prompt, attrs = ('hour', 'minute'))


def input_survey_boolean(prompt, default=True):
    return survey.routines.inquire(prompt, default=default)


def input_survey_password(prompt):
    return survey.routines.conceal(prompt)


def input_survey_select(prompt, options, focus_mark = '👉 '):
    """
    focus_mark
    evade_mark
    focus_color = survey.colors.basic('magenta')
    evade_color = survey.colors.basic('yellow')
    positive_mark = '✅ '
    negative_mark = '❌ '
    """
    index = survey.routines.select(prompt, options=options, focus_mark=focus_mark)
    return options[index]


# def input_survey_multiselect(prompt, options):
#     return survey.routines.basket(prompt, options=options)
def input_survey_multiselect(prompt, options):
    selected_indices = survey.routines.basket(prompt, options=options)
    return [options[index] for index in selected_indices]


def test_survey_input():
    name = input_survey_text("What's your name? ")
    age = input_survey_numeric("How old are you? ")
    birthday = input_survey_datetime("Enter your birthday: ")
    confirm = input_survey_boolean("Do you confirm? (y/n) ")
    password = input_survey_password("Enter your password: ")
    color = input_survey_select("What's your favorite color? ", options=["Red", "Green", "Blue"])
    hobbies = input_survey_multiselect("Select your hobbies: ", options=["Reading", "Writing", "Traveling"])

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Birthday: {birthday}")
    print(f"Confirmation: {confirm}")
    print(f"Password: {'*' * len(password)}")
    print(f"Favorite Color: {color}")
    print(f"Hobbies: {', '.join(hobbies)}")
    print("END.")
    print()


def print_survey():
    """
    https://survey.readthedocs.io/reference.html

    Printers
    Functions that print to the console with optional sentiment using marks.

    survey.printers.text(*values, sep=' ', end='\\n', re=False)
        Print a plain value. Works similar to print().

        Parameters
        :
        values – Used to create the final value by mapping all with str() and concatenating with text.sep.

        end (str) – Appended to the end of the final value.

        re (bool) – Whether to return the cursor to the last saved position before printing.

    survey.printers.info(*values, mark='!', mark_color=<fg:cyan>, **kwargs)
        Print a value denoting information.

        Parameters
        :
        values – Same as text.value.

        mark (str) – Prepended to the final value.

        mark_color (str) – Used to color info.mark with.

        Additional arguments are passed to text().

    survey.printers.done(*values, mark='✔', mark_color=<fg:green>, **kwargs)
        Print a value denoting success.

        Parameters
        :
        values – Same as text.value.

        mark (str) – Prepended to the final value.

        mark_color (str) – Used to color info.mark with.

        Additional arguments are passed to text().

    survey.printers.fail(*values, mark='✘', mark_color=<fg:red>, **kwargs)
        Print a value denoting failure.

        Parameters
        :
        values – Same as text.value.

        mark (str) – Prepended to the final value.

        mark_color (str) – Used to color info.mark with.

        Additional arguments are passed to text().

    """
    color = survey.colors.basic('cyan')
    colored = survey.utils.paint(color, 'I am blue!') 
    survey.printers.text(colored) # "I am blue", but cyan

# https://survey.readthedocs.io/reference.html
# survey.routines.form(*args, reply=<function _form_reply>, **kwargs)

#     Use an Form widget.

#     The default hint shows available controls, including of focused widgets.

#     All widget and start() arguments are valid.

#     🎨 Theme with 'routines.form'
#     _images/routines.form-1.gif

#     form = {
#         'name': survey.widgets.Input(),
#         'price': survey.widgets.Count(),
#         'type': survey.widgets.Select(options = ('food', 'stationary', 'tobacco', 'literature'))
#     }
#     data = survey.routines.form('Item Data: ', form = form)

def input_form(title="Item data: "):
    """
    field:s
    field:i
    field:d
    field:t
    field:dt
    field:p
    field:enum=satu,dua,tiga,empat
    """
    form = {
        'name': survey.widgets.Input(),
        'price': survey.widgets.Count(),
        'type': survey.widgets.Select(options = ('food', 'stationary', 'tobacco', 'literature'))
    }
    data = survey.routines.form(title, form = form)
    print(f"""input_form
    jenis data = {type(data)}
    data = {data}
    """)
# ? Item Data: 
#  name: usef
# price: 42
#  type: tobacco
# input_form
#     jenis data = <class 'dict'>
#     data = {'name': 'usef', 'price': 42, 'type': 2}


if __name__ == '__main__':
    input_form()
