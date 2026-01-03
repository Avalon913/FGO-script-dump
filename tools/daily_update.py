import requests

BASE_URL = "https://api.atlasacademy.io"
REGION = "JP"

def main():
    url = f"{BASE_URL}/nice/{REGION}/scripts"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    data = resp.json()
    ids = [str(item["id"]) for item in data]

    print(f"当前 ScriptID 总数: {len(ids)}")
    print("前 10 个 ScriptID：")
    for sid in ids[:10]:
        print(sid)

if __name__ == "__main__":
    main()
