import json, time, traceback

if __name__ in ["myredis", "__main__"]:
    import os, sys

    curdir = os.path.dirname(__file__)
    schnelldir = os.path.join(curdir, os.pardir)
    sidoarjodir = os.path.join(schnelldir, os.pardir)
    sys.path.extend([sidoarjodir, schnelldir, curdir])
    from dotenv import load_dotenv

    load_dotenv(os.path.join(schnelldir, ".env"))

from schnell.db.myredis_common import (
    get_connection,
    try_redis_connect,
    redis_connect,
    redis_publish,
)
from schnell.db.redis_config import redis_config
from schnell.db.replservice import ReplService, repl_service
from schnell.db.redis_repl_from_vscode import redis_repl_from_vscode
from schnell.app.printutils import indah4


def redis_subscribe_getmessage(
    channel, pubsub, printer=print, message_callback=None, reply_channel=None
):
    """
    mengenai data yg datang ke kanal:
    redis_conn = redis.Redis(charset="utf-8", decode_responses=True)

    We can only publish messages of type string, bytes or float,
    but when the subscriber gets a message from the channel,
    it comes as a dictionary object:
    {
     "type": "message",
                    There are six types:
                            subscribe, unsubscribe, psubscribe, punsubscribe, message, pmessage.
                    We are only interested in the message type for this tutorial.
     "pattern": None,
     "channel": b"broadcast",
     "data": b"hello"
    }
    """

    try:
        message = (
            pubsub.get_message()
        )  # cek dokumentasi, https://stackoverflow.com/questions/7871526/is-non-blocking-redis-pubsub-possible

        if message:
            if printer:
                pesan = f"""[myredis_common][redis_subscribe] message: [{message['type']}] channel [{message['channel']}]"""
                printer(pesan)

            if message.get("type") == "message":
                # message punya type dan data, data bisa string atau dict
                data = json.loads(message.get("data"))

                if printer:
                    printer(
                        f"""
					{'*'*20}
					[db.myredis][redis_subscribe] kanal = [{channel}] menerima data berjenis [{type(data)}]:
					{data}
					{'*'*20}
					"""
                    )

                if isinstance(data, (bytes, bytearray, str)):
                    """
                    keluar dg
                    /Pub <nama kanal>|quit
                    {'type': 'message', 'pattern': None, 'channel': b'command', 'data': b'"hello baby"'}
                    """
                    if not isinstance(data, str):
                        data = data.decode("utf8")
                    if printer:
                        printer(f"""[db.myredis]terima Pub data: [{data}]""")
                    if data in ["quit", "bye", "exit", "q", "x"]:
                        return
                    else:
                        """
                        UPD 9 Jul 2022, handle dg replservice
                        tapi utk mengirim respond, client jg hrs mendengar dari kanal kedua
                        server mendengar di kanal: namakanal_request
                                mengirim ke kanal: namakanal_response
                        client mendengar di kanal: namakanal_response
                                mengirim ke kanal: namakanal_request
                        """
                        # hasil, meta = repl_service.process(content, meta_input=metacontent)
                        # data = {
                        # 	'content': hasil,
                        # 	'meta': meta,
                        # 	'original': metacontent,
                        # }
                        # redis_publish(data, redis_config['from_server'])
                        # upd 21/8/2022, kita mau tambah kanal response baru utk gui/system/search/widgets/creator
                        response_kanal = (
                            reply_channel
                            if reply_channel
                            else redis_config["response_kanal"]
                        )
                        # answer = f"We acknowledge your request: {data}."
                        answer, _ = repl_service.process(data)
                        redis_publish(answer, response_kanal)

                else:
                    # kirim jawaban
                    # redis_publish(f'SERVER TELAH PROSES {data}!', redis_config['from_server'])
                    try:
                        redis_repl_from_vscode(data)
                    except Exception as err:
                        indah4(
                            f"[db.myredis] Gagal: [{err}]\nwaktu minta jawaban dari repl service.",
                            warna="red",
                        )
                        indah4(traceback.format_exc(), warna="magenta")
                        if printer:
                            printer(
                                f"[{traceback.format_exc()}]\n{traceback.format_exc()}"
                            )
                        # kirim error ke client
                        data = {
                            # TypeError: Object of type UnexpectedCharacters is not JSON serializable
                            "content": str(err),
                            "original": data,
                        }
                        redis_publish(data, redis_config["from_server"])

                if message_callback:
                    message_callback(data, message)

    except KeyboardInterrupt:
        if printer:
            printer("KeyboardInterrupt")
    except EOFError:
        if printer:
            printer("EOFError")
    except Exception as err:
        if printer:
            printer(f"Exception: {err}")
            printer(traceback.format_exc())


def subscribe_header(channel):
    try_redis_connect()
    # if not r:
    r = get_connection("sub")
    try:
        pubsub = r.pubsub()
    except Exception as err:
        print('[myredis_common] "pubsub = r.pubsub()" => redis belum jalan:', err)
        print("[myredis_common] redis_config:", redis_config)
        try_redis_connect()
        time.sleep(1.0)
        r = get_connection("sub")
        pubsub = r.pubsub()
        print("[myredis_common][redis_subscribe]", r)

    pubsub.subscribe(channel)
    return pubsub


def main():
    # listen ke 'replservice_request'
    # channel = redis_config['request_kanal']
    # # r = redis_connect()
    # try_redis_connect()
    # # if not r:
    # r = get_connection('sub')
    # try:
    # 	pubsub = r.pubsub()
    # except Exception as err:
    # 	print('[myredis_common] "pubsub = r.pubsub()" => redis belum jalan:', err)
    # 	print('[myredis_common] redis_config:', redis_config)
    # 	try_redis_connect()
    # 	time.sleep(1.0)
    # 	r = get_connection('sub')
    # 	pubsub = r.pubsub()
    # 	print('[myredis_common][redis_subscribe]', r)

    # pubsub.subscribe(channel)
    channel = redis_config["request_kanal"]
    pubsub = subscribe_header(channel)
    while True:
        redis_subscribe_getmessage(channel, pubsub)
        time.sleep(0.001)


if __name__ == "__main__":
    main()
