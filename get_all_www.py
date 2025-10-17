import json
import os

# SAMPLE

# PATH_ENTRY = r'C:\Users\User\Desktop\tmp\Organisations\res_search'
# PATH_OUT = r'C:\Users\User\Desktop\tmp\Organisations\www'
# LIST_DIR = os.listdir(PATH_ENTRY)

with open(f"{PATH_OUT}\\www.txt", 'w') as w:
    for name_file in LIST_DIR:
        with open(f"{PATH_ENTRY}\\{name_file}", 'r', encoding='utf-8') as f:
            orgns_json = json.loads(f.read())
            for request in orgns_json["requests"]:
                if len(request["result"]) != 0 and request["result"][0]["www"] != "":
                    w.write(f'{request["result"][0]["www"]}\n')
