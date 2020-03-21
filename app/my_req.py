import json

import requests

from . import config

session = requests.Session()
if not (config.USERNAME == '' or config.PASSWORD == ''):
    session.auth = (config.USERNAME, config.PASSWORD)
else:
    print(
        'Добавьте свой файл настроек с логином и паролем в папку instance, иначе github выбросит ошибку 403 спустя несколько запросов!'
    )


def get(url):
    resp = session.get(url)
    if not resp.status_code == 200:
        msg = 'Вышло следующее сообщение от сервера.\n'
        msg += f'Код от сервера: {resp.status_code}\n'
        msg += (resp.content).decode()
        raise Exception(msg)
    return resp


def get_last_page(r):
    return int(r.links['last']['url'].split('&page=')[1])


def get_content(r):
    return json.loads(r.content)
