from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config.settings import get_button_text, get_translation

# Language selection constants
UZ = "🇺🇿 O'zbek Tili"
EN = "🇺🇸 English"
RU = "🇷🇺 Русский"

JOB_ROLES = {
    'uz': {
        'hr_manager': '👤 HR menejer',
        'manager': '👔 Menejer',
        'cook': '👨‍🍳 Povar (Oshpaz)',
        'cashier': '💰 Kassir',
        'cafe_universal': '☕ Kafening universal hodimi',
        'call_center': '📞 Call center operatori',
        'salesperson': '🛒 Salat tayyorlovchi',
        'courier_driver': '🚗 Kuryer (dostavka)'
    },
    'en': {
        'hr_manager': '👤 HR Manager',
        'manager': '👔 Manager',
        'cook': '👨‍🍳 Cook (Chef)',
        'cashier': '💰 Cashier',
        'cafe_universal': '☕ Cafe Universal Worker',
        'call_center': '📞 Call Center Operator',
        'salesperson': '🛒 Salad Preparer',
        'courier_driver': '🚗 Courier (Delivery)'
    },
    'ru': {
        'hr_manager': '👤 HR менеджер',
        'manager': '👔 Менеджер',
        'cook': '👨‍🍳 Повар (Шеф-повар)',
        'cashier': '💰 Кассир',
        'cafe_universal': '☕ Универсальный работник кафе',
        'call_center': '📞 Оператор колл-центра',
        'salesperson': '🛒 Приготовитель салатов',
        'courier_driver': '🚗 Курьер (доставка)'
    }
}


def language_keyboard() -> ReplyKeyboardMarkup:
    """Language selection keyboard"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UZ)],
            [KeyboardButton(text=EN)],
            [KeyboardButton(text=RU)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def main_keyboard(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Main menu keyboard"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_button_text('register_button', language))],
            [KeyboardButton(text=get_button_text('contact_us_button', language)),
             KeyboardButton(text=get_button_text('settings_button', language))],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def job_roles_keyboard(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Job roles selection keyboard in specified language"""
    roles = JOB_ROLES.get(language, JOB_ROLES['uz'])
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=roles['hr_manager']), 
             KeyboardButton(text=roles['manager'])],
            [KeyboardButton(text=roles['cook']), 
             KeyboardButton(text=roles['cashier'])],
            [KeyboardButton(text=roles['cafe_universal'])],
            [KeyboardButton(text=roles['call_center'])],
            [KeyboardButton(text=roles['salesperson']), 
             KeyboardButton(text=roles['courier_driver'])],
            [KeyboardButton(text=get_button_text('back_button', language))]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def back_keyboard(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Back button keyboard"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_button_text('back_button', language))]
        ],
        resize_keyboard=True
    )

def student_keyboard(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Yes/No keyboard for student question"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_button_text('yes_button', language)),
             KeyboardButton(text=get_button_text('no_button', language))],
            [KeyboardButton(text=get_button_text('back_button', language))]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def phone_number_keyboard(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Phone number sharing keyboard"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_button_text('phone_number_button', language), request_contact=True)],
            [KeyboardButton(text=get_button_text('back_button', language))]
        ],
        resize_keyboard=True
    )


def get_job_role_text(role_key: str, language: str = 'uz') -> str:
    """Get job role text by key and language"""
    roles = JOB_ROLES.get(language, JOB_ROLES['uz'])
    return roles.get(role_key, role_key)


def get_job_role_key_by_text(text: str, language: str = 'uz') -> str:
    """Get job role key by text and language (for handling button clicks)"""
    roles = JOB_ROLES.get(language, JOB_ROLES['uz'])
    for key, value in roles.items():
        if value == text:
            return key
    return None

