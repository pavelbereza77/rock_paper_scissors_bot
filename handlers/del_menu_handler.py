from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()


@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer('Кнопка меню удалена', reply_markup=ReplyKeyboardRemove())
