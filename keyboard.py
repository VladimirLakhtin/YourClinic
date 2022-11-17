from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


btn_sign_up = KeyboardButton("О нас")
btn_queshion = KeyboardButton("Задать вопрос")
btn_sales = KeyboardButton("Прайс с акциями -50%")
btn_inst = KeyboardButton("Наши работы до-после")
btn_contacts = KeyboardButton("Наши контакты")
kb_mark_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_mark_main.add(btn_sales).row(btn_queshion, btn_inst).add(btn_sign_up).add(btn_contacts)

# btn_site_url = InlineKeyboardButton("Перейти на сайт", url="https://www.your-clinic.pro/")
# inl_kb_mark_site = InlineKeyboardMarkup().add(btn_site_url)

# btn_inst_url = InlineKeyboardButton("Перейти в Instagram", url="https://instagram.com/yourclinic.ru?igshid=YmMyMTA2M2Y=")
# inl_kb_mark_inst = InlineKeyboardMarkup().add(btn_inst_url)

btn_contacts_inst = InlineKeyboardButton("Instagram", url="https://instagram.com/yourclinic.ru?igshid=YmMyMTA2M2Y=")
btn_contacts_site = InlineKeyboardButton("Сайт", url="https://www.your-clinic.pro/")
btn_contacts_tg = InlineKeyboardButton("Telegram", url="https://t.me/YourClinic_pro")
inl_kb_mark_contacts = InlineKeyboardMarkup().add(btn_contacts_inst).add(btn_contacts_tg).add(btn_contacts_site)
inl_kb_mark_inst = InlineKeyboardMarkup().add(btn_contacts_inst)
inl_kb_mark_about = InlineKeyboardMarkup().add(btn_contacts_tg).add(btn_contacts_inst).add(btn_contacts_site)

btn_tg = InlineKeyboardButton("Диалог Telegram", url="https://t.me/yourclinicpro")
btn_num = InlineKeyboardButton("Позвонить", callback_data="call")
inl_kb_mark_queshions = InlineKeyboardMarkup().add(btn_tg).add(btn_num)

btn_sign_up_num = InlineKeyboardButton("По телефону", url="https://clicks.su/gbNLJL")
btn_sign_up_tg = InlineKeyboardButton("Telegram", url="https://t.me/yourclinicpro")
btn_sign_up_site = InlineKeyboardButton("Сайт", url="https://www.your-clinic.pro/")
inl_kb_mark_sign_up = InlineKeyboardMarkup().add(btn_sign_up_num).add(btn_sign_up_tg)

services = ["Брекет системы 12.990₽", "Имплантация 14.990₽", "Лечение кариеса 1.990₽", "Профессиональная гигиена 2.990₽", "Керамические виниры e-max 11.990₽", "Реставрация скола зуба 1.990₽", "Циркониевая коронка 9.990₽", "Удаление зуба 1.990₽"]
inl_kb_mark_services = InlineKeyboardMarkup()
for i, ser in enumerate(services):
    inl_kb_mark_services.add(InlineKeyboardButton(ser, callback_data=f"ser_{i+1}"))
btn_sign_up_num_2 = InlineKeyboardButton("Консультация по телефону  ☎️", url="https://clicks.su/gbNLJL")
btn_sign_up_tg_2 = InlineKeyboardButton("Консультация в Telegram 💬", url="https://t.me/yourclinicpro")
inl_kb_mark_services.add(btn_sign_up_num_2).add(btn_sign_up_tg_2)

btn_sign_up_service = InlineKeyboardButton("Записаться", callback_data="sign_up")
btn_back_service = InlineKeyboardButton("Назад", callback_data="back")
inl_kb_mark_service_description = InlineKeyboardMarkup().add(btn_sign_up_service).add(btn_back_service)

