import threading
import concurrent.futures
from typing import Any, BinaryIO, Callable, Dict, Generic, Iterable, Iterator, List, Literal, NamedTuple, Optional, Sequence, TextIO, Tuple, Type, TypeVar, Union, TYPE_CHECKING, cast, overload

from .notifutils import notify


def mulai(funcs, args=(), kwargs=None):
    """
    perlukah:
    if isinstance(args, str):
        args = (args,)
    """
    t = threading.Thread(target=funcs, args=args, kwargs=kwargs)
    # t = threading.Thread(target=main_process, kwargs={'title':title})
    t.start()


# https://stackoverflow.com/questions/51601756/use-tqdm-with-concurrent-futures
# https://stackoverflow.com/questions/65547580/print-tqdm-progress-bar-from-external-python-script-called-by-subprocess
def startme(funcs, title='title', body='body', args=None, kwargs=None):
    mulai(funcs, args, kwargs)
    notify(title, body, duration=3)
    # notify(title, body)


def masa_depan(function, result: List[str], args=(), kwargs=None):
    if kwargs is None:
        kwargs = {}

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the function call to the executor
        future = executor.submit(function, *args, **kwargs)
        # Get the result of the function call
        function_result = future.result()

    # Store the result in the provided 'result' parameter
    result.append(function_result)


def masa_depan_dict(function, result: Dict, args=(), kwargs=None):
    if kwargs is None:
        kwargs = {}

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the function call to the executor
        future = executor.submit(function, *args, **kwargs)
        # Get the result of the function call
        function_result = future.result()
        # args[0] adlh key
        key = args[0]
        result[key] = function_result

    # # Store the result in the provided 'result' parameter
    # result.append(function_result)
