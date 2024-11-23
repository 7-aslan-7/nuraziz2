# import asyncio
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters import CommandStart, Command
# from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
# from config import token
# from aiogram import Router

# bot = Bot(token=token)
# dp = Dispatcher()
# # router = Router()


# buttons = [
#     [KeyboardButton(text='Повседневные'), KeyboardButton(text='Баскетбольные')],
#     [KeyboardButton(text='Коллекция люкс')]]

# regular_shoes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Jordan 4 Retro'), KeyboardButton(text='ASICS Gel-1130'), KeyboardButton(text='Nike Zoom Vomero 5')]])

# basketball_shoes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Nike Kobe 5'), KeyboardButton(text='adidas AE 1'), KeyboardButton(text='Nike Kobe 9 Elite Protro')]])

# lux_edition = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Louis Vuitton LV Trainer'), KeyboardButton(text='Nike SB Dunk Low'), KeyboardButton(text='Nike Air Skylon 2')]])

# keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')

# # dp.include_router(router)

# @dp.message(CommandStart())
# async def command_start(message: types.Message):
#     await message.answer('Приветствую вас !', reply_markup=keyboard)
#     await message.answer('Выберите пожалуйста категорию: ')

# async def main():
#         await dp.start_polling(bot)

# info_jordan = ('Описание продукта:\n\n'
# 'Jordan 4 Retro OG SP A Ma Maniére While You Were Sleeping (женская) — это последнее дополнение к продолжающемуся сотрудничеству Jordan Brand и A Ma Maniére, известных сочетанием роскошных материалов с вневременным дизайном. Этот релиз отличается верхом из высококачественной замши и кожи из окаменелого камня, что создает изысканный, но в то же время смелый образ. Контрастные черные акценты на межподошве добавляют глубину дизайну, а на язычке одной пары кроссовок изображена культовая бирка Jumpman, а на другой — логотип A Ma Maniére.'
# )

# info_asics = ('Описание продукта\n\n'
# 'ASICS Gel-1130 White Black — это кроссовки для бега с дизайном, уходящим корнями в технические беговые кроссовки начала 2000-х годов.\n\n'
# 'Версия ASICS Gel-1130 «White Black» черпает вдохновение в GEL-KAYANO 14 и девятой итерации серии GEL-1000. Хотя модель была впервые представлена ​​в 2008 году, эта версия имеет полностью белую основу с черными и серебристыми акцентами. Верх выполнен из легкой сетки со свободным плетением, что придает кроссовкам ощущение воздушности. Накладки из синтетической кожи пересекают сетчатую основу и вносят вклад в технический силуэт обуви. С точки зрения технологии, гелевая амортизация в пятке снижает ударную нагрузку, не утяжеляя обувь. Фирменная система поддержки ASICS TRUSSTIC также улучшает устойчивость и является возвратом к началу 2000-х годов.')

# info_nike_vomero = ('Описание продукта\n\n'
# 'Кроссовки Nike Zoom Vomero 5 Photon Dust Metallic Silver (W) выпускаются в следующих цветовых гаммах: Photon Dust, Chrome, Gridiron и Sail. Кроссовки\n\n'

# 'Photon Dust Metallic Silver Nike Zoom Vomero 5 (W) имеют верх из воздухопроницаемой ткани, что обеспечивает воздухопроницаемость и комфорт. В кроссовках используется технология амортизации Zoom Air от Nike, которая обеспечивает отзывчивую амортизацию с возвратом энергии. Кроссовки также оснащены мягкой и поддерживающей подошвой из мягкой пены. Кроссовки оснащены фиксатором пятки из термополиуретана, который обеспечивает устойчивость и снижает риск скольжения. Прочная резиновая подошва кроссовок имеет вафельный рисунок для сцепления. Кроссовки украшены логотипом Nike Swoosh по бокам, надписью «NIKE VOMERO 5» на язычке и небольшим логотипом Swoosh на пятке.')

# info_kobe_5 = ('Описание продукта\n\n'
# 'Nike Kobe 5 Protro X-Ray — это яркая дань уважения легендарной карьере Коби Брайанта, вдохновленная культовой футболкой X-ray, на которой была изображена его рука, украшенная пятью чемпионскими кольцами. Переосмысливая эту концепцию, дизайн X-ray нанесен на верхнюю часть Kobe 5 с элементами, светящимися в темноте, изображающими рентгеновский снимок стопы. Выполненные в глубоком королевском синем, балтийском синем и ледниковом синем цветах, эти смелые кроссовки также имеют светящуюся в темноте подошву, что добавляет дополнительный слой изюминки и без того поразительному силуэту.')

