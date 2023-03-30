import json
from aiogram import Bot,Dispatcher,executor,types
from auth_data import token


bot = Bot(token=token)
dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def get_all_news(message: types.Message):
#     await message.reply('Whats up Doc?')

@dp.message_handler(commands='all_news')
async def get_all_news(message: types.Message):
    with open('news_dict.json',encoding='utf-8') as file:
        news_dict = json.load(file)

    for k,v in news_dict.items():
        
        news = f"{v['time:']}\n{v['title:']}\n{v['details:']}\n{v['url:']}"

        await message.answer(news)


if __name__ == '__main__':
    executor.start_polling(dp)

