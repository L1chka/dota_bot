from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import  get_keyboard,get_keyboard_2
bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_command(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description=' команда для того что бы купить бластоун '),
        types.BotCommand(command='/help', description=' команда для того что бы купить BKB ')
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет любитель доты , ты попался в мою ловушку теперь ты вечно будешь играть на бристе и хускаре ', reply_markup= get_keyboard())

@dp.message_handler(lambda message: message.text == '1 скилл')
async def button_1_click(message: types.Message):
    await message.reply('ты прожал первый скиилл')

@dp.message_handler(lambda message: message.text == '2 скилл')
async def button_2_click(message: types.Message):
    await message.answer('ты прожал второй скиилл')

@dp.message_handler(lambda message: message.text == '3 скилл')
async def button_3_click(message: types.Message):
    await message.answer('ты прожал третий скиилл')

@dp.message_handler(lambda message: message.text == '4 скилл')
async def button_4_click(message: types.Message):
    await message.answer('ты прожал четвертый  скиилл')

@dp.message_handler(lambda message: message.text == 'ульта')
async def button_5_click(message: types.Message):
    await message.reply('ты прожал ульту')

@dp.message_handler(lambda message: message.text == 'SF')
async def button_6_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://pm1.aminoapps.com/7266/c551b64f4011e11657ff9f66755c4ad3574ca482r1-564-846v2_uhq.jpg', caption= 'Держи гуленыш недоделаный ')

@dp.message_handler(lambda message: message.text == 'перейти на 2 клаву')
async def button_7_click(message: types.Message):
    await message.reply('больше возможностей ',reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'хускар')
async def button_8_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://cybersport.metaratings.ru/storage/images/55/08/55082fa3db71526d0d8be65f174c3d9b.png', caption= 'Держи армлет в хлебало ')

@dp.message_handler(lambda message: message.text == 'байбек')
async def button_7_click(message: types.Message):
    await message.reply('больше возможностей ',reply_markup= get_keyboard() )



@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Тебе нужнa помощь на хускаре или бристе? Чел ты...... ')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispathcer):
    await set_command(dispathcer.bot)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates= True, on_startup= on_startup)
