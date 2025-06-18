from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import FSInputFile
import asyncio
import json
from aiogram.utils.chat_action import ChatActionSender
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

bot = Bot(token=token)
dp = Dispatcher()
user_data = {}

ChannelName = "@zayavkalar_infosi"

with open("data.json", 'r', encoding="utf-8") as d:
    lang = json.load(d)


@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start":
        await start(message)
    elif message.text in {"🇺🇿 O'zbekcha", '🇷🇺 Русский', '🇺🇸 English'}:
        await menu(message)
    elif message.text in {"📥 CV Yuklash", "📥 Download CV", "📥 Загрузить резюме"}:
        await cv_download_menu(message,bot)
    elif message.text in {"📞 Bog'lanish", "📞 Contact", "📞 Контакты","/contact"}:
        await contact(message)
    elif message.text in {"📨 Telegram"}:
        await tginfo(message)
    elif message.text in {"🔗 Linkedin"}:
        await linkedin(message)
    elif message.text in {"📸 Instagram"}:
        await instainfo(message)
    elif message.text in {"🧑‍💻 Tajriba","🧑‍💻 Experience","🧑‍💻 Опыт","/experience"}:
        await experience(message)
    elif message.text in {"🛒 Korzinka"}:
        await korzinka(message)
    elif message.text in {"🏀⚾️🎾 SportMaster"}:
        await sportmaster(message)
    elif message.text in {"🛍️ Havas"}:
        await havas(message)
    elif message.text in {"🧑‍🏫 Ta'lim","🧑‍🏫 Education","🧑‍🏫 Образование","/education"}:
        await education(message)
    elif message.text in {"🤝💻 Личностные и технические навыки", "🤝💻 soft and hard skills","🤝💻 Shaxsiy va Texnik  ko'nikmalar"}:
        await softandhard(message)
    elif message.text in {"🤝 Личные навыки","🤝 Soft Skills","🤝Shaxsiy ko'nikmalar"}:
        await soft(message)
    elif message.text in {"💻 Технические навыки", "💻 Hard Skills", "💻 Texnik  ko'nikmalar"}:
        await hard(message)
    elif message.text in {"🏫 Kollej","🏫 College","🏫 Колледж"}:
        await kollej(message)
    elif message.text in {"📚 Курсы","📚 Courses","📚 Kurslar"}:
        await courses(message)
    elif message.text in {"🧑‍💻 Ustudy"}:
        await ustudy(message)
    elif message.text in {"🇺🇸 Cambridge"}:
        await cambridge(message)
    elif message.text in {"🧠👈 Supermiya"}:
        await supermiya(message)
    elif message.text in {"💻 Projects", "💻 Loyihalar", "💻 Проекты","/projects"}:
        await projects(message)
    elif message.text  == "🧩 Leetcode":
        await leetcode(message)
    elif message.text in {"💼 GitHub"}:
        await githubinfo(message)
    elif message.text in {"👨‍💻 Портфолио", "👨‍💻 Portfolio", "👨‍💻 Portfolio"}:
        await portfolio(message)
    elif message.text in {"🎯 projcets","🎯 проекты"}:
        await pro(message)


    elif message.text in {"⬅️ Orqaga", "⬅️ Назад", "⬅️ Back"}:
        if user_data[user_id]["state"] in {"cv_download_menu","contact","experience","education", "projects"}:
            await menu(message)
        elif user_data[user_id]["state"] in {"korzinka","havas","sportmaster"}:
            await experience(message)
        elif user_data[user_id]["state"] in {"courses","softandhard","soft","hard"}:
            await education(message)
        elif user_data[user_id]["state"] in {"linkedin","tginfo","instainfo"}:
            await contact(message)






@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text='🇷🇺 Русский'), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
         types.KeyboardButton(text='🇺🇸 English')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f"{lang["🇺🇿 O'zbekcha"][0][0]}"
                         f"{lang['🇷🇺 Русский'][0][0]}\n"
                         f"{lang['🇺🇸 English'][0][0]}\n",reply_markup=keyboard)
    new_user = (f"id:{message.from_user.id}\n"
                f"full name:{message.from_user.full_name}\n"
                f"first name:{message.from_user.first_name}\n"
                f"last name:{message.from_user.last_name}\n"
                f"username:{message.from_user.username}")
    await bot.send_message(ChannelName, new_user)
    print(user_data)





