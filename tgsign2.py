import asyncio
from telethon import TelegramClient

api_ids = [123456, 654321]  # 输入api_id，一个账号一项
api_hashes = ['0123456789abcdef0123456789abcdef', 'abcdef0123456789abcdef0123456789']  # 输入api_hash，一个账号一项
bot_username = "@luxiaoxun_bot"  # 机器人用户名

async def checkin(api_id, api_hash):
    session_name = f"id_{api_id}"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    await client.send_message(bot_username, '/checkin')
    await client.send_read_acknowledge(bot_username)
    print(f"Done! Session name: {session_name}")
    await client.disconnect()

async def main():
    tasks = [checkin(api_id, api_hash) for api_id, api_hash in zip(api_ids, api_hashes)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
