import os
import json as j

# SAMPLE

# PATH_JSONS = r'C:\Users\User\Desktop\tmp\DNS\dns-routers-characteristics-jsons'
# PATH_OUT_JSON = r'C:\Users\User\Desktop\tmp\DNS\dns-routers-characteristics-json'


def jsons_to_json(path_json: str, path_out_json: str):
    jsons = []
    for json in os.listdir(PATH_JSONS):
        with open(fr"{path_json}\{json}", 'r', encoding='utf-8') as f:
            jsons.append(j.loads(f.read())['data'])
    with open(path_out_json, 'w', encoding='utf-8') as f:
        f.write(j.dumps(jsons))


jsons_to_json(PATH_JSONS, PATH_OUT_JSON)