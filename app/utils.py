import datetime

from . import config


def get_obj_number_since_date(req_handler, some_date, obj, func_get_date=None):
    if func_get_date is None:
        func_get_date = obj.get_date
    t2 = datetime.datetime.strptime(some_date, "%Y-%m-%d%H:%M:%SZ")
    url = obj.url(per_page=1)
    r = req_handler.get(url)

    last_page = req_handler.get_last_page(r)

    page_begin_from = 1
    page_end = last_page + 1

    # binary search
    last_page = page_begin_from
    while (True):
        central_page = page_begin_from + (page_end - page_begin_from) // 2
        url = obj.url(per_page=1, page=central_page)
        r = req_handler.get(url)
        central_obj = req_handler.get_content(r)[0]
        date_of_obj = func_get_date(central_obj)
        t1 = datetime.datetime.strptime(date_of_obj, "%Y-%m-%dT%H:%M:%SZ")
        if t1 > t2:
            page_begin_from = central_page
            page_end = page_end
        else:
            page_begin_from = page_begin_from
            page_end = central_page
        if last_page == central_page:
            break
        last_page = central_page
    return last_page


def get_request_number_pages(req_handler,
                             obj,
                             begin_date=None,
                             end_date=None,
                             func_get_date=None):
    if begin_date is None:
        begin_date = config.BEGIN_DATE
    if end_date is None:
        end_date = config.END_DATE

    print('Получение порядковых номеров объектов с требуемыми датами')
    finish_with_commit = get_obj_number_since_date(req_handler, begin_date,
                                                   obj, func_get_date)
    start_from_commit = get_obj_number_since_date(req_handler, end_date, obj,
                                                  func_get_date) + 1

    start_from_page = (start_from_commit // config.MAX_PER_PAGE) + 1
    finish_with_page = (finish_with_commit // config.MAX_PER_PAGE) + 2
    return (
        start_from_commit,
        finish_with_commit,
        start_from_page,
        finish_with_page,
    )


def get_obj_from_pages(
        req_handler,
        obj,
        start_from_page,
        finish_with_page,
        start_from_commit,
        finish_with_commit,
):
    for page_num in range(start_from_page, finish_with_page):
        print(page_num - start_from_page + 1, '/',
              finish_with_page - start_from_page)
        url = obj.url(per_page=config.MAX_PER_PAGE, page=page_num)
        r = req_handler.get(url)
        content = req_handler.get_content(r)
        if page_num == start_from_page:
            content = content[start_from_commit % config.MAX_PER_PAGE - 1:]
        if page_num == finish_with_page - 1:
            content = content[:finish_with_commit % config.MAX_PER_PAGE]
        yield from content


def get_content(req_handler, obj, func_get_date=None):
    (
        start_from_commit,
        finish_with_commit,
        start_from_page,
        finish_with_page,
    ) = get_request_number_pages(req_handler, obj, func_get_date=func_get_date)

    contents = get_obj_from_pages(req_handler, obj, start_from_page,
                                  finish_with_page, start_from_commit,
                                  finish_with_commit)
    return contents
