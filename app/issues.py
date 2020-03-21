from . import config


def url(
        state=None,
        per_page=None,
        page=None,
):
    if per_page is None:
        per_page = config.PER_PAGE
    if state is None:
        state = 'all'
    request_template = '/repos/{owner}/{repo}/issues?per_page={per_page}'.format(
        owner=config.OWNER,
        repo=config.REPO,
        per_page=per_page,
    )
    filters = [
        ('&state={}', state),
        ('&page={}', page),
    ]
    for f in filters:
        request_template = config.construct_request(request_template, *f)
    return config.GITHUB_API + request_template


def get_created_at(x):
    return x['created_at']


def get_state(x):
    return x['state']
