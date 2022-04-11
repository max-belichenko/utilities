def join_urls(url: str, path: str):
    """
    Собирает полный URL-адрес из базового URL и пути к ресурсу.

    Пример:
        get_full_url(url='http://www.hostname.com:80/', path='/path/to/resource/')
        # 'http://www.hostname.com:80/path/to/resource/'
    """
    return str(url).rstrip('/') + '/' + str(path).lstrip('/')
