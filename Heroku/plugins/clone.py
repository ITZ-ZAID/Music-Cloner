import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from Heroku import cloner, ASSUSERNAME

@cloner.on_message(filters.private & filters.command("start"))
async def hello(client, message: Message):
    await message.reply("Hey! It's Just a Cloner Bot example source Code")

##Copy from here 

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@cloner.on_message(filters.private & filters.command("clone"))
async def clone(bot, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Heroku.modules"})
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @{ASSUSERNAME} To Your Chat!\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!

