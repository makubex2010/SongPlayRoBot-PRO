from pyrogram.types.messages_and_media import message
from config import OWNER_ID
from pyrogram import filters
from pyrogram.errors import BadRequest
from TamilBots import app
import TamilBots.sql.blacklist_sql as sql
from TamilBots.TamilBots import get_arg


@app.on_message(filters.user(OWNER_ID) & filters.command("blacklist"))
async def blacklist(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user["id"]
    else:
        arg = get_arg(message)
        if len(arg) != 1:
            await message.reply(
                "傳遞用戶 ID 或用戶名或回復用戶消息"
            )
            return ""
        if arg.startswith("@"):
            try:
                user = await app.get_users(arg)
                user_id = user.id
            except BadRequest as ex:
                await message.reply("不是有效用戶")
                print(ex)
                return ""
        else:
            user_id = int(arg)
        sql.add_user_to_bl(int(user_id))
        await message.reply(f"[blacklisted](tg://user?id={user_id})")


@app.on_message(filters.user(OWNER_ID) & filters.command("unblacklist"))
async def unblacklist(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user["id"]
    else:
        arg = get_arg(message)
        if len(arg) != 1:
            await message.reply(
                "傳遞用戶 ID 或用戶名或回復用戶消息"
            )
            return ""
        if arg.startswith("@"):
            try:
                user = await app.get_users(arg)
                user_id = user.id
            except BadRequest:
                await message.reply("不是有效用戶")
                return ""
        else:
            user_id = int(arg)
        sql.rem_user_from_bl(int(user_id))
        await message.reply(f"[unblacklisted](tg://user?id={user_id})")
