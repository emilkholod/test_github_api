GITHUB_API = 'https://api.github.com'

OWNER = 'fastlane'
REPO = 'fastlane'

PER_PAGE = 1
# max value of PER_PAGE  = 100
MAX_PER_PAGE = 100

# YYYY-MM-DDTHH:MM:SSZ
BEGIN_DATE = '2019-01-0100:00:00Z'
END_DATE = '2020-01-0100:00:00Z'
BRANCH = 'master'

USERNAME = ''
PASSWORD = ''


def construct_request(request_in, filter_template, filter):
    if filter is not None:
        request_in = request_in + filter_template.format(filter)
    return request_in
