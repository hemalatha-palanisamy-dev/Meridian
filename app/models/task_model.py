from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Boolean, func
from app.db.database import Base
import enum
from sqlalchemy.orm import relationship

class TaskCategory(str, enum.Enum):
    OFFICE = "office"
    PERSONAL = "personal"
    HEALTH = "health"
    KIDS = "kids"
    FINANCE = "finance"
    FAMILY = "family"
    OTHER = "other"

class TaskPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SNOOZED = "snoozed"
    CANCELLED = "cancelled"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    category = Column(Enum(TaskCategory, name="task_category_enum"), nullable=False, default=TaskCategory.PERSONAL)
    priority = Column(Enum(TaskPriority, name="task_priority_enum"), nullable=False, default=TaskPriority.MEDIUM)
    due_date = Column(DateTime(timezone=True), nullable=True)
    estimated_minutes = Column(Integer, nullable=True)
    status = Column(Enum(TaskStatus, name="task_status_enum"), nullable=False, default=TaskStatus.PENDING)
    scheduled_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    is_calendar_synced = Column(Boolean, default=False, nullable=False)
    google_calendar_event_id = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False) # pylint: disable=not-callable
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False) # pylint: disable=not-callable

    user = relationship("User", back_populates="tasks")
    notifications = relationship("Notification", back_populates="task",
                             cascade="all, delete-orphan")

