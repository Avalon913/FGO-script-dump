# daily_update.py
# Step 1: read existing ScriptIDs from ids_all.txt

import os

def main():
    # 仓库根目录
    root_dir = os.path.dirname(os.path.dirname(__file__))

    # ids_all.txt 路径
    ids_file = os.path.join(root_dir, "tools", "ids_all.txt")

    # 已存在的 ScriptID 集合
    existing_ids = set()

    if os.path.exists(ids_file):
        with open(ids_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    existing_ids.add(line)

    print(f"已记录的 ScriptID 数量: {len(existing_ids)}")

if __name__ == "__main__":
    main()
