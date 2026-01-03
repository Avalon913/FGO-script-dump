import requests

URL = "https://apps.atlasacademy.io/db/JP/script"

def main():
    resp = requests.get(URL, timeout=30)

    print("HTTP 状态码:", resp.status_code)
    print("响应前 500 字符：")
    print(resp.text[:500])

if __name__ == "__main__":
    main()
