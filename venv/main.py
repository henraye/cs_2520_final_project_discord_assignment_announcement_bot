from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
#Reference from: https://youtu.be/UYJDKSah-Ww?si=JpRQE6e1kJjoNgQS

#Step 0: Load token from .env file(To use, add your own)
load_dotenv()
TOKEN: Final = os.getenv('DISCORD_TOKEN') 

#Step 1: Bot setup
intents=Intents.default()
intents.message_content=True
client: Client = Client(intents=intents)

#Step 2: MESSAGE_FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message is empty because intents were not enabled.")
        return
    #provide a private response if the message starts with a question mark
    if is_private :=user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response: str=get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#Step 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')

@client.event
#Step 4: HANDLING THE MESSAGE FUNCTIONALITY
async def on_message(message: Message) -> None:
    #ignore messages from the bot itself
    if message.author == client.user:
        return
    
    username : str=str(message.author)
    user_message: str=message.content
    channel: str=str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#Step 5: Main
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()