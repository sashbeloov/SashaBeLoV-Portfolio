import json

data = {
    '🇺🇿 O\'zbekcha':[
        ["Assalomu Alaykum! Ushbu bot yordamida siz Chayka Aleksandrning portfoliosi bilan tanishib chiqasiz.😊\n\n"],
        ["💻 Loyihalar","🧑‍💻 Tajriba","🧑‍🏫 Ta'lim","📞 Bog'lanish","📥 CV Yuklash",
         "Quyidagi tugmalardan birini tanlang:\n\n"
        "💻 Loyihalar — Mening loyihalarim bilan tanishing.\n\n"
        "🧑‍💻 Tajriba — Tajribam haqida ma'lumot oling.\n\n"
        "🧑‍🏫 Qayerda o‘qiganim haqida ma'lumot oling.\n\n"
        "📞 Bog'lanish — Mening aloqalarimni ko‘rish.\n\n"
        "📥 CV Yuklash — Rezyumeni yuklab olish.\n\n👇👇👇👇"],
        ["Bu mening rezyumem. Yuklab oling! 😊"],
        ["📨 Telegram","🔗 Linkedin","📸 Instagram","Men bilan quyidagi platformalar orqali bog‘lanishingiz mumkin. Tugmalardan birini tanlang:\n👇👇👇👇"],
        ["Men bilan bog'lanish uchun kontaktlar: \n\nhttps://t.me/Belovsasha ✉️ \n\nTelefon raqam: +998-33-545-05-42 ☎️"],
        ["🔗 Linkedin orqali bog'lanish uchun linkni ustiga bosing:\n👇👇👇👇","Linkedin akkauntimga havol:"],
        ["📸 Instagramga havola","Instagram uchun havolani ustiga bosing: \n👇👇👇👇"],
        ["🛒 Korzinka","🏀⚾️🎾 SportMaster","🛍️ Havas"," 🗂 Bu bo'limda siz mening tajribam haqida ma'lumot olasiz.\nTugmalar ustiga bosing va batafsil ma'lumot oling.\n👇👇👇👇👇👇"],
        ["🛒 Korzinka \n\n"
         "2020-2024 🗓\n\n"
         "Lavozim: Bosh Kassir va Kassir nazoratchi.\n\n"
         "Korzinka tarmog‘ida ishlash faoliyatim oddiy kassir sifatida boshlaganman."
         "Ish jarayonida savdo tizimlari, mijozlarga xizmat ko‘rsatish va ish samaradorligini oshirish bo‘yicha ko‘p tajriba orttirdim."
         "Bu menga kassir nazoratchi va katta nazoratchi darajasiga ko‘tarilish imkonini berdi.",
         "🏀⚾️🎾SportMaster \n\n"
         "2024 🗓\n\n"
         "Lavozim: Bosh Kassir.\n\n"
         "Men Sportmaster do‘konida bosh kassir lavozimida faoliyat yuritdim."
         "Bu davrda mijozlarga xizmat ko‘rsatish sifati va kassirlar jamoasining ish jarayonlarini samarali tashkil qilish bo‘yicha tajriba orttirdim."
         "Bosh kassir sifatida savdo operatsiyalarini nazorat qilish va jamoani boshqarishda mas’uliyatli vazifalarni muvaffaqiyatli bajardim.",
         "🛍️ Havas Food \n\n"
         "2020 🗓\n\n"
         "Lavozim: Sotuvchi-kassir.\n\n"
         "Men Havas do‘konida sotuvchi-kassir lavozimida ishladim."
         "Ushbu lavozimda mijozlarga xizmat ko‘rsatish,savdo jarayonlarini boshqarish va kassa amaliyotlarini bajarish bo‘yicha tajriba orttirdim."],
         ["📚 Kurslar", "🏫 Kollej", "🤝💻 Shaxsiy va Texnik  ko'nikmalar", "Bu bo'limda siz mening qaysi ta'lim musassasida o'qiganim va qaysi kurslarni bitirganim haqida to'liq ma'lumot olasiz,hamada shaxsiy va texnik  ko'nikmalar haqida ma'lumot olasiz. 🧑‍💻\nBuning uchun pastdagi tugmalarni ustiga bosing:\n👇👇👇👇👇👇"],
         ["Toshkent Iqtisodiyot Kolleji 🏫\n\nBuxgalteriya hisobi va audit yo'nalishi \n\n2015 – 2018 🗓"
         "\n\nToshkent Iqtisodiyot Kollejida buxgalteriya hisobi va audit yo'nalishi bo'yicha ta'lim oldim. O'qish davomida buxgalteriya hisobi,"
         "moliyaviy tahlil, soliq qonunchiligi va audit metodologiyasi kabi sohalarda chuqur bilimlarga ega bo'ldim."
         "Ushbu yo'nalish bo'yicha amaliyotlar orqali real ish sharoitlarida tejamkor va to'g'ri hisob-kitoblarni amalga oshirish ko'nikmalarini rivojlantirdim. 😊"],
         ["🧑‍💻 Ustudy", "🇺🇸 Cambridge", "🧠👈 Supermiya", "📚 Men o'qigan kurslarim haqida batafsil malunmotlar",
          "💻 Ustudy: Pythonai \n\n2024–2025 📆\n\nUstudy o‘quv markazida Python dasturlash tilini,data analysis va sun’iy intellekt yo‘nalishlarini tahsil olganman."
          "Kurs amaliyotga yo‘naltirilgan va real loyihalar ustida ishlashga yordam berdi.",
          "🇺🇸 Cambridge \n\n"
          "2021-2022 📆\n\n"
          "Cambridge markazida ingliz tilining turli darajalari bo‘yicha chuqur bilimlarga ega bo‘ldim, jumladan Elementary, "
          "Pre-Intermediate va Intermediate bosqichlarini muvaffaqiyatli tugatdim.",
          "🧠👈 Supermiya \n\n2023 📆\n\nSupermiya o‘quv markazida mnemotexnika va intellektual ko‘nikmalarni "
          "rivojlantirish bo‘yicha kurslarda tahsil oldim."],
          ["👨‍💻 Portfolio", "🎯 projcets", "🧩 Leetcode","💼 GitHub", "🧑‍💻 Bu yerda siz menig Loyihalarim bilan tanishib chiqasiz\n",
           "🗂 GitHub orqali siz mening loyihalarimning kodlari bilan tanishib chiqishingiz mumkin \n\nGitHub uchun havolani ustiga bosing: \n👇👇👇👇",
           "Bu tugmani bosish orqali siz mening portfolio websiteimga kirasiz 👇👇👇👇",
           "Loyihalarim bilan tanishish uchun quyidagi tugmalardan birini bosing 👇👇👇👇👇👇"],
          ["🤝Shaxsiy ko'nikmalar", "💻 Texnik  ko'nikmalar", "Bu bo'limda siz mening 🤝💻 Shaxsiy va Texnik  ko'nikmalarim bilan tanishib chiqasiz"],
          ["💬 Muloqot va jamoa bilan ishlash:\nOchiq va aniq muloqot,shuningdek jamoa bilan ishlash qobiliyati menga har qanday ish muhitida boshqalar bilan hamjihatlikda ishlash,"
           "fikr almashish va umumiy maqsad sari harakat qilish imkonini beradi.\n"
           "⏳ Vaqtni boshqarish:\nHar bir ishni oldindan rejalashtiraman."
           "Topshiriqlarni o‘z vaqtida puxta va samarali qilib yakunlayman.\n"
           "🎯 Masulyatni o'z zimmamga olish:\nHar doim ishga jiddiy yondashaman.Mas’uliyatli vazifalardan qochmayman va topshiriqni oxirigacha bajaraman."],
            ["Python - SQL\n"
             "Telegram Bot Development\n"
             "Web Development\n"
             "Data Analysis\n"
             "Data Visualization\n"
             "Web Scraping and Automation\n"
             "Machine Learning\n"
             "Big Data Testing\n"
             "Audio Processing"],
        ["🧩 LeetCode Algoritmik Masalalar\nMen har kuni LeetCode platformasida algoritm va ma’lumotlar "
         "tuzilmasi bo‘yicha 200 ga yaqin masalalarni yechganman,bu menga kod yozish ko‘nikmalarimni rivojlantirmoqda.\n"],


        ["⬅️ Orqaga"]
    ],
    '🇺🇸 English':[
        ["Hello! With this bot, you can explore Chayka Aleksandr's portfolio.😊\n"],
        ["💻 Projects", "🧑‍💻 Experience", "🧑‍🏫 Education", "📞 Contact", "📥 Download CV",
        "Select one of the following buttons:\n\n"
        "💻 Projects — Check out my projects.\n\n"
        "🧑‍💻 Experience — Learn about my experience.\n\n"
        "🧑‍🏫 Education — Learn about my education background.\n\n"
        "📞 Contact — View my contacts.\n\n"
        "📥 Upload CV — Download my resume.\n\n👇👇👇👇"],
        ["This is my resume.You can download 😊"],
        ["📨 Telegram","🔗 Linkedin","📸 Instagram","You can contact me through the following platforms. Please choose one of the buttons:👇👇👇👇"],
        ["To contact me, use the following details:https://t.me/Belovsasha ✉️Phone number: +998-33-545-05-42 ☎️"],
        ["🔗 To connect via Linkedin, click the link below:👇👇👇👇", " Link to my Linkedin profile:"],
        ["📸 Instagram Link", "Click the link below to open Instagram: \n👇👇👇👇"],
        ["🛒 Korzinka","🏀⚾️🎾 SportMaster","🛍️ Havas", " 🗂 In this section, you will learn about my work experience.\nClick the buttons to get more details.\n👇👇👇👇👇👇"],
        ["🛒 Korzinka \n\n"
        "2020–2024 🗓\n\n"
        "Position: Head Cashier and Cashier Supervisor.\n\n"
        "I started my career at the Korzinka retail chain as a regular cashier. "
        "During my work, I gained a lot of experience in sales systems, "
        "customer service, and improving work efficiency. "
        "This allowed me to advance to the level of cashier supervisor and senior supervisor.",
        "🏀⚾️🎾 SportMaster \n\n"
        "2024 🗓\n\n"
        "Position: Head Cashier.\n\n"
        "I worked as a head cashier at the Sportmaster store. "
        "During this period, I gained experience in organizing efficient workflows for the cashier team and "
        "improving customer service quality. "
        "As a head cashier, I successfully handled important responsibilities such as supervising sales operations and managing the team.",
        "🛍️ Havas Food \n\n"
        "2020 🗓\n\n"
        "Position: Sales Cashier.\n\n"
        "I worked as a sales cashier at the Havas store."
        "In this position,I gained experience in customer service,managing sales processes"
        "and performing cashier operations."],
        ["📚 Courses", "🏫 College","🤝💻 soft and hard skills",
        "In this section, you can learn about the educational institutions I attended and the courses I completed, as well as explore my personal and technical skills. 🧑‍💻if you want to know more information click the buttons below:👇👇👇👇👇👇"],
        ["Tashkent College of Economics 🏫\n\nField of Study: Accounting and Audit \n\n2015 – 2018 🗓\n\nI studied Accounting and Audit at the Tashkent College of Economics."
         "During my studies,I gained deep knowledge in areas such as accounting, financial analysis, tax legislation, and audit methodology.Through internships, "
         "I developed practical skills in performing accurate and efficient calculations in real work environments. 😊"],
        ["🧑‍💻 Ustudy", "🇺🇸 Cambridge", "🧠👈 Supermiya", "📚 Detailed information about the courses I have taken",
         "💻 Ustudy: Python AI \n\n2024–2025 📆\n\nAt the Ustudy learning center, I studied Python programming,data analysis and artificial intelligence."
         "The course was practice-oriented and helped me work on real projects.",
         "🇺🇸 Cambridge \n\n2021–2022 📆\n\nAt the Cambridge center, I gained in-depth knowledge of various levels of "
         "English and successfully completed the Elementary, Pre-Intermediate, and Intermediate levels.",
         "🧠👈 Supermiya \n\n2023 📆\n\nAt the Supermiya learning center."
         "I took courses on mnemonics and the development of intellectual skills."],
        ["👨‍💻 Portfolio", "🎯 projcets", "🧩 Leetcode","💼 GitHub", "🧑‍💻 Here you can explore my projects\n",
         "🗂 Through GitHub, you can explore the code of my projects \n\nClick the link below to open GitHub: \n👇👇👇👇",
         "By clicking this button, you will access my portfolio website 👇👇👇👇",
         "Click one of the buttons below to explore my projects 👇👇👇👇👇👇"],
        ["🤝 Soft Skills","💻 Hard Skills","In this section, you will get to know my 🤝💻 Soft and Hard skills."],
        ["💬 Communication and Team work:\nClear and open communication along with strong teamwork skills allow me to collaborate effectively with "
         "others and work towards shared goals in any environment.\n"
         "⏳ Time Management:\nI plan each task in advance and complete it on time,thoroughly and efficiently.\n"
         "🎯 Responsibility:\nI always take my work seriously.I don't avoid responsibility and aim to complete every task to the end."],
        ["Python - SQL\n"
         "Telegram Bot Development\n"
         "Web Development\n"
         "Data Analysis\n"
         "Data Visualization\n"
         "Web Scraping and Automation\n"
         "Machine Learning\n"
         "Big Data Testing\n"
         "Audio Processing"],
        ["🧩 LeetCode Algorithmic Problems\nI solve algorithm and data structure problems on LeetCode almost every day "
         "and I’ve solved nearly 200 problems so far.This is helping me improve my coding skills."],



        ["⬅️ Back"]
    ],
    '🇷🇺 Русский':[
        ["Здравствуйте! С помощью этого бота вы сможете ознакомиться с портфолио Чайка Александра.😊\n"],
        ["💻 Проекты", "🧑‍💻 Опыт", "🧑‍🏫 Образование", "📞 Контакты", "📥 Загрузить резюме",
            "Выберите одну из следующих кнопок:\n\n"
            "💻 Проекты — Ознакомьтесь с моими проектами.\n\n"
            "🧑‍💻 Опыт — Получите информацию о моём опыте.\n\n"
            "🧑‍🏫 Образование — Узнайте о моём образовании.\n\n"
            "📞 Контакты — Посмотреть мои контакты.\n\n"
            "📥 Загрузить резюме — Скачать резюме.\n\n👇👇👇👇"],
        ["Это мое резюме. Вы можете скачать😊"],
        ["📨 Telegram","🔗 Linkedin","📸 Instagram","Вы можете связаться со мной через следующие платформы. Выберите одну из кнопок:👇👇👇👇"],
        ["Для связи со мной используйте следующие контакты:https://t.me/Belovsasha ✉️Телефон: +998-33-545-05-42 ☎️"],
        ["🔗 Чтобы связаться через Linkedin, нажмите на ссылку ниже:👇👇👇👇", "Ссылка на мой профиль в Linkedin:"],
        ["📸 Ссылка на Instagram", "Нажмите на ссылку для перехода в Instagram: \n👇👇👇👇"],
        ["🛒 Korzinka","🏀⚾️🎾 SportMaster","🛍️ Havas", " 🗂 В этом разделе вы узнаете о моем опыте работы.\nНажмите на кнопки, чтобы получить подробную информацию.\n👇👇👇👇👇👇"],
        ["🛒 Korzinka \n\n"
        "2020–2024 🗓\n\n"
        "Должность: Старший кассир и контролер-кассир.\n\n"
        "Я начал свою карьеру в сети Korzinka с позиции обычного кассира. "
        "В процессе работы я приобрел большой опыт в торговых системах, "
        "обслуживании клиентов и повышении эффективности работы."
        "Это дало мне возможность подняться до уровня контролера-кассира и старшего контролера.",
         "🏀⚾️🎾 SportMaster \n\n"
         "2024 🗓\n\n"
         "Должность: Старший кассир.\n\n"
         "Я работал в магазине Sportmaster на должности старшего кассира. "
         "За это время я приобрел опыт в организации эффективной работы кассирской команды и "
         "повышении качества обслуживания клиентов. "
         "Как старший кассир, я успешно выполнял ответственные задачи по контролю торговых операций и управлению командой.",
        "🛍️ Havas Food \n\n"
        "2020 🗓\n\n"
        "Должность: Продавец-кассир.\n\n"
        "Я работал в магазине Havas на должности продавца-кассира. "
        "На этой должности я получил опыт в обслуживании клиентов, управлении торговыми процессами "
        "и выполнении кассовых операций."],
        ["📚 Курсы", "🏫 Колледж","🤝💻 Личностные и технические навыки",
        "В этом разделе вы сможете узнать, в каких учебных заведениях я учился и какие курсы прошёл, а также ознакомиться с моими личностными и техническими навыками. 🧑‍💻Для этого нажмите на кнопки ниже:👇👇👇👇👇👇"],
        ["Ташкентский Экономический Колледж 🏫\n\nСпециальность: Бухгалтерский учет и аудит \n\n2015 – 2018 🗓\n\nЯ получил образование в Ташкентском Экономическом Колледже "
         "по направлению бухгалтерского учета и аудита.В процессе обучения я приобрел глубокие знания в таких областях, как бухгалтерский учет,финансовый анализ,"
         "налоговое законодательство и методология аудита.Благодаря практике я развил навыки точных и экономичных расчетов в реальных рабочих условиях. 😊"],
        ["🧑‍💻 Ustudy", "🇺🇸 Cambridge", "🧠👈 Supermiya", "📚 Подробная информация о курсах, которые я проходил",
         "💻 Ustudy: Python AI \n\n2024–2025 📆\n\nВ учебном центре Ustudy я изучал язык программирования "
         "Python, анализ данных и искусственный интеллект."
         "Курс был ориентирован на практику и помог работать над реальными проектами.",
         "🇺🇸 Cambridge \n\n2021–2022 📆\n\nВ центре Cambridge я получил углублённые знания английского языка на разных "
         "уровнях и успешно завершил уровни Elementary, Pre-Intermediate и Intermediate.",
         "🧠👈 Supermiya \n\n2023 📆\n\nВ учебном центре Supermiya я "
         "проходил курсы по мнемотехнике и развитию интеллектуальных навыков."],
        ["👨‍💻 Портфолио", "🎯 проекты", "🧩 Leetcode","💼 GitHub", "🧑‍💻 Здесь вы можете ознакомиться с моими проектами\n",
         "🗂 Через GitHub вы можете ознакомиться с кодами моих проектов \n\nНажмите на ссылку ниже, чтобы открыть GitHub: \n👇👇👇👇",
         "Нажав на эту кнопку, вы перейдёте на мой сайт-портфолио 👇👇👇👇",
         "Чтобы ознакомиться с моими проектами, нажмите на одну из кнопок ниже 👇👇👇👇👇👇"],
        ["🤝 Личные навыки", "💻 Технические навыки","В этом разделе вы познакомитесь с моими 🤝💻 личными и техническими навыками."],
        ["💬 Коммуникация:\nЧеткое и открытое общение,а также умение работать в команде позволяют мне эффективно взаимодействовать с "
         "коллегами и достигать общих целей в любой рабочей среде.\n"
         "⏳ Управление временем:\nЯ заранее планирую каждую задачу и завершаю её вовремя, качественно и продуктивно.\n"
         "🎯 Ответственность:\nЯ всегда серьёзно подхожу к работе. Не избегаю ответственных задач и стараюсь доводить каждое дело до конца."],
        ["Python - SQL — Работа с языками программирования Python и SQL\n"
         "Разработка Telegram-ботов \n"
         "Веб-разработка\n"
         "Анализ данных\n"
         "Визуализация данных\n"
         "Веб-скрейпинг и автоматизация\n"
         "Машинное обучение\n"
         "Тестирование Big Data\n"
         "Обработка аудио"],
         ["🧩 Алгоритмические задачи на LeetCode\nЯ почти каждый день решаю задачи по алгоритмам и структурам данных на "
          "платформе LeetCode и уже решил около 200 задач.Это помогает мне развивать навыки программирования."],


        ["⬅️ Назад"]
    ],
}

with open("data.json", "w", encoding="utf-8") as d:
    json.dump(data, d, ensure_ascii=False, indent=4)


# async def set_commands(bot: Bot):
#     await bot.set_my_commands(commands, BotCommandScopeDefault())
# commands = [
#     BotCommand(
#         command="start",
#         description="Перезапуск бот"),
#     BotCommand(
#         command="contact",
#         description="Контакты")
# ] await set_commands(bot)







