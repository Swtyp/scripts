# SAMPLE

# PATH_LOG = r"C:\Users\English_folder\Firefox-Extensions\dns-get-ids\console-export-2025-9-15_2-11-38.log"
# PATH_URLS = r"C:\Users\English_folder\Firefox-Extensions\dns-get-ids\dns-urls.txt"
# URL = "https://www.dns-shop.ru/pwa/pwa/get-product/?id="


def to_urls(path_input: str, path_out: str, url: str):
    with open(path_out, 'w', encoding="utf-8") as ff:
        with open(path_input, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                ff.write(f"{url}{line.split(' ')[0]}\n")


if __name__ == '__main__':
    to_urls(PATH_LOG, PATH_URLS, URL)

