from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from app.db.database import Base
import enum
from sqlalchemy.orm import relationship

class NotificationType(str, enum.Enum):
    EMAIL = "email"
    PUSH = "push"
    SMS = "sms"

class NotificationStatus(str, enum.Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False, index=True)
    notification_type = Column(Enum(NotificationType, name="notification_type_enum"), nullable=False, default=NotificationType.EMAIL)
    scheduled_for = Column(DateTime(timezone=True), nullable=False)
    sent_at = Column(DateTime(timezone=True), nullable=True)
    message = Column(String, nullable=False)
    status = Column(Enum(NotificationStatus, name="notification_status_enum"), nullable=False, default=NotificationStatus.PENDING)
    error_message = Column(String, nullable=True)

    user = relationship("User", back_populates="notifications")
    task = relationship("Task", back_populates="notifications")