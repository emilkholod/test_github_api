from . import my_req, tasks

req_handler = my_req

if __name__ == '__main__':
    tasks.get_most_active_users_in_commits(req_handler)
    tasks.count_open_closed_pull_requests(req_handler)
    tasks.count_old_pull_requests(req_handler)
    tasks.count_open_closed_issues(req_handler)
    tasks.count_old_issues(req_handler)
