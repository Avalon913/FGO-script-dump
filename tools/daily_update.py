import requests

# 测试用：一个已知存在的 ScriptID
SCRIPT_ID = "0100000010"

URL = f"https://apps.atlasacademy.io/db/JP/script/{SCRIPT_ID}.json"

def main():
    resp = requests.get(URL, timeout=30)
    print("HTTP 状态码:", resp.status_code)

    if resp.status_code != 200:
        print("请求失败")
        return

    data = resp.json()

    print("成功获取 Script JSON")
    print("包含的字段：", list(data.keys()))
    print("text 行数:", len(data.get("text", [])))

if __name__ == "__main__":
    main()