# Position details in 3 languages - NO SALARY INFORMATION
POSITION_DETAILS = {
    'uz': {
        'hr_manager': """
👤 <b>HR Menejer</b>

📋 <b>Vazifalar:</b>
• Xodimlarni ishga qabul qilish
• Kadrlar bilan ishlash
• Hujjatlarni rasmiylashtirish
• Xodimlar bilan muloqot

⏰ <b>Ish vaqti:</b> 9:00 - 18:00

📋 <b>Talablar:</b>
• Oliy ma'lumot
• HR sohada tajriba
• Kompyuter bilimi
• Kommunikatsiya qobiliyati
        """,
        'manager': """
👔 <b>Menejer</b>

📋 <b>Vazifalar:</b>
• Jamoani boshqarish
• Sotuvni nazorat qilish
• Hisobotlar tayyorlash
• Mijozlar bilan ishlash

⏰ <b>Ish vaqti:</b> 8:00 - 20:00 (smenalarda)

📋 <b>Talablar:</b>
• Boshqaruvda tajriba
• Mas'uliyat hissi
• Stressga chidamlilik
• Liderlik qobiliyati
        """,
        'cook': """
👨‍🍳 <b>Povar (Oshpaz)</b>

📋 <b>Vazifalar:</b>
• Taomlar tayyorlash
• Retseptlarga rioya qilish
• Oshxona tartibini saqlash
• Mahsulotlar sifatini nazorat qilish

⏰ <b>Ish vaqti:</b> 7:00 - 22:00 (smenalarda)

📋 <b>Talablar:</b>
• Oshpazlik tajribasi
• Tez ishlash qobiliyati
• Toza ishlash
• Jamoa bilan ishlash
        """,
        'cashier': """
💰 <b>Kassir</b>

📋 <b>Vazifalar:</b>
• Mijozlarni xizmat qilish
• Pul hisobi
• Kassa bilan ishlash
• Cheklar berish

⏰ <b>Ish vaqti:</b> 8:00 - 22:00 (smenalarda)

📋 <b>Talablar:</b>
• Matematik bilim
• Diqqatlilik
• Mijozlar bilan muloqot
• Mas'uliyat hissi
        """,
        'cafe_universal': """
☕ <b>Kafening universal hodimi</b>

📋 <b>Vazifalar:</b>
• Mijozlarni xizmat qilish
• Taom va ichimlik tayyorlash
• Stollarni tozalash
• Buyurtmalarni qabul qilish

⏰ <b>Ish vaqti:</b> 8:00 - 22:00 (smenalarda)

📋 <b>Talablar:</b>
• Mijozlar bilan ishlash tajribasi
• Tezkorlik
• Jamoaviy ishlash
• Toza va tartibli ishlash
        """,
        'call_center': """
📞 <b>Call center operatori</b>

📋 <b>Vazifalar:</b>
• Mijozlar bilan telefon orqali muloqot
• Buyurtmalarni qabul qilish
• Ma'lumot berish
• Shikoyatlarni hal qilish

⏰ <b>Ish vaqti:</b> 8:00 - 20:00 (smenalarda)

📋 <b>Talablar:</b>
• Yaxshi ovozli nutq
• Sabr-toqat
• Kompyuter bilimi
• Til bilishi (o'zbek, rus)
        """,
        'salesperson': """
🥗 <b>Salat tayyorlovchi</b>

📋 <b>Vazifalar:</b>
• Salatlar tayyorlash
• Ingredientlarni tozalash
• Retseptlarga rioya qilish
• Ish joyini toza saqlash

⏰ <b>Ish vaqti:</b> 7:00 - 21:00 (smenalarda)

📋 <b>Talablar:</b>
• Toza ishlash
• Tezkorlik
• Diqqat bilan ishlash
• Jamoa bilan hamkorlik
        """,
        'courier_driver': """
🚴 <b>Kuryer (dostavka)</b>

📋 <b>Vazifalar:</b>
• Buyurtmalarni yetkazish
• Mijozlar bilan aloqa
• Pul yig'ish
• Transport vositasini parvarish qilish

⏰ <b>Ish vaqti:</b> 10:00 - 23:00 (moslashuvchan)

📋 <b>Talablar:</b>
• Haydovchilik guvohnomasi
• Shaharni yaxshi bilish
• Mas'uliyat hissi
• Mijozlar bilan muloqot
        """,
        'cleaner': """
🧹 <b>Tozalik hodimi</b>

📋 <b>Vazifalar:</b>
• Xonalarni tozalash
• Jihozlarni artish
• Axlat chiqarish
• Tartib-intizomni saqlash

⏰ <b>Ish vaqti:</b> 6:00 - 14:00 yoki 22:00 - 6:00

📋 <b>Talablar:</b>
• Toza va tartibli ishlash
• Mas'uliyat hissi
• Mustaqil ishlash qobiliyati
• Sog'liq holati yaxshi bo'lishi
        """
    },
    'en': {
        'hr_manager': """
👤 <b>HR Manager</b>

📋 <b>Responsibilities:</b>
• Employee recruitment
• Personnel management
• Documentation processing
• Employee communication

⏰ <b>Working hours:</b> 9:00 AM - 6:00 PM

📋 <b>Requirements:</b>
• Higher education
• HR experience
• Computer skills
• Communication abilities
        """,
        'manager': """
👔 <b>Manager</b>

📋 <b>Responsibilities:</b>
• Team management
• Sales control
• Report preparation
• Customer relations

⏰ <b>Working hours:</b> 8:00 AM - 8:00 PM (shifts)

📋 <b>Requirements:</b>
• Management experience
• Responsibility
• Stress resistance
• Leadership skills
        """,
        'cook': """
👨‍🍳 <b>Cook (Chef)</b>

📋 <b>Responsibilities:</b>
• Food preparation
• Following recipes
• Kitchen cleanliness
• Quality control

⏰ <b>Working hours:</b> 7:00 AM - 10:00 PM (shifts)

📋 <b>Requirements:</b>
• Cooking experience
• Fast working ability
• Cleanliness
• Teamwork
        """,
        'cashier': """
💰 <b>Cashier</b>

📋 <b>Responsibilities:</b>
• Customer service
• Money handling
• Cash register operation
• Receipt processing

⏰ <b>Working hours:</b> 8:00 AM - 10:00 PM (shifts)

📋 <b>Requirements:</b>
• Math skills
• Attention to detail
• Customer communication
• Responsibility
        """,
        'cafe_universal': """
☕ <b>Cafe Universal Worker</b>

📋 <b>Responsibilities:</b>
• Customer service
• Food and beverage preparation
• Table cleaning
• Order taking

⏰ <b>Working hours:</b> 8:00 AM - 10:00 PM (shifts)

📋 <b>Requirements:</b>
• Customer service experience
• Speed and efficiency
• Teamwork
• Clean and organized work
        """,
        'call_center': """
📞 <b>Call Center Operator</b>

📋 <b>Responsibilities:</b>
• Customer phone communication
• Order processing
• Information provision
• Complaint resolution

⏰ <b>Working hours:</b> 8:00 AM - 8:00 PM (shifts)

📋 <b>Requirements:</b>
• Clear speech
• Patience
• Computer skills
• Language skills (Uzbek, Russian)
        """,
        'salesperson': """
🥗 <b>Salad Preparer</b>

📋 <b>Responsibilities:</b>
• Salad preparation
• Ingredient cleaning
• Recipe following
• Workspace cleanliness

⏰ <b>Working hours:</b> 7:00 AM - 9:00 PM (shifts)

📋 <b>Requirements:</b>
• Clean work habits
• Speed and efficiency
• Attention to detail
• Team collaboration
        """,
        'courier_driver': """
🚴 <b>Courier (Delivery)</b>

📋 <b>Responsibilities:</b>
• Order delivery
• Customer communication
• Payment collection
• Vehicle maintenance

⏰ <b>Working hours:</b> 10:00 AM - 11:00 PM (flexible)

📋 <b>Requirements:</b>
• Driver's license
• City knowledge
• Responsibility
• Customer communication
        """,
        'cleaner': """
🧹 <b>Cleaner</b>

📋 <b>Responsibilities:</b>
• Room cleaning
• Equipment washing
• Trash removal
• Order maintenance

⏰ <b>Working hours:</b> 6:00 AM - 2:00 PM or 10:00 PM - 6:00 AM

📋 <b>Requirements:</b>
• Clean and organized work
• Responsibility
• Independent work ability
• Good health condition
        """
    },
    'ru': {
        'hr_manager': """
👤 <b>HR Менеджер</b>

📋 <b>Обязанности:</b>
• Набор сотрудников
• Управление персоналом
• Оформление документов
• Общение с сотрудниками

⏰ <b>Рабочее время:</b> 9:00 - 18:00

📋 <b>Требования:</b>
• Высшее образование
• Опыт в HR
• Знание компьютера
• Коммуникативные способности
        """,
        'manager': """
👔 <b>Менеджер</b>

📋 <b>Обязанности:</b>
• Управление командой
• Контроль продаж
• Подготовка отчетов
• Работа с клиентами

⏰ <b>Рабочее время:</b> 8:00 - 20:00 (смены)

📋 <b>Требования:</b>
• Опыт управления
• Ответственность
• Стрессоустойчивость
• Лидерские качества
        """,
        'cook': """
👨‍🍳 <b>Повар (Шеф-повар)</b>

📋 <b>Обязанности:</b>
• Приготовление пищи
• Соблюдение рецептов
• Чистота кухни
• Контроль качества

⏰ <b>Рабочее время:</b> 7:00 - 22:00 (смены)

📋 <b>Требования:</b>
• Опыт готовки
• Быстрота работы
• Чистоплотность
• Работа в команде
        """,
        'cashier': """
💰 <b>Кассир</b>

📋 <b>Обязанности:</b>
• Обслуживание клиентов
• Работа с деньгами
• Работа с кассой
• Выдача чеков

⏰ <b>Рабочее время:</b> 8:00 - 22:00 (смены)

📋 <b>Требования:</b>
• Математические навыки
• Внимательность
• Общение с клиентами
• Ответственность
        """,
        'cafe_universal': """
☕ <b>Универсальный работник кафе</b>

📋 <b>Обязанности:</b>
• Обслуживание клиентов
• Приготовление еды и напитков
• Уборка столов
• Прием заказов

⏰ <b>Рабочее время:</b> 8:00 - 22:00 (смены)

📋 <b>Требования:</b>
• Опыт обслуживания клиентов
• Скорость и эффективность
• Командная работа
• Чистая и организованная работа
        """,
        'call_center': """
📞 <b>Оператор колл-центра</b>

📋 <b>Обязанности:</b>
• Телефонное общение с клиентами
• Обработка заказов
• Предоставление информации
• Решение жалоб

⏰ <b>Рабочее время:</b> 8:00 - 20:00 (смены)

📋 <b>Требования:</b>
• Четкая речь
• Терпение
• Знание компьютера
• Знание языков (узбекский, русский)
        """,
        'salesperson': """
🥗 <b>Приготовитель салатов</b>

📋 <b>Обязанности:</b>
• Приготовление салатов
• Очистка ингредиентов
• Соблюдение рецептов
• Поддержание чистоты рабочего места

⏰ <b>Рабочее время:</b> 7:00 - 21:00 (смены)

📋 <b>Требования:</b>
• Чистая работа
• Скорость и эффективность
• Внимание к деталям
• Командное сотрудничество
        """,
        'courier_driver': """
🚴 <b>Курьер (доставка)</b>

📋 <b>Обязанности:</b>
• Доставка заказов
• Общение с клиентами
• Сбор оплаты
• Уход за транспортным средством

⏰ <b>Рабочее время:</b> 10:00 - 23:00 (гибкий)

📋 <b>Требования:</b>
• Водительские права
• Знание города
• Ответственность
• Общение с клиентами
        """,
        'cleaner': """
🧹 <b>Уборщик</b>

📋 <b>Обязанности:</b>
• Уборка помещений
• Мытье оборудования
• Вынос мусора
• Поддержание порядка

⏰ <b>Рабочее время:</b> 6:00 - 14:00 или 22:00 - 6:00

📋 <b>Требования:</b>
• Чистая и организованная работа
• Ответственность
• Способность к самостоятельной работе
• Хорошее состояние здоровья
        """
    }
}

