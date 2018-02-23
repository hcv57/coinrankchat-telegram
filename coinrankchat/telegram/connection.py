from getpass import getpass
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError

from . import config

def _setup_client():
    client = TelegramClient(
        config.TELEGRAM_SESSION,
        config.TELEGRAM_API_ID,
        config.TELEGRAM_API_HASH,
        update_workers = 4,
        spawn_read_thread=False)

    assert client.connect()

    if not client.is_user_authorized():
        client.send_code_request(config.TELEGRAM_PHONE)
        code_ok = False
        while not code_ok:
            code = input('Enter the auth code: ') or 'NOCODE'
            try:
                code_ok = client.sign_in(config.TELEGRAM_PHONE, code)
            except PhoneCodeInvalidError:
                print('Invalid code')
            except SessionPasswordNeededError:
                password = getpass('Two step verification enabled. Please enter your password: ')
                code_ok = client.sign_in(password=password)
    print('INFO: Client initialized succesfully!')
    return client

client = _setup_client()