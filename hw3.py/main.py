import asyncio
from aiogram import Bot, Dispatcher
from config import token
from handlers import start, regular, basketball, luxury, order

bot = Bot(token=token)
dp = Dispatcher()


dp.include_router(start.router)
dp.include_router(regular.router)
dp.include_router(basketball.router)
dp.include_router(luxury.router)
dp.include_router(order.router)

async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