DATA_LABELS = {
    'uz': {
        'summary_title': '📋 <b>Sizning ma\'lumotlaringiz:</b>',
        'first_name': '👤 <b>Ism:</b>',
        'last_name': '👤 <b>Familiya:</b>',
        'age': '🎂 <b>Yosh:</b>',
        'phone_number': '📞 <b>Telefon raqam:</b>',
        'extra_number': '📱 <b>Qo\'shimcha raqam:</b>',
        'address': '📍 <b>Manzil:</b>',
        'is_student': '🎓 <b>Talaba:</b>',
        'student_level': '📚 <b>O\'qish darajasi:</b>',
        'workplace': '🏢 <b>Oldingi ish joyi:</b>',
        'friend_worker': '👥 <b>Do\'st ishchisi:</b>',
        'expected_salary': '💰 <b>Kutilayotgan maosh:</b>',
        'working_us': '⭐ <b>Bizda ishlash sababi:</b>',
        'about_did': '💼 <b>Nima qilgansiz:</b>',
        'position': '🎯 <b>Lavozim:</b>',
        'photo_status': '📸 <b>Rasm:</b> Yuklandi',
        'yes': 'Ha',
        'no': 'Yo\'q',
        'confirm_data': 'Ma\'lumotlar to\'g\'rimi?'
    },
    'en': {
        'summary_title': '📋 <b>Your Information:</b>',
        'first_name': '👤 <b>First Name:</b>',
        'last_name': '👤 <b>Last Name:</b>',
        'age': '🎂 <b>Age:</b>',
        'phone_number': '📞 <b>Phone Number:</b>',
        'extra_number': '📱 <b>Extra Number:</b>',
        'address': '📍 <b>Address:</b>',
        'is_student': '🎓 <b>Student:</b>',
        'student_level': '📚 <b>Education Level:</b>',
        'workplace': '🏢 <b>Previous Workplace:</b>',
        'friend_worker': '👥 <b>Friend Worker:</b>',
        'expected_salary': '💰 <b>Expected Salary:</b>',
        'working_us': '⭐ <b>Why work with us:</b>',
        'about_did': '💼 <b>What you did:</b>',
        'position': '🎯 <b>Position:</b>',
        'photo_status': '📸 <b>Photo:</b> Uploaded',
        'yes': 'Yes',
        'no': 'No',
        'confirm_data': 'Is the information correct?'
    },
    'ru': {
        'summary_title': '📋 <b>Ваша информация:</b>',
        'first_name': '👤 <b>Имя:</b>',
        'last_name': '👤 <b>Фамилия:</b>',
        'age': '🎂 <b>Возраст:</b>',
        'phone_number': '📞 <b>Номер телефона:</b>',
        'extra_number': '📱 <b>Дополнительный номер:</b>',
        'address': '📍 <b>Адрес:</b>',
        'is_student': '🎓 <b>Студент:</b>',
        'student_level': '📚 <b>Уровень образования:</b>',
        'workplace': '🏢 <b>Предыдущее место работы:</b>',
        'friend_worker': '👥 <b>Друг работник:</b>',
        'expected_salary': '💰 <b>Ожидаемая зарплата:</b>',
        'working_us': '⭐ <b>Почему работать с нами:</b>',
        'about_did': '💼 <b>Что вы делали:</b>',
        'position': '🎯 <b>Должность:</b>',
        'photo_status': '📸 <b>Фото:</b> Загружено',
        'yes': 'Да',
        'no': 'Нет',
        'confirm_data': 'Правильна ли информация?'
    }
}


