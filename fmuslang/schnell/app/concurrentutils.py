from concurrent.futures import ThreadPoolExecutor
from threading import Timer
import asyncio


"""
The ThreadPoolExecutor offers an extremely simple interface for running functions
in a thread—and the best part is that, if needed, you can convert the pool of threads
into a pool of subprocesses simply by using ProcessPoolExecutor instead.

In general, you’ll prefer your tasks to be somewhat short-lived, so that when your
program needs to shut down, you can simply call Executor.shutdown(wait=True)
and wait a second or two to allow the executor to complete.
"""

def worker(data):
    # <process the data>
    with ThreadPoolExecutor(max_workers=10) as exe:
        future = exe.submit(worker, data)


def twoArgs(arg1,arg2):
    print (arg1)
    print (arg2)
    print ("")


def nArgs(*args):
    for each in args:
        print (each)


def sample_timer():
    #arguments: 
    #how long to wait (in seconds), 
    #what function to call, 
    #what gets passed in
    r = Timer(1.0, twoArgs, ("arg1","arg2"))
    s = Timer(2.0, nArgs, ("OWLS","OWLS","OWLS"))

    r.start()
    s.start()


def sample_call_later():
    loop = asyncio.get_event_loop()

    def callback():
        print("callback")
        loop.call_later(1, callback)

    loop.call_later(1, callback)

    async def main():
        while True:
            await asyncio.sleep(1)

    loop.run_until_complete(main())


def sample_call_later2():
    loop = asyncio.get_event_loop()
    loop.call_soon(print, "I am scheduled on a loop!")
    loop.call_soon_threadsafe(print, "I am scheduled on a loop but threadsafely!")
    loop.call_later(1, print, "I am scheduled on a loop in one second")
    loop.call_at(loop.time() + 1, print, "I am scheduled on a loop in one second too")


def setTimeout(seconds, func, *args):
    loop = asyncio.get_event_loop()
    loop.call_later(seconds, func, *args)
    try:
        print("Stop the loop by hitting the CTRL+C keys...")

        # To see the callbacks running you need to start the running loop

        # loop.run_forever()

        async def main():
            while True:
                await asyncio.sleep(1)
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()


def nanti(detik, fungsi, *args):
    t = Timer(detik*1.0, fungsi, *args)
    t.start()


def nantisystem(detik, cmdargs):
    if not isinstance(detik, int):
        detik = int(detik) * 1.0
    from .utils import perintah
    t = Timer(detik, perintah, (cmdargs,))
    t.start()

