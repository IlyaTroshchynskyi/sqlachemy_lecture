from datetime import datetime
import enum
from typing import Optional

from sqlalchemy import CheckConstraint, create_engine, DateTime, ForeignKey, func, Index, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker


class Base(DeclarativeBase):
    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            cols.append(f'{col}={getattr(self, col)}')

        return f"<{self.__class__.__name__} {', '.join(cols)}>"


class WorkerModel(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    age: Mapped[int] = mapped_column(Integer, default=18)
    position: Mapped[str] = mapped_column(String(64), server_default='Developer')

    resumes: Mapped[list['ResumeModel']] = relationship(back_populates='worker')


class Workload(enum.Enum):
    part_time = 'part_time'
    full_time = 'full_time'


class ResumeModel(Base):
    __tablename__ = 'resumes'

    __table_args__ = (
        Index('title_index', 'title'),
        CheckConstraint('compensation > 0', name='check_compensation_positive'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    compensation: Mapped[int | None] = mapped_column(Integer, nullable=True)
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete='CASCADE'))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    worker: Mapped['WorkerModel'] = relationship(back_populates='resumes')

    vacancies_replied: Mapped[list['VacanciesModel']] = relationship(
        back_populates='resumes_replied',
        secondary='vacancies_replies',
    )


class VacanciesModel(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    compensation: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    resumes_replied: Mapped[list['ResumeModel']] = relationship(
        back_populates='vacancies_replied',
        secondary='vacancies_replies',
    )


class VacanciesRepliesModel(Base):
    __tablename__ = 'vacancies_replies'

    resume_id: Mapped[int] = mapped_column(
        ForeignKey('resumes.id', ondelete='CASCADE'),
        primary_key=True,
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey('vacancies.id', ondelete='CASCADE'),
        primary_key=True,
    )

    cover_letter: Mapped[Optional[str]]


DB_PORT = '5440'
DB_HOST = 'localhost'
DB_PASSWORD = 'postgres'
DB_USER = 'postgres'
DB_NAME = 'lecture'
DIALECT_DRIVER = 'postgresql+psycopg'

sync_engine = create_engine(f'{DIALECT_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)
session_factory = sessionmaker(sync_engine)


def create_table():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
