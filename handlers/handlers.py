from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from .states import UserStates
from utils.utils import *
from config.settings import get_button_text, get_translation
from keyboards.keyboards import *
import traceback
from aiogram.exceptions import TelegramForbiddenError
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
import re
import os

ADMIN_ID = [6589960007, 8128453330]  
router = Router()

@router.message(Command('start'))
async def start_handler(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        if user_exists(user_id=user_id) and language is not None:
            await message.reply(get_translation('main_message', language=language), reply_markup=main_keyboard(language=language), parse_mode="HTML")
            await state.set_state(UserStates.main)
            set_user_state(user_id=user_id, state=UserStates.main.state)
        else:
            await message.reply(get_translation("start_message", 'en'), reply_markup=language_keyboard(), parse_mode="HTML")
            await state.set_state(UserStates.set_language)
    except Exception as e:
        await message.reply(f'Error occured in start handler: {e}')



@router.message(lambda message: message.text == get_button_text("back_button", get_user_language(message.from_user.id)), StateFilter(UserStates.regiser_first.state, UserStates.main, UserStates.last_name, UserStates.age, UserStates.phone_number, UserStates.extra_number, UserStates.address, UserStates.student_confirmation, UserStates.student_class_level, UserStates.workplace_old, UserStates.friend_worker, UserStates.workin_us, UserStates.expected_salary, UserStates.about_did, UserStates.position, UserStates.your_im, UserStates.confirmation_data))
async def handle_back(message: Message, state: FSMContext, bot: Bot):
    try:
        current_state = await state.get_state()
        print(current_state)
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)

        async def go_to_main():
            await state.set_state(UserStates.main)  
            set_user_state(user_id, UserStates.main.state) 
            await message.answer(                      
                get_translation("main_message", language=language),
                reply_markup=main_keyboard(language=language),
                parse_mode="HTML"
            )
        async def go_to_first_name():
            await state.set_state(UserStates.regiser_first)
            set_user_state(user_id, UserStates.regiser_first.state)
            await message.answer(
                get_translation("first_name_message", language=language),
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )
        
        async def go_to_last_name():
            await state.set_state(UserStates.last_name)
            set_user_state(user_id, UserStates.last_name.state)
            await message.answer(
                get_translation('last_name_message', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )
        async def go_to_age():
            await state.set_state(UserStates.age)
            set_user_state(user_id, UserStates.age.state)
            await message.answer(
                get_translation('age_message', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )

        async def go_to_phone_number():
            await state.set_state(UserStates.phone_number)
            set_user_state(user_id=user_id, state=UserStates.phone_number.state)
            await message.answer(
                get_translation('phone_number_message', language=language), 
                reply_markup=phone_number_keyboard(language),
                parse_mode='HTML'
            )

        async def go_to_phone_number_extra():
            await state.set_state(UserStates.extra_number)
            set_user_state(user_id=user_id, state=UserStates.extra_number.state)
            await message.answer(
                get_translation('extra_number', language=language), 
                reply_markup=phone_number_keyboard(language),
                parse_mode='HTML'
            )

        async def go_to_address():
            await state.set_state(UserStates.address)
            set_user_state(user_id=user_id, state=UserStates.address.state)
            await message.reply(
                get_translation('address_message', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )

        async def go_to_student_confirmation():
            await state.set_state(UserStates.student_confirmation)
            set_user_state(user_id=user_id, state=UserStates.student_confirmation.state)
            await message.reply(
                get_translation('student_mess', language=language), 
                reply_markup=student_keyboard(language),
                parse_mode='HTML'
            )
        async def go_to_workplace_old():
            await state.set_state(UserStates.workplace_old)
            set_user_state(user_id=user_id, state=UserStates.workplace_old.state)
            await message.reply(
                get_translation('workplace_mess', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )

        async def go_to_friend_worker():
            await state.set_state(UserStates.friend_worker)
            set_user_state(user_id=user_id, state=UserStates.friend_worker.state)
            await message.reply(
                get_translation('friend_worker_mess', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )
        async def go_to_salary():
            await state.set_state(UserStates.expected_salary)
            set_user_state(user_id=user_id, state=UserStates.expected_salary.state)
            await message.reply(
                get_translation('expected_salary_mess', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )
        async def go_to_workin_us():
            await state.set_state(UserStates.workin_us)
            set_user_state(user_id=user_id, state=UserStates.workin_us.state)
            await message.reply(
                get_translation('workin_us_mess', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )

        async def go_to_about_did():
            await state.set_state(UserStates.about_did)
            set_user_state(user_id=user_id, state=UserStates.about_did.state)
            await message.reply(
                get_translation('about_did_mess', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )
        
        async def go_to_position():
            await state.set_state(UserStates.position)
            set_user_state(user_id=user_id, state=UserStates.position.state)
            await message.reply(
                get_translation('position_mess', language=language), 
                reply_markup=job_roles_keyboard(language),
                parse_mode='HTML'
            )

        async def go_to_your_im():
            await state.set_state(UserStates.your_im)
            set_user_state(user_id=user_id, state=UserStates.your_im.state)
            await message.reply(
                get_translation('your_im_mess', language=language), 
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )

        state_actions = {
            UserStates.last_name: go_to_first_name,
            UserStates.regiser_first: go_to_main,
            UserStates.age: go_to_last_name,
            UserStates.age: go_to_last_name,
            UserStates.phone_number: go_to_age,
            UserStates.extra_number: go_to_phone_number,
            UserStates.address: go_to_phone_number_extra,
            UserStates.student_confirmation: go_to_address,
            UserStates.student_class_level: go_to_student_confirmation,
            UserStates.workplace_old: go_to_student_confirmation,
            UserStates.friend_worker: go_to_workplace_old,
            UserStates.expected_salary: go_to_friend_worker,
            UserStates.workin_us: go_to_salary,
            UserStates.about_did: go_to_workin_us,
            UserStates.position: go_to_about_did,
            UserStates.your_im: go_to_position,
            UserStates.confirmation_data: go_to_your_im


        }

        action = state_actions.get(current_state)
        if action:
            await action()
        else:
            await message.answer("Unknown state. Please try again.")

    except Exception as e:
        await message.reply(f'Error occured on handle back: {e}')

@router.message(lambda message: message.text == get_button_text('contact_us_button', get_user_language(message.from_user.id)), StateFilter(UserStates.main))
async def main_contact_us_input(message: Message, state: FSMContext, bot: Bot):
    try:
        language = get_user_language(message.from_user.id)
        caption = get_translation('contact_us', language=language)
        photo_path = FSInputFile("media/photos/qr_code.jpg")


        await bot.send_photo(
                chat_id=message.chat.id,
                photo=photo_path,
                caption=caption,
                parse_mode="HTML",
                reply_markup=main_keyboard(language=language)
        )
    except Exception as e:
        await message.reply(f"⚠️ Error: {e}")

@router.message(lambda message: message.text == get_button_text('settings_button', get_user_language(message.from_user.id)), StateFilter(UserStates.main))
async def main_settings_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        set_user_state(user_id=user_id, state=UserStates.set_language.state)
        await message.reply(get_translation("start_message", 'en'), reply_markup=language_keyboard(), parse_mode="HTML")
        await state.set_state(UserStates.set_language)
    except Exception as e:
        await message.reply(f"⚠️ Error occurred while settings results: {e}")

@router.message(lambda message: message.text in [EN, RU, UZ], StateFilter(UserStates.set_language))
async def set_language_handler(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language_map = {
            "🇺🇸 English": "en",
            "🇺🇿 O'zbek Tili": "uz",
            "🇷🇺 Русский язык": "ru" 
        }
        language = language_map.get(message.text, "ru")
        set_user_state(user_id=user_id, state=UserStates.set_language.state)
        set_user_language(user_id=user_id, language=language)
        user_language = get_user_language(user_id=user_id)
        await message.reply(get_translation('main_message', user_language), reply_markup=main_keyboard(user_language), parse_mode="HTML")
        set_user_state(user_id=user_id, state=UserStates.main.state)
        await state.set_state(UserStates.main)
    except Exception as e:
        await message.reply(f'Error occurred: {e}')


@router.message(lambda message: message.text == get_button_text('register_button', language=get_user_language(message.from_user.id)), StateFilter(UserStates.main))
async def regiser_button_handler(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        set_user_state(user_id=user_id, state=UserStates.regiser_first.state)
        await message.reply(get_translation('first_name_message', language=language), reply_markup=back_keyboard(language=language), parse_mode="HTML")
        await state.set_state(UserStates.regiser_first)
    except Exception as e:
        await message.reply(f'Error occured on regiser button handler: {e}')


@router.message(StateFilter(UserStates.regiser_first))
async def handle_first_name(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        first_name = message.text.strip()
        await state.update_data(first_name=first_name)
        set_user_state(user_id=user_id, state=UserStates.last_name.state)
        await message.reply(
            get_translation('last_name_message', language=language),
            reply_markup=back_keyboard(language=language), parse_mode="HTML"
        )
        await state.set_state(UserStates.last_name)
    except Exception as e:
        await message.reply(f'Error occured on handle first name: {e}')


@router.message(StateFilter(UserStates.last_name))
async def handle_last_name(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        last_name = message.text.strip()
        await state.update_data(last_name=last_name)
        set_user_state(user_id=user_id, state=UserStates.age.state)
        await message.reply(get_translation('age_message', language=language), reply_markup=back_keyboard(language=language), parse_mode='HTML')
        await state.set_state(UserStates.age)
    except Exception as e:
        await message.reply(f'Error occured on handle last name: {e}')

@router.message(StateFilter(UserStates.age))
async def handle_age(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        age = message.text.strip()

        if not age.isdigit() or not (16 <= int(age) <= 50): 
            await message.reply(
                get_translation('age_message', language=language),
                reply_markup=back_keyboard(language),
                parse_mode='HTML'
            )
            return
        await state.update_data(age=age)
        set_user_state(user_id=user_id, state=UserStates.phone_number.state)
        await message.reply(
            get_translation('phone_number_message', language=language),
            reply_markup=phone_number_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.phone_number)

    except Exception as e:
        await message.reply(f'Error occurred: {e}')


@router.message(StateFilter(UserStates.phone_number))
async def handle_phone_number(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)


        if message.contact and message.contact.phone_number:
            phone_number = message.contact.phone_number
        elif message.text:
            phone_number = message.text.strip()
        else:
            phone_number = None

 
        if phone_number:
            phone_number = re.sub(r"[^\d+]", "", phone_number)

            if not phone_number.startswith('+'):
                phone_number = '+' + phone_number

        if not phone_number or not re.fullmatch(r"\+\d{7,15}", phone_number):
            await message.reply(
                get_translation('phone_number_invalid', language=language),
                reply_markup=phone_number_keyboard(language=language),
                parse_mode='HTML'
            )
            return


        await state.update_data(phone_number=phone_number)
        set_user_state(user_id, state=UserStates.extra_number.state)
        await state.set_state(UserStates.extra_number)

        await message.reply(
            get_translation('extra_number', language=language),
            reply_markup=back_keyboard(language),
            parse_mode='HTML'
        )

    except Exception as e:
        await message.reply(f"Error occurred on handle number: {e}")


@router.message(StateFilter(UserStates.extra_number))
async def handle_phone_number_extra(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)


        if message.contact and message.contact.phone_number:
            phone_number = message.contact.phone_number
        elif message.text:
            phone_number = message.text.strip()
        else:
            phone_number = None

 
        if phone_number:
            phone_number = re.sub(r"[^\d+]", "", phone_number)

            if not phone_number.startswith('+'):
                phone_number = '+' + phone_number

        if not phone_number or not re.fullmatch(r"\+\d{7,15}", phone_number):
            await message.reply(
                get_translation('phone_number_invalid', language=language),
                parse_mode='HTML'
            )
            return

        await state.update_data(extra_number=phone_number)
        set_user_state(user_id, state=UserStates.address.state)
        await state.set_state(UserStates.address)

        await message.reply(
            get_translation('address_message', language=language),
            reply_markup=back_keyboard(language),
            parse_mode='HTML'
        )

    except Exception as e:
        await message.reply(f"Error occurred on handle number: {e}")


@router.message(StateFilter(UserStates.address))
async def handle_address_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        address = message.text.strip()
        await state.update_data(address=address)
        set_user_state(user_id=user_id, state=UserStates.student_confirmation.state)
        await message.reply(
            get_translation('student_mess', language=language),
            reply_markup=student_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.student_confirmation)
    except Exception as e:
        await message.reply(f"Error occured on address input: {e}")

@router.message(lambda message: message.text == get_button_text('yes_button', language=get_user_language(message.from_user.id)), StateFilter(UserStates.student_confirmation))
async def handle_student_confirmation_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        set_user_state(user_id=user_id, state=UserStates.student_class_level.state)
        await message.reply(
            get_translation('student_class_level_mess', language=language),
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.student_class_level)
    except Exception as e:
        await message.reply(f"Error occured on address input: {e}")

@router.message(lambda message: message.text == get_button_text('no_button', language=get_user_language(message.from_user.id)), StateFilter(UserStates.student_confirmation))
async def handle_student_confirmation_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        set_user_state(user_id=user_id, state=UserStates.workplace_old.state)
        await message.reply(
            get_translation('workspace_mess', language=language),
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.workplace_old)
    except Exception as e:
        await message.reply(f"Error occured on address input: {e}")


@router.message(StateFilter(UserStates.student_class_level))
async def handle_student_class_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        level = message.text.strip()
        await state.update_data(level=level)
        set_user_state(user_id=user_id, state=UserStates.workplace_old.state)
        await message.reply(
            get_translation('workspace_mess', language=language),
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.workplace_old)

    except Exception as e:
        pass

@router.message(StateFilter(UserStates.workplace_old))
async def handle_student_class_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        workplace = message.text.strip()
        await state.update_data(workplace=workplace)
        set_user_state(user_id=user_id, state=UserStates.friend_worker.state)
        await message.reply(
            get_translation('friend_worker_mess', language=language),
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.friend_worker)

    except Exception as e:
        pass

@router.message(StateFilter(UserStates.friend_worker))
async def handle_student_class_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        friend_worker = message.text.strip()
        await state.update_data(friend_worker=friend_worker)
        set_user_state(user_id=user_id, state=UserStates.expected_salary.state)
        await message.reply(
            get_translation('expected_salary_mess', language=language),
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.expected_salary)

    except Exception as e:
        pass

@router.message(StateFilter(UserStates.expected_salary))
async def handle_student_class_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        expected_salary = message.text.strip()
        await state.update_data(expected_salary=expected_salary)
        set_user_state(user_id=user_id, state=UserStates.workin_us.state)
        await message.reply(
            get_translation('workin_us_mess', language=language),
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.workin_us)

    except Exception as e:
        pass

@router.message(StateFilter(UserStates.workin_us))
async def handle_student_class_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        workin_us = message.text.strip()
        await state.update_data(workin_us=workin_us)
        set_user_state(user_id=user_id, state=UserStates.about_did.state)
        await message.reply(
            get_translation('about_did_mess', language=language),
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.about_did)

    except Exception as e:
        pass

@router.message(StateFilter(UserStates.about_did))
async def handle_student_class_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        about_did_mess = message.text.strip()
        await state.update_data(about_did_mess=about_did_mess)
        set_user_state(user_id=user_id, state=UserStates.position.state)
        await message.reply(
            get_translation('position_mess', language=language),
            reply_markup=job_roles_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.position)

    except Exception as e:
        pass


@router.message(StateFilter(UserStates.position))
async def handle_student_class_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        position = message.text.strip()
        await state.update_data(position=position)
        position_key = get_job_role_key_by_text(message.text.strip(), language)
        position_details = get_position_details(position_key, language)
        set_user_state(user_id=user_id, state=UserStates.your_im.state)
        await message.reply(
            position_details + f"\n\n\n <b>{get_translation('your_im_mess', language)}</b>",
            reply_markup=back_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.your_im)

    except Exception as e:
        pass


@router.message(StateFilter(UserStates.your_im))
async def handle_image_upload(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        
        if message.photo:
            photo = message.photo[-1]
            photo_file_id = photo.file_id
            await state.update_data(user_photo=photo_file_id)
            
            state_data = await state.get_data()
            
            state_data = await state.get_data()  
            
            data_summary = get_data_summary(state_data, language)
            
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_file_id,
                caption=data_summary,
                reply_markup=confirmation_keyboard(language=language),
                parse_mode='HTML'
            )
            
            try:
                application_id = save_application_to_database(user_id, state_data, language)
                
                admin_summary = get_admin_summary(state_data, language, application_id)
                
                for admin_id in ADMIN_ID:
                    try:
                        await bot.send_photo(
                            chat_id=admin_id,
                            photo=photo_file_id,
                            caption=admin_summary,
                            parse_mode='HTML'
                        )
                    except Exception as admin_error:
                        print(f"Failed to send to admin {admin_id}: {admin_error}")
                
            except Exception as db_error:
                print(f"Database error: {db_error}")
            
            set_user_state(user_id=user_id, state=UserStates.confirmation_data.state) 
            await state.set_state(UserStates.confirmation_data)
            
        else:
            await message.reply(
                get_translation('please_send_photo_message', language=language),
                reply_markup=back_keyboard(language=language),
                parse_mode='HTML'
            )
            
    except Exception as e:
        await message.reply(f"Error in image upload: {str(e)}")

@router.message(lambda message: message.text == get_button_text('yes_button', language=get_user_language(message.from_user.id)), StateFilter(UserStates.confirmation_data))
async def handle_student_confirmation_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        set_user_state(user_id=user_id, state=UserStates.main.state)
        await message.reply(
            get_translation('main_message', language=language),
            reply_markup=main_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.main)
    except Exception as e:
        await message.reply(f"Error occured on address input: {e}")

@router.message(lambda message: message.text == get_button_text('no_button', language=get_user_language(message.from_user.id)), StateFilter(UserStates.confirmation_data))
async def handle_student_confirmation_input(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        set_user_state(user_id=user_id, state=UserStates.main.state)
        await message.reply(
            get_translation('canceled_mess', language=language),
            reply_markup=main_keyboard(language=language),
            parse_mode='HTML'
        )
        await state.set_state(UserStates.main)
    except Exception as e:
        await message.reply(f"Error occured on address input: {e}")

@router.message(StateFilter(UserStates.set_language, UserStates.main, UserStates.student_confirmation, UserStates.position, UserStates.confirmation_data))
async def handle_unrecognized_input(message: Message, state: FSMContext, bot: Bot):
    try:
        current_state = await state.get_state()
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        state_responses = {
            UserStates.set_language: {
                "text": get_translation('start_message', language=language),
                "keyboard": language_keyboard()
            },
            UserStates.student_confirmation: {
                "text": get_translation('student_mess', language=language),
                "keyboard": student_keyboard(language=language)
            },
            UserStates.position: {
                "text": get_translation('positon_mess', language=language),
                "keyboard": job_roles_keyboard(language=language)
            },
            UserStates.position: {
                "text": get_translation('confirmation_data_mess', language=language),
                "keyboard": confirmation_keyboard(language=language)
            },
        }
        response = state_responses.get(current_state, {
            "text": get_translation('main_message', language=language),
            "keyboard": main_keyboard(language=language)
        })

        await message.reply(
            response['text'],
            reply_markup=response['keyboard'],
            parse_mode='HTML'
        )

    except Exception as e:
        await message.reply(f'Error occured on handle_unrecognized_input handler: {e}')

@router.message(StateFilter(UserStates.main))
async def main_handler(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        await message.reply(get_translation('main_message', language=language), reply_markup=main_keyboard(language=language), parse_mode="HTML")
        set_user_state(user_id=user_id, state=UserStates.main.state)
    except Exception as e:
        await message.reply(f"Error occured: {e}")


@router.message()
async def fallback_handler(message: Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        language = get_user_language(user_id=user_id)
        if user_exists(user_id=user_id) and language is not None:
            await message.reply(get_translation('main_message', language=language), reply_markup=main_keyboard(language=language), parse_mode="HTML")  
            await state.set_state(UserStates.main)
            set_user_state(user_id=user_id, state=UserStates.main.state)

        else:
            await message.reply(get_translation('start_message', 'uz'), reply_markup=language_keyboard(), parse_mode='HTML')
            await state.set_state(UserStates.start)
            await set_user_state(user_id=user_id, state=UserStates.main.state)          
    except Exception as e:
        await message.reply(f"Error occured on fallback_handler: {e}")
