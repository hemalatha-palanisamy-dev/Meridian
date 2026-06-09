from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from app.db.database import Base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    google_id = Column(String, unique=True, nullable=True, index=True)
    google_calendar_token = Column(JSONB, nullable=True)
    avatar_url = Column(String, nullable=True)
    schedule_template = Column(JSONB, nullable=True)
    timezone = Column(String, nullable=True)
    notification_preferences = Column(JSONB, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False) # pylint: disable=not-callable
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False) # pylint: disable=not-callable

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
