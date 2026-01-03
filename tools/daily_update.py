import requests

URL = "https://api.atlasacademy.io/export/JP/script.json"

def main():
    resp = requests.get(URL, timeout=60)
    resp.raise_for_status()

    data = resp.json()

    ids = [str(item["id"]) for item in data]

    print(f"ScriptID 总数: {len(ids)}")
    print("前 10 个 ScriptID：")
    for sid in ids[:10]:
        print(sid)

if __name__ == "__main__":
    main()
