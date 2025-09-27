from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    state = Column(String)
    language = Column(String)
    username = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # FIXED: relationship to JobApplication, not User
    applications = relationship("JobApplication", back_populates="user")


class JobPosition(Base):
    __tablename__ = "job_positions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)  
    description = Column(String, nullable=True)

    applications = relationship("JobApplication", back_populates="position")


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    position_id = Column(Integer, ForeignKey("job_positions.id"), nullable=False)
    status = Column(String, default="pending")  
    submitted_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="applications")
    position = relationship("JobPosition", back_populates="applications")
    details = relationship("ApplicationDetail", back_populates="application")


class ApplicationDetail(Base):
    __tablename__ = "application_details"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("job_applications.id"), nullable=False)

    field_name = Column(String, nullable=False)   
    field_value = Column(String, nullable=False)  
    field_type = Column(String, nullable=True)       

    is_required = Column(Integer, default=1)   # better: Boolean
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    application = relationship("JobApplication", back_populates="details")
