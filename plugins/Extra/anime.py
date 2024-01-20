import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from info import PREFIX
from helper.utils import Automato

API_URL = "https://api.nekosapi.com/v2/images/random"


@Automato.on_message(filters.command(["anime"], Config.PREFIX) & filters.private)
async def random_anime(client: Client, message: Message):
    # Send the "Processing..." message
    dx = await message.reply_text("Fetching a random anime image...")

    # Make the API request
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()["data"]["attributes"]
        image_url = data["file"]
        title = data["title"]
    except (requests.exceptions.RequestException, KeyError):
        await dx.edit("Failed to fetch a random anime image.")
        return

    # Send the image and title as a reply
    await client.send_photo(message.chat.id, image_url, caption=f"**Title:** {title}")

    # Edit the original message to indicate success
    await dx.edit("Random anime image sent!")
