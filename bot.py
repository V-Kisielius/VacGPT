import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_handler
import os
from dotenv import load_dotenv
load_dotenv()

async def main():
    bot = Bot(token=os.environ['TG_TOKEN'])
    dp = Dispatcher()

    dp.include_router(user_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())