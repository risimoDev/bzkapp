
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Устанавливаем уровень логов для отладки
logging.basicConfig(level=logging.INFO)

# Создаем экземпляр бота и диспетчера
bot = Bot(token='bot_token')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Отправляем приветственное сообщение
    await message.reply('Приветствуем вас в BZK-PRINT!\n\nУ нас вы можете распечатать или отсканировать документы, также  мы можем изготовить для вас все виды полиграфической продукции (листовки, визитки, одежду с принтом или вышивкой, наклейки, кружки, фотографии, каталоги, журналы и книги, корпоративные сувениры, блокноты, календари) с высочайшим качеством и в кратчайшие сроки! \n\nМы используем современное оборудование, а также расходные материалы самого высокого качества.\n\n Так же вы можете написать нам в телеграм или оставить заявку прямо в этом боте\n\nНаш прайс - bzk-print.ru/price.php\nМы ВКонтакте - vk.com/bzkprint\nМы в телеграм - @bzk_print')

# Обработчик всех остальных сообщений от пользователей
@dp.message_handler()
async def user_message(message: types.Message):
    # Получаем id пользователя, отправившего сообщение
    user_id = message.from_user.id

    # Отправляем пользователю сообщение о том, что его заявка принята
    await message.reply('Ваша заявка отправлена!')

    # Получаем id администратора (можно задать заранее или получить из базы данных)
    admin_id = 7190590865

    # Отправляем заявку администратору
    await bot.send_message(chat_id=admin_id, text=f'Новая заявка от пользователя с id {user_id}:\n{message.text}')

# Обработчик команды /sendbigms только для администраторов
@dp.message_handler(commands=['sendbigms'])
async def send_big_message(message: types.Message):
    # Проверяем, является ли отправитель администратором (можно задать заранее или получить из базы данных)
    if message.from_user.id == 7190590865:
        # Получаем список всех пользователей бота
        users = await bot.get_chat_members(chat_id=-1001657565315)
        
        # Отправляем массовую рассылку всем пользователям бота
        for user in users:
            await bot.send_message(chat_id=user.user.id, text='Это массовая рассылка от администратора')
    else:
        # Отправляем сообщение о том, что доступ к команде запрещен
        await message.reply('У вас нет доступа к этой команде.')

# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