def get_position_details(position_key: str, language: str = 'uz') -> str:
    """Get detailed information about a position"""
    details = POSITION_DETAILS.get(language, POSITION_DETAILS['uz'])
    return details.get(position_key, "❌ Position details not found")


def get_data_summary(state_data: dict, language: str = 'uz') -> str:
    """Generate a formatted summary of all collected user data"""
    labels = DATA_LABELS.get(language, DATA_LABELS['uz'])
    
    # Start with title
    summary = f"{labels['summary_title']}\n\n"
    
    # Add each field if it exists
    if 'first_name' in state_data:
        summary += f"{labels['first_name']} {state_data['first_name']}\n"
    
    if 'last_name' in state_data:
        summary += f"{labels['last_name']} {state_data['last_name']}\n"
    
    if 'age' in state_data:
        summary += f"{labels['age']} {state_data['age']}\n"
    
    if 'phone_number' in state_data:
        summary += f"{labels['phone_number']} {state_data['phone_number']}\n"
    
    if 'extra_number' in state_data:
        summary += f"{labels['extra_number']} {state_data['extra_number']}\n"
    
    if 'address' in state_data:
        summary += f"{labels['address']} {state_data['address']}\n"
    
    # Handle student status
    if 'level' in state_data:
        summary += f"{labels['is_student']} {labels['yes']}\n"
        summary += f"{labels['student_level']} {state_data['level']}\n"
    else:
        summary += f"{labels['is_student']} {labels['no']}\n"
    
    if 'workplace' in state_data:
        summary += f"{labels['workplace']} {state_data['workplace']}\n"
    
    if 'friend_worker' in state_data:
        summary += f"{labels['friend_worker']} {state_data['friend_worker']}\n"
    
    if 'expected_salary' in state_data:
        summary += f"{labels['expected_salary']} {state_data['expected_salary']}\n"
    
    if 'workin_us' in state_data:
        summary += f"{labels['working_us']} {state_data['workin_us']}\n"
    
    if 'about_did_mess' in state_data:
        summary += f"{labels['about_did']} {state_data['about_did_mess']}\n"
    
    if 'position' in state_data:
        summary += f"{labels['position']} {state_data['position']}\n"
    
    if 'user_photo' in state_data:
        summary += f"{labels['photo_status']}\n"
    
    summary += f"\n❓ <b>{labels['confirm_data']}</b>"
    
    return summary


