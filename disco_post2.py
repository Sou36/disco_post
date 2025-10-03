from playwright.sync_api import sync_playwright
import random


count = int(input("回数: "))
print("設定→詳細設定→開発者モードをオンにして右クリックで取得出来ます↓")
severid = int(input("サーバーID:"))
channelid = int(input("チャンネルID:"))
randomumu = input("入力する言葉をランダムにしますか？(y/n): ")
if randomumu == "y":
    tango = ["おはようございます","こんにちは","こんばんは","おやすみなさい"]#ここ！
if randomumu == "n":
    tango = input("送信したい言葉を入力: ")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="discord_login.json")
    page = context.new_page()
    page.goto("https://discord.com/channels/@me") #最初に開く画面
    page.wait_for_timeout(5000)
    page.locator(f'div[data-list-item-id="guildsnav___{severid}"]').first.click()
    page.wait_for_timeout(1000)
    page.locator(f'a[data-list-item-id="channels___{channelid}"]').first.click()
    page.wait_for_timeout(1000)
    for i in range(count):
     page.locator(f'div[role="textbox"]').first.click()
     page.wait_for_timeout(1000)
     if randomumu == "y":
      randomtango = random.randint(0,len(tango))
      page.fill(f"{randomtango}")
     if randomumu == "n":
      page.fill(f"{tango}")
     page.wait_for_timeout(14000)
    browser.close()