# info_adidas = ('Описание продукта\n\n'
# 'Adidas AE 1 Ascent добавляет гладкую цветовую гамму Charcoal и Core Black к первым фирменным кроссовкам игрока NBA Энтони Эдвардса с adidas.\n\n'

# 'Средняя по высоте модель Ascent adidas AE 1 установлена ​​на легкой подошве Jet Boost и LightStrike с покрытием из ТПУ, которая находит поддержку в полноразмерной торсионной пластине. В то время как верх изготовлен из плотно сплетенной сетки, боковые панели из ТПУ с сотовой конструкцией поддерживают обувь и позволяют ноге дышать. Боковые панели из ТПУ также имеют мраморный рисунок в цвете Charcoal, который выделяет «Ascent» среди других моделей adidas AE 1. Хотя кроссовки могут похвастаться минимальным количеством фирменных деталей, прорезиненный логотип с тремя полосками украшает формованную заднюю часть пятки.')

# @dp.message(F.text == 'Повседневные')
# async def command_regular(message: types.Message):
#     await message.answer('В наличии: ', reply_markup=regular_shoes)

# @dp.message(F.text == 'Jordan 4 Retro')
# async def command_jordan(message: types.Message):
#     await message.reply_photo(photo='https://spikeprague.cz/cdn/shop/files/eb020bfedc19497fc8266bf91ee3ce05_700x700.webp?v=1727947987')
#     await message.answer(info_jordan)
#     await message.answer('Цена на данную модель состовляет: 85$')
    
# @dp.message(F.text == 'ASICS Gel-1130')
# async def command_asics(message: types.Message):
#     await message.reply_photo(photo='https://www.freesoulz.nl/cdn/shop/files/asics-gel-1130-white-black-724065.jpg?v=1725547494&width=2048')
#     await message.answer(info_asics)
#     await message.answer('Цена на данную модель состовляет: 95$') 

# @dp.message(F.text == 'Nike Zoom Vomero 5')
# async def command_nike(message: types.Message):
#     await message.reply_photo(photo='https://www.sneakerhype.eu/cdn/shop/products/nike-zoom-vomero-5-photon-dust-metallic-silver-w-sneakerhype-2.webp?v=1731074702')
#     await message.answer(info_nike_vomero)
#     await message.answer('Цена на данную модель состовляет: 92$') 

# @dp.message(F.text == 'Баскетбольные')
# async def command_basketball(message: types.Message):
#     await message.answer('В налачии: ', reply_markup=basketball_shoes)
    
    
# @dp.message(F.text == 'Nike Kobe 5')
# async def command_kobe(message: types.Message):
#     await message.reply_photo(photo='https://cdn.eql.media/draw-api/aub862ba-af88-47b7-91e7-10af7320ed51/ed1f30db-5bf6-4587-81de-ee1152972f17.png?auto=format&ar=1%3A1&fit=crop&ixlib=react-9.7.0&w=580')
#     await message.answer(info_kobe_5)
#     await message.answer('Цена на данную модель состовляет: 181$')
    
# @dp.message(F.text == 'adidas AE 1')
# async def command_adidas(message: types.Message):
#     await message.reply_photo(photo='https://www.basketballemotion.com/imagesarticulos/223344/grandes/zapatillas-adidas-a.e.-1-cloud-white-core-black-green-spark-0.webp')
#     await message.answer(info_adidas)
#     await message.answer('Цена на данную модель состовляет: 77$')
    
# # @dp.message(F.text == '')
# # async def command_kobe(message: types.Message):
# #     await message.reply_photo(photo='')
# #     await message.answer(inf)
# #     await message.answer('Цена на данную модель состовляет: ')
    
# # @dp.message(F.text == '')
# # async def command_kobe(message: types.Message):
# #     await message.reply_photo(photo='')
# #     await message.answer(info_adidas)
# #     await message.answer('Цена на данную модель состовляет: ')






# @dp.message(F.text == 'Nike Kobe 5')
# async def command_asics(message: types.Message):
#     await message.reply_photo(photo='https://www.dtlr.com/cdn/shop/files/Nike_HM9522_20400_GS086.jpg?v=1731109125')
#     await message.answer(info_kobe_5)
#     await message.answer('Цена на данную модель состовляет: 181$')


    
# @dp.message(F.text == 'ASICS Gel-1130')
# async def command_asics(message: types.Message):
#     # await message.reply_photo(photo=)
#     await message.answer()
#     await message.answer('Цена на данную модель состовляет: ') 


# if __name__ == "__main__":
#     asyncio.run(main())