def get_data_summary(state_data: dict, language: str = 'uz') -> str:
    """Generate a formatted summary of all collected user data"""
    labels = DATA_LABELS.get(language, DATA_LABELS['uz'])
    
    # Start with title
    summary = f"{labels['summary_title']}\n\n"
    
    # Add each field if it exists
    if 'first_name' in state_data:
        summary += f"{labels['first_name']} {state_data['first_name']}\n"
    
    if 'last_name' in state_data:
        summary += f"{labels['last_name']} {state_data['last_name']}\n"
    
    if 'age' in state_data:
        summary += f"{labels['age']} {state_data['age']}\n"
    
    if 'phone_number' in state_data:
        summary += f"{labels['phone_number']} {state_data['phone_number']}\n"
    
    if 'extra_number' in state_data:
        summary += f"{labels['extra_number']} {state_data['extra_number']}\n"
    
    if 'address' in state_data:
        summary += f"{labels['address']} {state_data['address']}\n"
    
    # Handle student status
    if 'level' in state_data:
        summary += f"{labels['is_student']} {labels['yes']}\n"
        summary += f"{labels['student_level']} {state_data['level']}\n"
    else:
        summary += f"{labels['is_student']} {labels['no']}\n"
    
    if 'workplace' in state_data:
        summary += f"{labels['workplace']} {state_data['workplace']}\n"
    
    if 'friend_worker' in state_data:
        summary += f"{labels['friend_worker']} {state_data['friend_worker']}\n"
    
    if 'expected_salary' in state_data:
        summary += f"{labels['expected_salary']} {state_data['expected_salary']}\n"
    
    if 'workin_us' in state_data:
        summary += f"{labels['working_us']} {state_data['workin_us']}\n"
    
    if 'about_did_mess' in state_data:
        summary += f"{labels['about_did']} {state_data['about_did_mess']}\n"
    
    if 'position' in state_data:
        summary += f"{labels['position']} {state_data['position']}\n"
    
    if 'user_photo' in state_data:
        summary += f"{labels['photo_status']}\n"
    
    summary += f"\n❓ <b>{labels['confirm_data']}</b>"
    
    return summary

def confirmation_keyboard(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Final confirmation keyboard"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_button_text('yes_button', language)),
             KeyboardButton(text=get_button_text('no_button', language))],
            [KeyboardButton(text=get_button_text('back_button', language))]
        ],
        resize_keyboard=True
    )

