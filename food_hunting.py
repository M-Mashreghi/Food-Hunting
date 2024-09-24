# -*- coding: utf-8 -*-

!pip install telethon
!pip install nest_asyncio

import nest_asyncio
import asyncio
from telethon.sync import TelegramClient, events
api_id = 
api_hash = ''
group_target ='@self_ut'

async def reply_to_hi(event):
    message = event.message.message
    chat = await event.get_chat()
    message = message.lower()

    conditions = [
        'فنی بالا دارم' == message,
        'بالا دارم.' == message,
        'فنی بالا' == message,
        'فنی بالا دارم.' == message,
        'بالا دارم' == message,
        'fanni bala daram' == message,
        'fanni bala' == message,
    ]
    excluded_words = ['پایین', 'فیزیک', 'مدیریت', 'سلف مهر', 'کوی', 'تعویض', 'میخوام']

    if any(conditions) and not any(word in message for word in excluded_words):

        reply_message = f'اس'
        await event.reply(reply_message)

        user = await event.get_sender()

        async with event.client.conversation(user, timeout=10) as conv:
            await conv.send_message('سلام')


async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        client.add_event_handler(reply_to_hi, events.NewMessage(chats=[group_target]))
        print("Listening for messages...")
        await client.run_until_disconnected()

if __name__ == '__main__':
    nest_asyncio.apply()  # Apply nest_asyncio here
    asyncio.run(main())

