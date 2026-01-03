import requests
import os
import hashlib
from datetime import date

URL = "https://git.atlasacademy.io/atlasacademy/fgo-game-data/-/raw/master/mstQuestScript.json"

ROOT = os.path.dirname(os.path.dirname(__file__))
RAW_DIR = os.path.join(ROOT, "raw")
UPDATES_DIR = os.path.join(ROOT, "updates", date.today().isoformat())

RAW_FILE = os.path.join(RAW_DIR, "mstQuestScript.json")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(UPDATES_DIR, exist_ok=True)

def file_hash(path):
    if not os.path.exists(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def main():
    print("Downloading mstQuestScript.json ...")
    resp = requests.get(URL, timeout=120)
    resp.raise_for_status()
    data = resp.content

    old_hash = file_hash(RAW_FILE)
    new_hash = hashlib.sha256(data).hexdigest()

    if old_hash == new_hash:
        print("No update detected.")
        return

    # 写 raw
    with open(RAW_FILE, "wb") as f:
        f.write(data)

    # 写 updates
    update_file = os.path.join(UPDATES_DIR, "mstQuestScript.json")
    with open(update_file, "wb") as f:
        f.write(data)

    print("Update detected.")
    print("Saved to raw/ and updates/")

if __name__ == "__main__":
    main()
