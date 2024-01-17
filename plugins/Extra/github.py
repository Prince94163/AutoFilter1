import os
import requests
import pyrogram
import json
from info import SUPPORT_CHAT
from pyrogram import Client as Koshik
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters


def github(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    msg = update.effective_message
    if len(args) != 2:
        update.effective_message.reply_text("/github Username")
        return
    username = args[1]
    URL = f'https://api.github.com/users/{username}'
    result = requests.get(URL).json()
    try:
        m = msg.reply_text("`Searching.....`")
        url = result['html_url']
        name = result['name']
        company = result['company']
        bio = result['bio']
        created_at = result['created_at']
        avatar_url = result['avatar_url']
        blog = result['blog']
        location = result['location']
        repositories = result['public_repos']
        followers = result['followers']
        following = result['following']
        caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
        m.delete()
        update.effective_message.reply_photo(avatar_url, caption=caption,reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Profile",
                            url=url,
                        ),
                    ],
                ],
            ), parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(str(e))
        update.effective_message.reply_text(f"ERROR!! Contact @{SUPPORT_CHAT}")
        pass

git_handler = CommandHandler(("git", "github"), github, run_async = True)
dispatcher.add_handler(git_handler)

__mod_name__ = "Github 🐱‍💻"
__help__ = """
Here is help for Github

 ❍ `/github` <username> - Get information from a profile on GitHub.
 ❍ `/git` <username> - Get information from a profile on GitHub.
"""
