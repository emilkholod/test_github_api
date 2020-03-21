import datetime

from . import commits
from . import issues
from . import pull_requests as pr
from . import utils


def get_most_active_users_in_commits(req_handler, count_active_users=30):
    print('\n---Задача: Самые активные участники.')
    contents = utils.get_content(req_handler, commits, commits.get_date)

    print('Обработка страниц:')
    logins = {}
    for con in contents:
        try:
            l = commits.get_login(con)
            logins[l] = logins.get(l, 0) + 1
        except TypeError as e:
            print('---Не найден логин у следующего коммита:---')
            print(con)
            print('---Пропускаем ошибку---')
            pass

    most_active_users = sorted(logins.items(),
                               key=lambda item: item[1],
                               reverse=True)[:count_active_users]
    print('Список пользователей с наибольшим количеством коммитов:')
    print(''.join([f'{user} - {count}\n'
                   for user, count in most_active_users]))


def count_open_closed_pull_requests(req_handler):
    print('\n---Задача: Количество открытых и закрытых pull requests')
    contents = utils.get_content(req_handler, pr, pr.get_created_at)
    print('Обработка страниц:')
    ans = {}
    ans['open'] = 0
    ans['closed'] = 0
    for con in contents:
        ans[pr.get_state(con)] += 1
    print('Количество открытых и закрытых pull requests:')
    print(ans)


def count_old_pull_requests(req_handler):
    print('\n---Задача: Количество "старых" pull requests')
    contents = utils.get_content(req_handler, pr, pr.get_created_at)
    print('Обработка страниц:')
    count_old_request = 0
    for con in contents:
        if pr.get_state(con) == 'open':
            created_at = datetime.datetime.strptime(pr.get_created_at(con),
                                                    "%Y-%m-%dT%H:%M:%SZ")
            if (datetime.datetime.now() - created_at).days > 30:
                count_old_request += 1

    print('Количество "старых" pull requests:')
    print(count_old_request)


def count_open_closed_issues(req_handler):
    print('\n---Задача: Количество открытых и закрытых issues')
    contents = utils.get_content(req_handler, issues, issues.get_created_at)
    print('Обработка страниц:')
    ans = {}
    ans['open'] = 0
    ans['closed'] = 0
    for con in contents:
        if not 'pull_request' in con:
            ans[issues.get_state(con)] += 1
    print('Количество открытых и закрытых issues:')
    print(ans)


def count_old_issues(req_handler):
    print('\n---Задача: Количество "старых" issues')
    contents = utils.get_content(req_handler, issues, issues.get_created_at)
    print('Обработка страниц:')
    count_old_issues = 0
    for con in contents:
        if not 'pull_request' in con and issues.get_state(con) == 'open':
            created_at = datetime.datetime.strptime(issues.get_created_at(con),
                                                    "%Y-%m-%dT%H:%M:%SZ")
            if (datetime.datetime.now() - created_at).days > 14:
                count_old_issues += 1

    print('Количество "старых" issues:')
    print(count_old_issues)
