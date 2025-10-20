
from pyrogram import Client, filters
from pyrogram.types import Message
from info import ADMINS
import os

@Client.on_message(filters.command("view_utils") & filters.user(ADMINS))
async def view_utils_file(client, message: Message):
    """
    This command allows admins to view the contents of the utils.py file.
    """
    try:
        with open("utils.py", "r") as file:
            content = file.read()

        # Truncate the content if it's too long for a single message
        if len(content) > 4096:
            content = content[:4090] + "\n..."

        await message.reply_text(f"```\n{content}\n```")
    except FileNotFoundError:
        await message.reply_text("Error: `utils.py` not found.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
