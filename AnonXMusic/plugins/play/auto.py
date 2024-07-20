import random
import string

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message, InlineKeyboardButton
from pytgcalls.exceptions import NoActiveGroupCall
from config import START_IMG_URL
import config
from AnonXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from AnonXMusic.core.call import Alexa
from AnonXMusic.utils import seconds_to_min, time_to_seconds
from AnonXMusic.utils.channelplay import get_channeplayCB
from AnonXMusic.utils.database import is_video_allowed
from AnonXMusic.utils.decorators.language import languageCB
from AnonXMusic.utils.decorators.play import PlayWrapper
from AnonXMusic.utils.formatters import formats
from AnonXMusic.utils.inline.play import (
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from AnonXMusic.utils.inline.playlist import botplaylist_markup
from AnonXMusic.utils.logger import play_logs
from AnonXMusic.utils.stream.stream import stream
from config import BANNED_USERS, lyrical, CHANNEL_SUDO, YAFA_NAME, YAFA_CHANNEL
from strings import get_command
from AnonXMusic.utils.database import is_served_user
import asyncio

from pyrogram import filters, Client
from pyrogram import enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from AnonXMusic import Telegram, YouTube, app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.plugins.play.playlist import del_plist_msg
from AnonXMusic.plugins.sudo.sudoers import sudoers_list
from AnonXMusic.utils.database import (
    add_served_chat,
    is_served_user,
    add_served_user,
    blacklisted_chats,
    get_assistant,
    get_lang,
    get_userss,
    is_on_off,
    is_served_private_chat,
)
from AnonXMusic.utils.decorators.language import LanguageStart
from AnonXMusic.utils.inline import help_pannel, private_panel, start_pannel
from AnonXMusic.utils.command import commandpro

MESSAGE = f"""- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه

وبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.

ارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️

معرف البوت 🎸 [ @{app.username} ]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{app.username}"""


BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك ❤️✨",url=f"https://t.me/{app.username}?startgroup=True")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  



@app.on_message(filters.command(["اعلان للبوت"], ""))
async def auto_broadcast_command(client: Client, message: Message):
     await message.reply("**تم بدء نشر اعلان للبوت في جميع المجموعات، يرجى عدم تكرار الامر**")
     await send_message_to_chats()
     await message.reply("**تم الانتهاء من الاعلان في جميع خاص المستخزمين والمجموعات**")
