def wait_for_shortcut():

    import keyboard

    def on_hotkey(event=None):
        if event.name == 'ctrl+shift+b':
            print('ctrl+shift+b pressed!')
        elif event.name == 'ctrl+shift+f':
            print('ctrl+shift+f pressed!')
            exit_program()

    def exit_program():
        print('Exiting the function.')
        keyboard.unhook_all()
        exit()

    # Register the hotkeys
    keyboard.add_hotkey('ctrl+shift+b', on_hotkey)
    keyboard.add_hotkey('ctrl+shift+f', on_hotkey)

    try:
        print('ctrl+shift+f to quit')
        # Keep the program running until ctrl+shift+f is pressed
        keyboard.wait('ctrl+shift+f')
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C to exit gracefully
    finally:
        # Unregister the hotkeys (optional)
        keyboard.unhook_all()

# # Call the function to wait for the shortcut
# wait_for_shortcut()



def wait_for_shortcut_pynput():
    
    from pynput import keyboard

    def on_hotkey(key):
        try:
            if key == {keyboard.Key.ctrl, keyboard.Key.shift, 'a'}:
                print('Ctrl+Shift+A pressed!')
            elif key == {keyboard.Key.ctrl, keyboard.Key.shift, 'e'}:
                print('Ctrl+Shift+E pressed!')
                exit_program()
        except AttributeError:
            pass

    def exit_program():
        print('Exiting the function.')
        listener.stop()

    # Set up the listener
    with keyboard.Listener(on_press=on_hotkey) as listener:
        listener.join()
