import requests
import json

URL = "https://raw.githubusercontent.com/atlasacademy/data/master/JP/Script.json"

def main():
    resp = requests.get(URL, timeout=60)
    resp.raise_for_status()

    data = resp.json()

    # Script.json 是一个列表
    ids = [str(item["id"]) for item in data]

    print(f"ScriptID 总数: {len(ids)}")
