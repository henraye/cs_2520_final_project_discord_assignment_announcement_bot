from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Game, Status
from responses import get_response
#Reference from: https://youtu.be/UYJDKSah-Ww?si=JpRQE6e1kJjoNgQS

# Step 0: Load token and channel IDs from .env file
load_dotenv()
TOKEN: Final = os.getenv('DISCORD_TOKEN')
SPECIFIC_CHANNEL_ID: Final = os.getenv('SPECIFIC_CHANNEL_ID')
PUBLIC_CHANNEL_ID: Final = os.getenv('PUBLIC_CHANNEL_ID')

if not TOKEN or not SPECIFIC_CHANNEL_ID or not PUBLIC_CHANNEL_ID:
    raise ValueError("One or more environment variables are missing. Please check your .env file.")

SPECIFIC_CHANNEL_ID = int(SPECIFIC_CHANNEL_ID)
PUBLIC_CHANNEL_ID = int(PUBLIC_CHANNEL_ID)

# Step 1: Bot setup
intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Step 2: MESSAGE_FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message is empty because intents were not enabled.")
        return
    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# Step 3: HANDLING STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')


@client.event
# Step 4: HANDLING THE MESSAGE FUNCTIONALITY
async def on_message(message: Message) -> None:
    # Ignore messages that come from the bot itself
    if message.author == client.user:
        return
    
    #Bot reading user name and message from a certain channel
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')

    # Admin sends message in private channel, bot responds in a specific channel (like an annoucement channel)
    if message.channel.id == SPECIFIC_CHANNEL_ID:
        print(f"Message received in specific channel: {SPECIFIC_CHANNEL_ID}")
        public_channel = client.get_channel(PUBLIC_CHANNEL_ID)
        if public_channel:
            response: str = get_response(user_message)
            await public_channel.send(response)
            print(f"Sent message to public channel: {PUBLIC_CHANNEL_ID}")
        else:
            print("Public channel not found.")
    else:
        await send_message(message, user_message)

# Step 5: Main
def main() -> None:
    client.run(TOKEN)

if __name__ == "__main__":
    main()