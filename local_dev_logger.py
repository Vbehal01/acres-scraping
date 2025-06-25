import os
import subprocess
from datetime import datetime, date
import random

REPO_DIR = "D:\\Learning\\data_scraping"
LAST_RUN_FILE = os.path.join(REPO_DIR, ".last_update.log")
LOG_FILE = os.path.join(REPO_DIR, "dev_notes.md")

COMMIT_MESSAGES = [
    "docs: update dev notes",
    "chore: added today's update to dev log",
    "docs: daily progress entry",
    "style: adjusted formatting in dev_notes",
    "refactor: improve log structure slightly"
]

def already_ran_today():
    if not os.path.exists(LAST_RUN_FILE):
        return False
    with open(LAST_RUN_FILE, "r") as f:
        last_date = f.read().strip()
        return last_date == str(date.today())

def update_last_run_date():
    with open(LAST_RUN_FILE, "w") as f:
        f.write(str(date.today()))

def append_dev_notes():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# Developer Notes\n\n")
    with open(LOG_FILE, "a") as f:
        f.write(f"- {datetime.now().strftime('%Y-%m-%d %H:%M')} - Worked on optimization and cleanup tasks.\n")

def git_commit_push():
    os.chdir(REPO_DIR)
    subprocess.run(["git", "add", "."], check=False)
    commit_msg = random.choice(COMMIT_MESSAGES)
    subprocess.run(["git", "commit", "-m", commit_msg], check=False)
    subprocess.run(["git", "push"], check=False)

if __name__ == "__main__":
    if not already_ran_today():
        append_dev_notes()
        git_commit_push()
        update_last_run_date()
    else:
        print("Dev notes already updated today.")
