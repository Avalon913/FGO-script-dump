import requests

SCRIPT_ID = "0400060020"
URL = f"https://apps.atlasacademy.io/db/JP/script/{SCRIPT_ID}.json"

def main():
    resp = requests.get(URL, timeout=30)
    print("HTTP 状态码:", resp.status_code)

    if resp.status_code != 200:
        print("请求失败")
        print(resp.text[:200])
        return

    data = resp.json()

    print("成功获取 Script JSON")
    print("字段：", list(data.keys()))
    print("text 行数：", len(data.get("text", [])))
    print("前 5 行文本：")
    for line in data.get("text", [])[:5]:
        print(line)

if __name__ == "__main__":
    main()
