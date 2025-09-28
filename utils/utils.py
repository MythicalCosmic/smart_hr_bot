from database.models import User, JobApplication, JobPosition, ApplicationDetail
from database.database import SessionLocal
from datetime import datetime
from keyboards.keyboards import get_data_summary, DATA_LABELS


# ============================
# USERS
# ============================

def user_exists(user_id: int) -> bool:
    with SessionLocal() as db:
        return db.query(User).filter(User.id == user_id).first() is not None


def add_user(user_id: int, first_name: str, last_name: str | None, username: str | None):
    with SessionLocal() as db:
        existing_user = db.query(User).filter(User.id == user_id).first()
        if not existing_user:
            user = User(
                id=user_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        return existing_user


def set_user_state(user_id: int, state: str):
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.state = state
            db.commit()


def get_user_state(user_id: int) -> str | None:
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        return user.state if user else None


def get_user_language(user_id: int) -> str | None:
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        return user.language if user else None


def set_user_language(user_id: int, language: str):
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.language = language
            db.commit()


# ============================
# JOB POSITIONS
# ============================

def create_position(title: str, description: str | None = None) -> JobPosition:
    with SessionLocal() as db:
        position = JobPosition(title=title, description=description)
        db.add(position)
        db.commit()
        db.refresh(position)
        return position


def get_position_by_id(position_id: int) -> JobPosition | None:
    with SessionLocal() as db:
        return db.query(JobPosition).filter(JobPosition.id == position_id).first()


def get_all_positions() -> list[JobPosition]:
    with SessionLocal() as db:
        return db.query(JobPosition).all()


def delete_position(position_id: int) -> bool:
    with SessionLocal() as db:
        position = db.query(JobPosition).filter(JobPosition.id == position_id).first()
        if position:
            db.delete(position)
            db.commit()
            return True
        return False


# ============================
# JOB APPLICATIONS
# ============================

def create_application(user_id: int, position_id: int) -> JobApplication:
    with SessionLocal() as db:
        application = JobApplication(
            user_id=user_id,
            position_id=position_id,
            status="pending",
            submitted_at=datetime.utcnow()
        )
        db.add(application)
        db.commit()
        db.refresh(application)
        return application


def get_application_by_id(application_id: int) -> JobApplication | None:
    with SessionLocal() as db:
        return db.query(JobApplication).filter(JobApplication.id == application_id).first()


def get_applications_by_user(user_id: int) -> list[JobApplication]:
    with SessionLocal() as db:
        return db.query(JobApplication).filter(JobApplication.user_id == user_id).all()


def update_application_status(application_id: int, status: str) -> bool:
    with SessionLocal() as db:
        application = db.query(JobApplication).filter(JobApplication.id == application_id).first()
        if application:
            application.status = status
            db.commit()
            return True
        return False


def delete_application(application_id: int) -> bool:
    with SessionLocal() as db:
        application = db.query(JobApplication).filter(JobApplication.id == application_id).first()
        if application:
            db.delete(application)
            db.commit()
            return True
        return False


# ============================
# APPLICATION DETAILS (Dynamic Fields)
# ============================

def add_application_detail(application_id: int, field_name: str, field_value: str, field_type: str = "text", is_required: int = 1) -> ApplicationDetail:
    with SessionLocal() as db:
        detail = ApplicationDetail(
            application_id=application_id,
            field_name=field_name,
            field_value=field_value,
            field_type=field_type,
            is_required=is_required
        )
        db.add(detail)
        db.commit()
        db.refresh(detail)
        return detail


def get_application_details(application_id: int) -> dict:
    """Return details as a dictionary {field_name: field_value}"""
    with SessionLocal() as db:
        details = db.query(ApplicationDetail).filter(ApplicationDetail.application_id == application_id).all()
        return {d.field_name: d.field_value for d in details}


def delete_application_detail(detail_id: int) -> bool:
    with SessionLocal() as db:
        detail = db.query(ApplicationDetail).filter(ApplicationDetail.id == detail_id).first()
        if detail:
            db.delete(detail)
            db.commit()
            return True
        return False
    
def get_position_by_title(title: str):
    db = SessionLocal()
    try:
        return db.query(JobPosition).filter(JobPosition.title == title).first()
    finally:
        db.close()


def save_application_to_database(user_id: int, state_data: dict, language: str) -> int:
    """Save the complete job application to database and return application_id"""
    
    user_info = state_data.get('user_info', {})
    add_user(
        user_id=user_id,
        first_name=state_data.get('first_name', ''),
        last_name=state_data.get('last_name', ''),
        username=user_info.get('username')
    )
    
    position_title = state_data.get('position', 'Unknown Position')
    position = get_position_by_title(position_title) 
    
    if not position:
        position = create_position(title=position_title)
    
    application = create_application(user_id=user_id, position_id=position.id)
    
    detail_fields = {
        "first_name": state_data.get("first_name"),
        "last_name": state_data.get("last_name"),
        "age": state_data.get("age"),
        "phone_number": state_data.get("phone_number"),
        "extra_number": state_data.get("extra_number"),
        "address": state_data.get("address"),
        "is_student": "Yes" if state_data.get("level") else "No",
        "student_level": state_data.get("level"),
        "workplace": state_data.get("workplace"),
        "friend_worker": state_data.get("friend_worker"),
        "expected_salary": state_data.get("expected_salary"),
        "working_us": state_data.get("workin_us"),
        "about_did": state_data.get("about_did_mess"),
        "position": state_data.get("position"),
        "photo_file_id": state_data.get("user_photo"),
        "language": language
    }
    
    for field_name, field_value in detail_fields.items():
        if field_value is not None:
            add_application_detail(
                application_id=application.id,
                field_name=field_name,
                field_value=str(field_value),
                field_type="photo" if field_name == "photo_file_id" else "text"
            )
    
    return application.id


def get_admin_summary(state_data: dict, language: str, application_id: int) -> str:
    """Generate admin notification summary"""
    labels = DATA_LABELS.get(language, DATA_LABELS['uz'])
    
    
    summary = f"🆕 <b>New Job Application #{application_id}</b>\n\n"
    summary += f"👤 <b>Applicant:</b> {state_data.get('first_name', '')} {state_data.get('last_name', '')}\n"
    summary += f"📞 <b>Phone:</b> {state_data.get('phone_number', '')}\n"
    summary += f"🎯 <b>Position:</b> {state_data.get('position', '')}\n"
    summary += f"🌐 <b>Language:</b> {language.upper()}\n"
    summary += f"📅 <b>Submitted:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    

    detail_fields = {
        "first_name": state_data.get("first_name"),
        "last_name": state_data.get("last_name"),
        "age": state_data.get("age"),
        "phone_number": state_data.get("phone_number"),
        "extra_number": state_data.get("extra_number"),
        "address": state_data.get("address"),
        "is_student": labels["yes"] if state_data.get("level") else labels["no"],
        "student_level": state_data.get("level"),
        "workplace": state_data.get("workplace"),
        "friend_worker": state_data.get("friend_worker"),
        "expected_salary": state_data.get("expected_salary"),
        "working_us": state_data.get("workin_us"),
        "about_did": state_data.get("about_did_mess"),
        "position": state_data.get("position"),
        "photo_status": labels["photo_status"] if state_data.get("user_photo") else labels["no"]
    }

    for field, value in detail_fields.items():
        if value:  
            label = labels.get(field, field)
            summary += f"{label} {value}\n"
    
    return summary



