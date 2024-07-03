from datetime import datetime
import enum

from sqlalchemy import CheckConstraint, DateTime, func, Index, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# сделать константы


class Workload(enum.StrEnum):
    part_time = 'part_time'
    full_time = 'full_time'


class ResumeModel(Base):
    __tablename__ = 'resumes'

    __table_args__ = (
        Index('title_index', 'title'),
        CheckConstraint('compensation > 0', name='check_compensation_positive'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str | None] = mapped_column(String(256))
    compensation: Mapped[int] = mapped_column(Integer, default=0)
    old_compensation: Mapped[int | None] = mapped_column(Integer, server_default='100')
    workload: Mapped[Workload]

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
