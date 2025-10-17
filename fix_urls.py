from urllib.parse import urlparse

# SAMPLE

# PATH_URLS = r'C:\Users\User\Desktop\tmp\Organisations\www\www.txt'
# PATH_FIX_URL_OUT = r'C:\Users\User\Desktop\tmp\Organisations\www\www_fix.txt'


def fix_list_org_www(path: str):
    urls_fix = []
    with open(path, 'r') as f:
        urls = f.readlines()
        for url in urls:
            urls_pipe = url.split("|")                      # pipe fix
            for url_pipe in urls_pipe:
                url_fixed = fix_schema(url_pipe.strip())    # schema fix
                parsed = urlparse(url_fixed)
                parsed_fix = parsed._replace(path='', params='', query='', fragment='')
                urls_fix.append(parsed_fix.geturl())
    return urls_fix


def fix_schema(url: str, default_schema: str = "http"):
    if not url.startswith(("http", "https")):
        return f"{default_schema}://{url}"
    return url


def run():
    urls = fix_list_org_www(PATH_URLS)
    with open(PATH_FIX_URL_OUT, 'w') as f:
        for url in urls:
            f.write(f"{url}\n")


run()
