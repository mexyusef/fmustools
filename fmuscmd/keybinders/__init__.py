# from keybinders import terima_prompt
def terima_prompt(event):
    event.app.current_buffer.text = ""
    event.app.current_buffer.validate_and_handle()  # jk empty bs terima input
