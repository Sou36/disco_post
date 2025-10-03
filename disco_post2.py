from playwright.sync_api import sync_playwright
import json
import random
import os

save_n = 0
savetrue = 0
json_savedore = 0
memo = ""
json_kakidasu = input("jsonから書き出しますか？(y/n): ")
if json_kakidasu == "y":
  json_savedore = int(input("読み込むファイルの番号を書いて(例:save1.jsonなら1と入力): "))
  with open(f"save{json_savedore}.json", "r", encoding="utf-8") as f:# jsonを読み出してloaded_dataに入れる
     loaded_data = json.load(f)
  print(loaded_data)
  saisyuu_kakunin = input("上の内容で合ってますか？(y/n): ")

  if saisyuu_kakunin == "y":
   count = loaded_data["count"]
   severid = loaded_data["severid"]
   channelid = loaded_data["channelid"]
   randomumu = loaded_data["randomumu"]
else:
 count = int(input("回数: "))
 print("設定→詳細設定→開発者モードをオンにして右クリックで取得出来ます↓")
 severid = int(input("サーバーID:"))
 channelid = int(input("チャンネルID:"))
 randomumu = input("入力する言葉をランダムにしますか？(y/n): ")
 print("jsonを保存します...")
 memo = input("識別するためのメモを入力: ")
 while savetrue != 1:
   if os.path.isfile(f"save{save_n}.json"):
     pass
   else:
     savetrue = 1
   save_n += 1
 
 data = {"count": f"{count}", "severid": f"{severid}","channelid": f"{channelid}","randomumu":f"{randomumu}","memo":f"{memo}"}  
 with open(f"save{save_n}.json", "w", encoding="utf-8") as f:# jsonに保存
    json.dump(data, f, ensure_ascii=False, indent=2)
 print(f"save{save_n}.jsonが保存されました")
 
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
      randomsuuji = int(random.randint(0,len(tango) - 1))
      page.fill('div[role="textbox"]',tango[randomsuuji])
      page.press('div[role="textbox"]', "Enter")
     if randomumu == "n":
      page.fill('div[role="textbox"]',f"{tango}")
      page.press('div[role="textbox"]', "Enter")
     page.wait_for_timeout(14000)
    browser.close()





