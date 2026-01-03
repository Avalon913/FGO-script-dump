# daily_update.py
# Step 2: fetch ScriptID list from Atlas Academy (read-only)

import os
import requests

BASE_URL = "https://api.atlasacademy.io"
REGION = "JP"

def main():
    # 仓库根目录
    root_dir = os.path.dirname(os.path.dirname(__file__))

    # ids_all.txt 路径
    ids_file = os.path.join(root_dir, "tools", "ids_all.txt")

    # 1. 读取本地已有的 ScriptID
    existing_ids = set()
    if os.path.exists(ids_file):
        with open(ids_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    existing_ids.add(line)

    print(f"本地已有 ScriptID 数量: {len(existing_ids)}")

    # 2. 从 Atlas Academy 获取 Script 列表
    url = f"{BASE_URL}/nice/{REGION}/script"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    data = resp.json()
    remote_ids = set(str(item["id"]) for item in data)

    print(f"Atlas Academy 当前 ScriptID 数量: {len(remote_ids)}")

    # 3. 计算差异（只打印）
    new_ids = remote_ids - existing_ids
    print(f"检测到新增 ScriptID 数量: {len(new_ids)}")

if __name__ == "__main__":
    main()
