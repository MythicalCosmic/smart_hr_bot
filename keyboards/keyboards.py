from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config.settings import get_button_text, get_translation
from details.detailes import *

UZ = "🇺🇿 O'zbek Tili"
EN = "🇺🇸 English"
RU = "🇷🇺 Русский"



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




def get_position_details(position_key: str, language: str = 'uz') -> str:
    """Get detailed information about a position"""
    details = POSITION_DETAILS.get(language, POSITION_DETAILS['uz'])
    return details.get(position_key, "❌ Position details not found")


def get_data_summary(state_data: dict, language: str = 'uz') -> str:
    """Generate a formatted summary of all collected user data"""
    labels = DATA_LABELS.get(language, DATA_LABELS['uz'])
    

    summary = f"{labels['summary_title']}\n\n"
    
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
    

    summary = f"{labels['summary_title']}\n\n"
    
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

