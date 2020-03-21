from . import config


def url(
        sha=None,
        # begin_date=None,
        # end_date=None,
        per_page=None,
        page=None,
):
    if per_page is None:
        per_page = config.PER_PAGE
    if sha is None:
        sha = config.BRANCH

    request_template = '/repos/{owner}/{repo}/commits?per_page={per_page}'.format(
        owner=config.OWNER,
        repo=config.REPO,
        per_page=per_page,
    )
    filters = [
        ('&sha={}', sha),
        # ('&since={}', begin_date),
        # ('&until={}', end_date),
        ('&page={}', page),
    ]
    for f in filters:
        request_template = config.construct_request(request_template, *f)
    return config.GITHUB_API + request_template


def get_date(x):
    return x['commit']['author']['date']


def get_login(x):
    return x['author']['login']
