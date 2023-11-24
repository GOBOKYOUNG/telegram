import asyncio
import datetime
import sys
import time

import pytz
import schedule
import telegram

sys.path.append(r'C:\users\user\anaconda3\lib\site-packages')

# function
def send_message():
    chat_id = "6504124318"
    bot_token = "6486863471:AAFrifp_oH40to4f2GXuz0uQ1LJwQ4MV8_M"
    bot = telegram.Bot(token=bot_token)

    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    str_now = str(now)
    asyncio.run(bot.sendMessage(chat_id=chat_id, text = '안뇽!'))

send_message()
schedule.every(30).minutes.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)