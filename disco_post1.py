from playwright.sync_api import sync_playwright
import sys

stop = input("前回のログイン情報ファイルが残っていれば使い回す事が出来ますが、実行しますか？(y/n): ")
if stop == "n":
  sys.exit(0)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://discord.com/login")

    print("開いたブラウザで手動でログイン、ログイン後にここで Enter を押す。")
    input()

    # ログイン後の状態を保存
    context.storage_state(path="./discord_login.json")
    print("ログイン情報を discord_login.json に保存しました。")
    browser.close()
