import subprocess, threading

from schnell.app.dirutils import joiner

###################### ctrl+q
def bind_key_q(bindings):
    @bindings.add("c-q", 'b')  # qute browser
    def _(event):
        from common_import import sidoarjodir
        program = joiner(sidoarjodir, 'schnell/vendor/browser/qute.py')
        x = threading.Thread(target=subprocess.run, kwargs={'args':f'python {program}'.split()})
        x.start()
    ######################################
    # @bindings.add("c-q", 'q')  # scratchpad, ternyata gak bisa, krn di luar loop
    # def _(event):
    #     from schnell.app.richtextual.scratchpad import main
    #     main()

    # @bindings.add("c-q", 'c-j')
    # def _(event):
    # 	event.app.current_buffer.text = "ctrl+q ctrl+j"
