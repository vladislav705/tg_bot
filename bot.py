
# Use this token to access the HTTP API:
# 5901195749:AAEzSxWowMMPWmI-d4_zp60tSt7X_XMushQ


print('Включаем бота!!!!!')
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '5901195749:AAEzSxWowMMPWmI-d4_zp60tSt7X_XMushQ'
 




bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def problem_solver(message: types.Message):

	ikb = InlineKeyboardMarkup(row_width=2)

	ib1 = InlineKeyboardButton(text='У меня бракованный товар', callback_data='f1')
	ib2 = InlineKeyboardButton(text='Товар не пришел', callback_data='f2')
	ib3 = InlineKeyboardButton(text='Прочее, связаться со специалистом', callback_data='f3')
	ikb.add(ib1)
	ikb.add(ib2)
	ikb.add(ib3)

	await bot.send_message(chat_id=message.chat.id, 
   	text="Привет, выбери проблему из списка:\n",
   	parse_mode="HTML", 
   	reply_markup=ikb)


	await message.delete()







 
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	ikb = InlineKeyboardMarkup(row_width=2)

	ib1 = InlineKeyboardButton(text='Дать обратную связь', callback_data='feedback')
	ib2 = InlineKeyboardButton(text='Получить информацию о бренде', callback_data='info')
	ib3 = InlineKeyboardButton(text='Ссылка на наш сайт', url='https://www.wildberries.ru/brands/14895683-LeSte')
	ib4 = InlineKeyboardButton(text='У меня возникла проблема', callback_data='problem')
	ikb.add(ib1)
	ikb.add(ib2)
	ikb.add(ib3)
	ikb.add(ib4)
	await bot.send_message(chat_id=message.from_user.id, 
   	text="Привет, Лена!\nЯ Шаблон бота!\nВыбери опцию которую ты хочешь задействовать",
   	parse_mode="HTML", 
   	reply_markup=ikb)
	await message.delete()


@dp.callback_query_handler()
async def bla_callback(callback: types.CallbackQuery):
	if callback.data == 'info':
		await callback.message.answer('Leste это таааакая крутая компания) вот наш логотип')

	elif callback.data == 'feedback':
		await callback.message.answer('ура, отзыв, напишите его ниже')
	elif callback.data == 'problem':
		await problem_solver(message=callback.message)
		await callback.answer()



	elif callback.data == 'f1':
		await callback.message.answer('Не повезло вам(')
	elif callback.data == 'f2':
		await callback.message.answer('Напишите в WB')
	elif callback.data == 'f3':
		await callback.message.answer('Их пока не наняли(')


@dp.message_handler()
async def echo(message: types.Message):
   await message.answer('Повторяю за тобой: '+message.text+ ". Если пишешь текстом, то умею только повторять. Хотя можешь научить меня обрабатывать слова")



 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)