@dp.message(Command(commands=["🇷🇺 Русский", "🇺🇿 O'zbekcha", "🇺🇸 English","⬅️ Orqaga", "⬅️ Назад", "⬅️ Back"]))
async def menu(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "menu"
    if "language" not in user_data[user_id]:
        user_data[user_id]["language"] = message.text
        choose_lang = user_data[user_id]["language"]
        print(message.text)
        button = [
            [types.KeyboardButton(text=f"{lang[choose_lang][1][0]}"),types.KeyboardButton(text=f"{lang[choose_lang][1][1]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][1][2]}"),types.KeyboardButton(text=f"{lang[choose_lang][1][3]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][1][4]}")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer(f"{lang[message.text][1][-1]}",reply_markup=keyboard)
        print(user_data)
    else:
        choose_lang = user_data[user_id]["language"]
        button = [
            [types.KeyboardButton(text=f"{lang[choose_lang][1][0]}"),
             types.KeyboardButton(text=f"{lang[choose_lang][1][1]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][1][2]}"),
             types.KeyboardButton(text=f"{lang[choose_lang][1][3]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][1][4]}")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer(f"{lang[choose_lang][1][-1]}", reply_markup=keyboard)
        print(user_data)



@dp.message(Command(commands=["CV Yuklash 📥", "Download CV 📥", "Загрузить резюме 📥"]))
async def cv_download_menu(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    if "language" in user_data[user_id]:
        user_data[user_id]["state"] = "cv_download_menu"
        choose_lang = user_data[user_id]["language"]
        button = [
            [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        if choose_lang == "🇺🇿 O'zbekcha":
            file_path = "../TgBot_Cv/images/cv_resume_uz.pdf"
        elif choose_lang == "🇷🇺 Русский":
            file_path = "../TgBot_Cv/images/cv_resume_ru.pdf"
        else:
            file_path = "../TgBot_Cv/images/cv_resume_eng.pdf"
        file = FSInputFile(path=file_path)

        async with ChatActionSender.upload_document(bot=bot,chat_id=message.chat.id):
            await message.reply_document(document=file)
        await message.answer(f"{lang[choose_lang][2][0]}", reply_markup=keyboard)
        print(user_data)




@dp.message(Command(commands=["📞 Bog'lanish", "📞 Contact", "📞 Контакты", "/contact"]))
async def contact(message: types.Message):
    user_id = message.from_user.id
    if "language" in user_data[user_id]:
        user_data[user_id]["state"] = "contact"
        choose_lang = user_data[user_id]["language"]
        button = [
            [types.KeyboardButton(text=f"{lang[choose_lang][3][0]}"), types.KeyboardButton(text=f"{lang[choose_lang][3][1]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][3][2]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer(f"{lang[choose_lang][3][-1]}",reply_markup=keyboard)


@dp.message(Command(commands=["📨 Telegram"]))
async def tginfo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "tginfo"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f"{lang[choose_lang][4][0]}",reply_markup=keyboard)
    print(user_data)


@dp.message(Command(commands=["🔗 Linkedin"]))
async def linkedin(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "linkedin"
    choose_lang = user_data[user_id]["language"]
    but = [
        [types.InlineKeyboardButton(text="Link", url="https://www.linkedin.com/in/chayka-aleksandr-861607299?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app")]
    ]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
    ]
    key = types.InlineKeyboardMarkup(inline_keyboard=but, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "images/linkedin.png"
    await message.answer_photo(
        caption=f"{lang[choose_lang][5][-1]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)
    await message.answer(f"{lang[choose_lang][5][0]}",reply_markup=key)
    print(user_data)


@dp.message(Command(commands=["📸 Instagram"]))
async def instainfo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "instainfo"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
    ]
    but = [
        [types.InlineKeyboardButton(text=f"Link",url="https://www.instagram.com/sashbeloov?igsh=MXNidW1nMGZ2ZWh2dw%3D%3D&utm_source=qr"),],
    ]
    file_path = "images/instagram.jpg"
    key = types.InlineKeyboardMarkup(inline_keyboard=but, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer_photo(
        caption=f"{lang[choose_lang][6][0]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)
    await message.answer(f"{lang[choose_lang][6][1]}",reply_markup=key)


@dp.message(Command(commands=["🧑‍💻 Tajriba","🧑‍💻 Experience","🧑‍💻 Опыт","/experience"]))
async def experience(message: types.Message):
    user_id = message.from_user.id
    if "language" in user_data[user_id]:
        user_data[user_id]["state"] = "experience"
        choose_lang = user_data[user_id]["language"]
        button = [
            [types.KeyboardButton(text=f"{lang[choose_lang][7][0]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][7][1]}"), types.KeyboardButton(text=f"{lang[choose_lang][7][2]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")],
        ]
        file_path = "images/experience.jpg"
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer_photo(photo=types.FSInputFile(path=file_path))
        await message.answer(f"{lang[choose_lang][7][-1]}",reply_markup=keyboard)


@dp.message(Command(commands=["🛒 Korzinka"]))
async def korzinka(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "korzinka"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "images/korzinka.jpg"
    await message.answer_photo(
        caption=f"{lang[choose_lang][8][0]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)


@dp.message(Command(commands=["🏀⚾️🎾 SportMaster"]))
async def sportmaster(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "sportmaster"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "images/sportmaster.png"
    await message.answer_photo(
        caption=f"{lang[choose_lang][8][1]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)



@dp.message(Command(commands=["🛍️ Havas"]))
async def havas(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "havas"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "images/havas.png"
    await message.answer_photo(
        caption=f"{lang[choose_lang][8][2]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)



@dp.message(Command(commands=["🧑‍🏫 Ta'lim","🧑‍🏫 Education","🧑‍🏫 Образование","/education"]))
async def education(message: types.Message):
    user_id = message.from_user.id
    if "language" in user_data[user_id]:
        user_data[user_id]["state"] = "education"
        choose_lang = user_data[user_id]["language"]
        button = [
            [types.KeyboardButton(text=f"{lang[choose_lang][9][0]}"),types.KeyboardButton(text=f"{lang[choose_lang][9][1]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][9][2]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")]
        ]
        file_path = "images/education.jpg"
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer_photo(
            caption=f"{lang[choose_lang][9][3]}",
            photo=types.FSInputFile(path=file_path),
            parse_mode="Markdown",
            reply_markup=keyboard)



@dp.message(Command(commands=["🤝💻 Личностные и технические навыки", "🤝💻 soft and hard skills","🤝💻 Shaxsiy va Texnik  ko'nikmalar"]))
async def softandhard(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "softandhard"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][13][0]}"),types.KeyboardButton(text=f"{lang[choose_lang][13][1]}")],
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")],
    ]
    file_path = "images/softandhardskills.png"
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer_photo(
        caption=f"{lang[choose_lang][13][2]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)


@dp.message(Command(commands=["🤝 Личные навыки","🤝 Soft Skills","🤝Shaxsiy ko'nikmalar"]))
async def soft(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "soft"
    choose_lang = user_data[user_id]["language"]
    file_path = "images/softskill.jpg"
    await message.answer_photo(
        caption=f"{lang[choose_lang][14][0]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",)


@dp.message(Command(commands=["💻 Технические навыки", "💻 Hard Skills", "💻 Texnik  ko'nikmalar"]))
async def hard(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "hard"
    choose_lang = user_data[user_id]["language"]
    file_path = "images/hardskill.jpg"
    await message.answer_photo(
        caption=f"{lang[choose_lang][15][0]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",)


@dp.message(Command(commands=["🏫 Kollej","🏫 College","🏫 Колледж"]))
async def kollej(message: types.Message):
    user_id = message.from_user.id
    print(23)
    user_data[user_id]["state"] = "education"
    choose_lang = user_data[user_id]["language"]
    await message.answer(f"{lang[choose_lang][10][0]}")



@dp.message(Command(commands=["📚 Курсы","📚 Courses","📚 Kurslar"]))
async def courses(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "courses"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.KeyboardButton(text=f"{lang[choose_lang][11][0]}")],
        [types.KeyboardButton(text=f"{lang[choose_lang][11][1]}"),types.KeyboardButton(text=f"{lang[choose_lang][11][2]}")],
        [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")],
    ]
    file_path = "images/education.jpg"
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer_photo(
        caption=f"{lang[choose_lang][11][3]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)


@dp.message(Command(commands=["🧑‍💻 Ustudy"]))
async def ustudy(message: types.Message):
    user_id = message.from_user.id
    choose_lang = user_data[user_id]["language"]
    file_path = "images/ustudy.jpeg"
    await message.answer_photo(
        caption=f"{lang[choose_lang][11][4]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",)



@dp.message(Command(commands=["🇺🇸 Cambridge"]))
async def cambridge(message: types.Message):
    user_id = message.from_user.id
    choose_lang = user_data[user_id]["language"]
    file_path = "images/images.jpg"
    await message.answer_photo(
        caption=f"{lang[choose_lang][11][5]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown")



@dp.message(Command(commands=["🧠👈 Supermiya"]))
async def supermiya(message: types.Message):
    user_id = message.from_user.id
    choose_lang = user_data[user_id]["language"]
    file_path = "images/supermiya.jpg"
    await message.answer_photo(
        caption=f"{lang[choose_lang][11][6]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown")


@dp.message(Command(commands=["💻 Projects", "💻 Loyihalar", "💻 Проекты","/projects"]))
async def projects(message: types.Message):
    user_id = message.from_user.id
    if "language" in user_data[user_id]:
        user_data[user_id]["state"] = "projects"
        choose_lang = user_data[user_id]["language"]
        button = [
            [types.KeyboardButton(text=f"{lang[choose_lang][12][0]}"),types.KeyboardButton(text=f"{lang[choose_lang][12][1]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][12][2]}"),types.KeyboardButton(text=f"{lang[choose_lang][12][3]}")],
            [types.KeyboardButton(text=f"{lang[choose_lang][-1][0]}")],
        ]
        file_path = "images/myprojects.jpg"
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer_photo(
            caption=f"{lang[choose_lang][12][4]}",
            photo=types.FSInputFile(path=file_path),
            parse_mode="Markdown",
            reply_markup=keyboard)



@dp.message(Command(commands=["💼 GitHub"]))
async def githubinfo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "githubinfo"
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.InlineKeyboardButton(text="Link",
                                    url="https://github.com/sashbeloov")]
    ]
    file_path = "images/GitHub-logo.png"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer_photo(
        caption=f"{lang[choose_lang][12][4]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)



@dp.message(Command(commands=["👨‍💻 Портфолио","👨‍💻 Portfolio","👨‍💻 Portfolio"]))
async def portfolio(message: types.Message):
    user_id = message.from_user.id
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.InlineKeyboardButton(text='Link',url="https://sashabeloov-portfolio.netlify.app/")]
    ]
    file_path = "images/portfolio-website.jpg"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer_photo(
        caption=f"{lang[choose_lang][12][5]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)



@dp.message(Command(commands=["🎯 projcets","🎯 проекты"]))
async def pro(message: types.Message):
    user_id = message.from_user.id
    choose_lang = user_data[user_id]["language"]
    button = [
        [types.InlineKeyboardButton(text='Chat Doctor', url="https://huggingface.co/sashabeloov/Gemma-2-2b-it-ChatDoctor"),
         types.InlineKeyboardButton(text='House price prediction', url="https://github.com/sashbeloov/AI/blob/main/uy_bor_nn.ipynb")],
        [types.InlineKeyboardButton(text='Car price prediction',
                                    url="https://github.com/sashbeloov/AI/blob/main/Car_price_prediction/cars_pred.ipynb"),
         types.InlineKeyboardButton(text='Heart risk disease',
                                    url="https://github.com/sashbeloov/AI/blob/main/classification/heart_risk.ipynb")],
        [types.InlineKeyboardButton(text='Audio analysis',
                                    url="https://github.com/sashbeloov/pydub-project-test"),
         types.InlineKeyboardButton(text='Student managment system',
                                    url="https://github.com/sashbeloov/student-managment-system")],
        [types.InlineKeyboardButton(text='Loook Telegram Bot',url="https://github.com/sashbeloov/LoookTgBoT"),
         types.InlineKeyboardButton(text='LesAiles Telegram Bot',url="https://github.com/sashbeloov/LesAilesBoT")],
        [types.InlineKeyboardButton(text='Youtube klone', url="https://youtube-cloneuz.netlify.app/"),
         types.InlineKeyboardButton(text='Traveluz', url="https://sayohat-uz.netlify.app/")],
        [types.InlineKeyboardButton(text='Shoesuz', url="https://shoes-uz.netlify.app/"),
         types.InlineKeyboardButton(text='Fast-Food-Uz', url="https://fast-food-uz.netlify.app/")],
        [types.InlineKeyboardButton(text='Parralax-website', url="https://parralax-websitee.netlify.app/"),
         types.InlineKeyboardButton(text='Soat-uz', url="https://soat-uzz.netlify.app/")],
    ]
    file_path = "images/websitee.jpg"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer_photo(
        caption=f"{lang[choose_lang][12][6]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",
        reply_markup=keyboard)


@dp.message(Command(commands=["🧩 Leetcode"]))
async def leetcode(message: types.Message):
    user_id = message.from_user.id
    choose_lang = user_data[user_id]["language"]
    file_path = "images/leetcode_total.jpg"
    await message.answer_photo(
        caption=f"{lang[choose_lang][16][0]}",
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown")



async def main():
    print('The bot is running...')
    await dp.start_polling(bot)
asyncio.run(main())
