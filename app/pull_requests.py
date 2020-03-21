from . import config


def url(
        per_page=None,
        page=None,
        state=None,
        base_branch=None,
):
    if per_page is None:
        per_page = config.PER_PAGE
    if state is None:
        state = 'all'
    if base_branch is None:
        base_branch = config.BRANCH
    request_template = '/repos/{owner}/{repo}/pulls?per_page={per_page}'.format(
        owner=config.OWNER,
        repo=config.REPO,
        per_page=per_page,
    )
    filters = [
        ('&page={}', page),
        ('&state={}', state),
        ('&base={}', base_branch),
    ]
    for f in filters:
        request_template = config.construct_request(request_template, *f)
    return config.GITHUB_API + request_template


def base_branch(x):
    return x['base']['ref']


def get_created_at(x):
    return x['created_at']


def get_state(x):
    return x['state']
